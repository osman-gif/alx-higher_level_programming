#!/usr/bin/python3

""" Write a script that takes in an argument and displays al
l values in the states table ofhbtn_0e_0_usa where name
 matches the argument"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    mydb = MySQLdb.connect('localhost', username, password, database, 3306)
    cursor = mydb.cursor()
    query_db = 'USE hbtn_0e_0_usa'
    query_all = 'SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC'
    cursor.execute(query_all)
    states = cursor.fetchall()
    for state in states:
        print(state)
    mydb.commit()
    cursor.close()
    mydb.close()
