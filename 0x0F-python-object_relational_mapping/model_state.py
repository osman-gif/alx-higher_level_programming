#!/usr/bin/python3
"""Write a python file that contains the class definition
of a State and an instance Base = declarative_base():

    State class:
        inherits from Base Tips
        links to the MySQL table states
        class attribute id that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
        class attribute name that represents a column of a string with
        maximum 128 characters and can’t be null
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import sys


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    
