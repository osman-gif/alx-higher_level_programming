#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_0_usa"""
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == '__main__':
    import MySQLdb
    mydb = MySQLdb.connect('localhost', username, password, database, 3306)

    cursor = mydb.cursor()

    query_all = """SELECT c.id, c.name, s.name
    FROM cities as c INNER JOIN states as s
    ON s.id = c.state_id ORDER BY c.id ASC"""

    cursor.execute(query_all)
    states = cursor.fetchall()
    for state in states:
        print(state)

    mydb.commit()
    mydb.close()
