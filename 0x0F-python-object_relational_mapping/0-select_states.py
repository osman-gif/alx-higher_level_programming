#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa

import sys
import MySQLdb

if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    connect = MySQLdb.connect(
        database=db, user=usr, passwd=pwd, host='localhost', port=3306)
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id')

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    connect.close()
