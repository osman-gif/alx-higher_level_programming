#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument.
the script name is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    sname = sys.argv[4]

    connect = MySQLdb.connect(
        database=db, user=usr, passwd=pwd, host='localhost', port=3306)
    cursor = connect.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"

    cursor.execute(query, (sname,))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    connect.close()
