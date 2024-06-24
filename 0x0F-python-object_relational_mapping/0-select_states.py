#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
import sys

un = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]

if __name__ == '__main__':
    import MySQLdb
    mydb = MySQLdb.
    connect(host='localhost', user=un, password=pwd, db=db, port=3306)

    cursor = mydb.cursor()

    query_all = 'SELECT * FROM states'

    cursor.execute("""SELECT * FROM states ORDER BY id""")

    states = cursor.fetchall()
    for state in states:
        print(state)

    mydb.commit()
    mydb.close()
