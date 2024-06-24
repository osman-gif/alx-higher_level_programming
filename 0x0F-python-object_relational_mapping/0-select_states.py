#!/usr/bin/python3

"""Write a script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    un = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    mydb = MySQLdb.connect('localhost', un, pwd, db, 3306)
    cursor = mydb.cursor()
    query_all = 'SELECT * FROM states'
    cursor.execute("""SELECT * FROM states ORDER BY id""")
    states = cursor.fetchall()
    for state in states:
        print(state)
    mydb.commit()
    mydb.close()
