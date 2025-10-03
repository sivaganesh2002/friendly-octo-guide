from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
from src.model import UserGame, UserRecommendation
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import uuid
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRec:
    def __init__(self, db_session: Session, url: str):
        self.db = db_session
        self.url = url # Database connection URL
        self.engine = create_engine(url)

    def fetch_user_game(self, username: str) -> pd.DataFrame:
        """Fetch all games for speicific user from the database."""
        query = text("SELECT username, appid FROM user_games WHERE username = :username")
        with self.engine.connect() as connection:
            df = pd.read_sql_query(query, connection, params={"username" : username})
            return df
    def fetch_all_category(self) -> pd.DataFrame:
        """Fetch all game tags from the database."""
        query = text("SELECT appid, category FROM game_tags")
        with self.engine.connect() as connection:
            df = pd.read_sql_query(query, connection)
            return df

    def create_game_vector(self, tag_df: pd.DataFrame) -> tuple[pd.DataFrame, List[str], List[str]]:
        """Create game vectors from tags """
        unique_tags = tag_df['category'].drop_duplicates().tolist()
        unique_games = tag_df['appid'].drop_duplicates().tolist()

        game_vec = []
        for game in unique_games:
            tags = tag_df[tag_df['appid'] == game]["category"].tolist()
            vec = [1 if tag in tags else 0 for tag in unique_tags]
            game_vec.append(vec)

        df = pd.DataFrame(game_vec, index=unique_games, columns=unique_tags)
        return df, unique_tags, unique_games

    def create_user_vector(self, user_games: pd.DataFrame, game_vector: pd.DataFrame, unique_tags: List[str]) -> pd.DataFrame:
        """Create user vector from their played games."""
        if user_games.empty:
            return pd.DataFrame([[0] * len(unique_tags)], columns=unique_tags, index=['unknown_user'])
        username = user_games.iloc[0]['username']
        user_game = user_games['appid'].tolist()

        user_game_vec = [g for g in user_game if g in game_vector.index]
        if not user_game_vec:
            user_vector = [0] * len(unique_tags)
        else:
            played_game_vec = game_vector.loc[user_game_vec]
            user_vector = played_game_vec.mean(axis=0).tolist()
        df = pd.DataFrame([user_vector], columns=unique_tags, index=[username])
        return df

    def calc_user_rec(self, user_vector: pd.DataFrame, game_vector: pd.DataFrame, top_n: int) -> pd.DataFrame:
        """Calculate similarity between user vector and all game vectors."""
        username = user_vector.index[0]
        user_vector_data = user_vector.iloc[0].values.reshape(1, -1)

        # calculate cosine similarity
        similarities = cosine_similarity(user_vector_data, game_vector)
        similarities = pd.DataFrame(similarities.T, index=game_vector.index, columns=[username])

        top_game = similarities[username].nlargest(top_n)
        recommendation = []
        for appid, sim in top_game.items():
            recommendation.append({
                "username" : username,
                "appid" : appid,
                "similarity" : float(sim)
            })

        return pd.DataFrame(recommendation)

    def delete_existing_recommendations(self, username: str):
        """Delete existing recommendations for the user."""
        self.db.query(UserRecommendation).filter(UserRecommendation.username == username).delele()
        self.db.commit()

    def save_recommendations(self, rec_df: pd.DataFrame):
        """save new recommendations to the database."""
        for _, row in rec_df.iterrows():
            rec = UserRecommendation(
                id = uuid.uuid4(),
                username = row['username'],
                appid = row['appid'],
                similarity = row['similarity']
            )
            self.db.add(rec)
        self.db.commit()

    def recommend(self, username: str, top_n: int = 20):
        """Main function to generate for user `username`."""
        try:
            logger.info("recommend generation for " + username + " ...")
            # fetch user games
            user_games_df = self.fetch_user_game(username)
            if user_games_df.empty:
                logger.warning(f"No games found for user {username}. No recommendations generated.")
                return

            # fetch all game tags
            tag_df = self.fetch_all_category()
            if tag_df.empty:
                logger.error("No game tags found in the database.")
                return
            
            # create game, user vectors
            game_vector, unique_tags, unique_games = self.create_game_vector(tag_df)
            user_vector = self.create_user_vector(user_games_df, game_vector, unique_tags)

            # calculate recommendations
            rec = self.calc_user_rec(user_vector, game_vector, top_n)
            self.delete_existing_recommendations(username)
            self.save_recommendations(rec)

            logger.info(f"Recommendations for {username} generated and saved ")
        
        except Exception as e:
            logger.error(f"Error generating recommendations for {username}: {e}")
            self.db.rollback()
            raise