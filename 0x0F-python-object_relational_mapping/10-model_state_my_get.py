#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    n = sys.argv[4]

    engine = create_engine('mysql://{}:{}@localhost/{}'.format(usr, pwd, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    my_session = Session()

    states = my_session.query(State).filter_by(name=n).order_by(State.id).all()

    if states:
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')
