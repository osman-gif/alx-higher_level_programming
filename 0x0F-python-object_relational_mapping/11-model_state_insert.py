#!/usr/bin/python3
"""Write a script that adds the State object “Louisiana” to
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

    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    states = session.query(State)
    louisiana = session.query(State).where(State.name == 'Louisiana').one()
    print(louisiana.id)
