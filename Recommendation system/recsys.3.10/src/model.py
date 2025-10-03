from pydantic import BaseModel
from uuid import UUID, uuid4
import uuid
from typing import Optional, List
from enum import Enum
from sqlalchemy import Column, Float, String, Integer
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship

Base = declarative_base()

# Game model
class Game(Base):
    __tablename__ = "optigame_products" 

    id = Column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    appid = Column(String, unique=True, nullable=False)  
    name = Column(String, nullable=False)  
    type = Column(String, nullable=True)  
    is_free = Column(pg.BOOLEAN, nullable=True, default=False)  #
    short_description = Column(String, nullable=True)  
    detailed_description = Column(String, nullable=True)  
    developers = Column(String, nullable=True)  
    publishers = Column(String, nullable=True)  
    price = Column(String, nullable=True)  
    genres = Column(String, nullable=True)  
    categories = Column(String, nullable=True)  
    release_date = Column(String, nullable=True)  
    platforms = Column(String, nullable=True)  
    metacritic_score = Column(Float, nullable=True)  
    recommendations = Column(Integer, nullable=True)  

# Pydantic model for data validation and serialization
class GameModel(BaseModel):
    id: Optional[UUID] = None
    appid: str
    name: str
    type: Optional[str] = None
    is_free: Optional[bool] = False
    short_description: Optional[str] = None
    detailed_description: Optional[str] = None
    developers: Optional[str] = None
    publishers: Optional[str] = None
    price: Optional[str] = None
    genres: Optional[str] = None
    categories: Optional[str] = None
    release_date: Optional[str] = None
    platforms: Optional[str] = None
    metacritic_score: Optional[float] = None
    recommendations: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True 


# User model
class User(Base):
    __tablename__ = "users"  

    id = Column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, nullable=False)


class UserModel(BaseModel):
    id: Optional[UUID] = None
    username: str
    password: str
    email: str
    role: str

    class Config:
        orm_mode = True 
        from_attributes = True 



# user_id:game_id mapping model
class UserGame(Base):
    __tablename__ = "user_games"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    appid = Column(String, nullable=False)
    shelf = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    review = Column(String, nullable=False)


class UserGameModel(BaseModel):
    id: Optional[UUID]  = None
    username: str
    appid: str
    shelf: Optional[str] = None
    rating: Optional[float] = None
    review: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True


# Game Similarity model
class GameSimilarity(Base):
    __tablename__ = "game_similarity"  

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    game1 = Column(String, nullable=False)
    game2 = Column(String, nullable=False)
    similarity = Column(Float, nullable=False)
    
class GameSimilarityModel(BaseModel):
    id: Optional[UUID] = None
    game1: str
    game2: str
    similarity: float

    class Config:
        orm_mode = True 
        from_attributes = True



# UserRecommendation model
class UserRecommendation(Base):
    __tablename__ = "user_recommendations" 

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    appid = Column(String, nullable=False)
    similarity = Column(Float, nullable=False)
    
class UserRecommendationModel(BaseModel):
    id: Optional[UUID] = None
    username: str
    appid: str
    similarity: float

    class Config:
        orm_mode = True 
        from_attributes = True 