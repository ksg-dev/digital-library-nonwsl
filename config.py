import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

load_dotenv()


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DB_URI"]


class Base(DeclarativeBase):
    pass

