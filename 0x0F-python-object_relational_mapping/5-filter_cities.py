#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa"""
 
if __name__ == '__main__':
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    mydb = MySQLdb.connect('localhost', username, password, database, 3306)

    cursor = mydb.cursor()
    state_cities = """SELECT c.name FROM cities as c INNER JOIN states
    as s ON state_id=s.id WHERE s.name="{}" ORDER BY c.id ASC""".format(state)
    cursor.execute(state_cities)
    cities = cursor.fetchall()
    for i in range(len(cities)):
        if i == len(cities) - 1:
            print(cities[i][0])
        else:
            print(cities[i][0], end=", ")
