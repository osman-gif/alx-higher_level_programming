"""
 python file that contains the class definition of a State
 and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


# declare a mapping
Base = declarative_base()
# create class


class State(Base):
    """This class models a state
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
