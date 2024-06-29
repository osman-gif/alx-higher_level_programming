#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py that
contains the class definition of a City"""

if __name__ == '__main__':
    from sqlalchemy import select, column
    from model_state import Base, State
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    cities = session.query(City).order_by(text('cities.id'))

    for state in states:
        for city in cities:
            if state.id == city.state_id:
                print('{}: ({}) {}'.format(state.name, city.id, city.name))
