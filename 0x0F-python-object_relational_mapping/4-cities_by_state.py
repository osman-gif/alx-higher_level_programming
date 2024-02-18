#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    query = "SELECT cities.id, cities.name,\
        states.name FROM cities JOIN states \
            ON state_id = states.id  ORDER BY cities.id"

    connect = MySQLdb.connect(user=usr, passwd=pwd, database=db)
    cur = connect.cursor()
    cur.execute(query)
    cities = cur.fetchall()

    for city in cities:
        print(city)
