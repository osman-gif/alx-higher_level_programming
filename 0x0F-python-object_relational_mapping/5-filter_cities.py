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
    state_name = sys.argv[4]

    query = "SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states \
            ON state_id = states.id \
            WHERE states.name = %s\
            ORDER BY cities.id"

    connect = MySQLdb.connect(user=usr, passwd=pwd, database=db)
    cur = connect.cursor()
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    strr = ''
    for i in range(0, len(cities)):
        if i+1 != len(cities):
            print(cities[i][1], end=", ")
        else:
            print(cities[i][1])
