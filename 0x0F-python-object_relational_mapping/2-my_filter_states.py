#!/usr/bin/python3
"""This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == '__main__':
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    mydb = MySQLdb.connect('localhost', username, password, database, 3306)
    cursor = mydb.cursor()
    q = """SELECT * FROM states WHERE BINARY name="{}"
    ORDER BY states.id ASC""".format(search)
    cursor.execute(q)
    states = cursor.fetchall()
    for state in states:
        print(state)
    mydb.commit()
    cursor.close()
    mydb.close()
