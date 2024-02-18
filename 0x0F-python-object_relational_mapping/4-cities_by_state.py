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

    query = "SELECT * FROM cities ORDER BY id"

    connect = MySQLdb.connect(user=usr, passwd=pwd, database=db)
    cur = connect.cursor()
    cur.execute(query)
    cities = cur.fetchall()

    for city in cities:
        print(city)
