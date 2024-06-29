#!/usr/bin/python3
"""Write a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa

    Your script should take 3 arguments: mysql username, mysql password
    and database name
    You must use the module SQLAlchemy
    The connection to your MySQL server must be to localhost on port 3306
    You must only use one query to the database
    You must use the cities relationship for all State objects
    Results must be sorted in ascending order by states.id and cities.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
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
    states = session.query(State)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        cities = state.cities
        for city in cities:
            print('    {}: {}'.format(city.id, city.name))
