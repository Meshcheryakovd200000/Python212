from sqlalchemy import create_engine  # метод для создания настроек
from sqlalchemy.ext.declarative import declarative_base  # для определения таблиц и моделей
from sqlalchemy.orm import sessionmaker  # сделаем возможность работы с сессиями


DATABASE_NAME = 'student.db'

engine = create_engine(f"sqlite:///{DATABASE_NAME}")  # create_engine создаст sqlite БД-student.db
Session = sessionmaker(bind=engine)  # отвечает за все обращения к БД

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
