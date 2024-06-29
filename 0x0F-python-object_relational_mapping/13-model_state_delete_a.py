#!/usr/bin/python3
"""Write a script that deletes all State objects with a name containing
the lettera from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from sqlalchemy import select, column
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_be_delected = session.query(State).where(State.name.like('%a%'))
    for state in states_to_be_delected:
        session.delete(state)
    session.commit()
