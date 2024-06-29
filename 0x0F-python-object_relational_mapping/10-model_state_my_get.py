#!/usr/bin/python3
"""Write a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from sqlalchemy import select, column
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    s_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).where(State.name == s_name).first()
    if state:
        print('{}'.format(state.id))
    else:
        print("Not found")
