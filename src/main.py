from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from uuid import UUID, uuid4

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from dotenv import load_dotenv
import os

load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from src.model import User, Game, GameModel, UserModel,  UserGameModel, UserGame, GameSimilarity
from src.similarity import UserRecommendation



