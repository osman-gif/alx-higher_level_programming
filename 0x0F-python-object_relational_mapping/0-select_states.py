#!/usr/bin/python3
#Write a script that lists all states from the database hbtn_0e_0_usa
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == '__main__':
	import MySQLdb
	mydb = MySQLdb.connect(host='localhost',
		user=username, password=password,db=database, port=3306)

	cursor = mydb.cursor()

	query_all = 'SELECT * FROM states'

	cursor.execute("""SELECT * FROM states ORDER BY id""")

	states = cursor.fetchall()
	for state in states:
		print(state)

	mydb.commit()
	mydb.close()

