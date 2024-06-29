#!/usr/bin/python3
""" Write a python file that contains the class definition of a State
and an instance Base = declarative_base()
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)