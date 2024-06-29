#!/usr/bin/python3
"""Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py:

    City class:
        No change
    State class:
        In addition to previous requirements, the class attribute cities
        must represent a relationship with the class City. If the State object
        is deleted, all linked City objects must be automatically deleted.
        Also, the reference from a City object to his State should be named
        state
    You must use the module SQLAlchemy
"""

if __name__ == '__main__':
    from sqlalchemy import select, column
    from relationship_state import Base, State
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities = [san_francisco]
    session.add(california)
    session.commit()
