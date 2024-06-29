#!/usr/bin/python3
"""Write a script that prints the first State object from
the database hbtn_0e_6_usa"""

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
    state = session.query(State).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")
