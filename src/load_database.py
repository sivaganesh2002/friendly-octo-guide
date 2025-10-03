from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

import os
from dotenv import load_dotenv

import pandas as pd

import uuid
import sys

import psycopg2
from utils.db_handler import DatabaseHandler

load_dotenv(override=True)

URL_database = os.environ.get("External_Database_Url")
engine = DatabaseHandler(db_url=URL_database)

users_df = pd.read_csv("data/users.csv")
games_df = pd.read_csv("data/games.csv")
user_games_df = pd.read_csv("data/stream_user_games.csv")
user_recommendations_df = pd.read_csv("data/user_recommendations.csv")
game_tags_df = pd.read_csv("data/game_tags.csv")

user_table_create_query = """
    create table if not exists users (
        id UUID PRIMARY KEY,
        username VARCHAR(255) unique not null,
        password VARCHAR(255) not null,
        email VARCHAR(255) unique not null,
        role VARCHAR(50) not null,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
"""

game_table_create_query = """
    create table if not exists games (
        id UUID PRIMARY KEY,
        appid VARCHAR(255) unique not null,
        name VARCHAR(255) not null,
        type VARCHAR(255),
        is_free BOOLEAN DEFAULT FALSE,
        short_decription TEXT,
        detailed_description TEXT,
        developer VARCHAR(255),
        publisher VARCHAR(255),
        price VARCHAR(255),
        genres VARCHAR(255),
        categories VARCHAR(255),
        release_date VARCHAR(255),
        platforms TEXT,
        metacritic_score FLOAT,
        recommendations INTEGER
    )
"""

user_games_query = """
    create table if not exists user_games (
        id UUID PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        appid VARCHAR(255) NOT NULL,
        shelf VARCHAR(50) DEFAULT 'wish_list',
        rating FLOAT DEFAULT 0.0,
        review TEXT
    )
"""

recommendations_table_create_query = """
    create table if not exists user_recommendations (
        id UUID PRIMARY KEY,
        username VARCHAR(255),
        appid VARCHAR(255),
        similarity FLOAT
    )
"""

game_tags_create_query = """
    create table if not exists game_tags (
        id UUID PRIMARY KEY,
        appid VARCHAR(255) not null,
        category VARCHAR(255) not null
    )
"""

# running queries to create tables
engine.delete_table('users')
engine.delete_table('games')
engine.delete_table('user_games')
engine.delete_table('user_recommendations')
engine.delete_table('game_tags')

# creating tables
engine.create_table(user_table_create_query)
engine.create_table(game_table_create_query)
engine.create_table(user_games_query)
engine.create_table(recommendations_table_create_query)
engine.create_table(game_tags_create_query)

# ensuring each row of each dataframe has a UUID
if 'id' not in users_df.columns:
    users_df['id'] = [str(uuid.uuid4()) for _ in range(len(users_df))]
if 'id' not in games_df.columns:
    games_df['id'] = [str(uuid.uuid4()) for _ in range(len(games_df))]
if 'id' not in user_games_df.columns:
    user_games_df['id'] = [str(uuid.uuid4()) for _ in range(len(user_games_df))]
if 'id' not in user_recommendations_df.columns:
    user_recommendations_df['id'] = [str(uuid.uuid4()) for _ in range(len(user_recommendations_df))]
if 'id' not in game_tags_df.columns:
    game_tags_df['id'] = [str(uuid.uuid4()) for _ in range(len(game_tags_df))]

# inserting data into tables
engine.insert_data(users_df, 'users')
engine.insert_data(games_df, 'games')
engine.insert_data(user_games_df, 'user_games')
engine.insert_data(user_recommendations_df, 'user_recommendations')
engine.insert_data(game_tags_df, 'game_tags')

# testing if tables exist and have data
print(engine.test_table('users'))
print(engine.test_table('games'))
print(engine.test_table('user_games'))
print(engine.test_table('user_recommendations'))
print(engine.test_table('game_tags'))