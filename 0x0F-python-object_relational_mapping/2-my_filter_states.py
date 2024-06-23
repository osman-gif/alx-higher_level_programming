#!/usr/bin/python3
#script that lists all states from the database hbtn_0e_0_usa
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
search = sys.argv[4]

if __name__ == '__main__':
	import MySQLdb
	mydb = MySQLdb.connect(host='localhost',
		user=username, password=password,db=database, port=3306)

	cursor = mydb.cursor()

	query_db = 'USE hbtn_0e_0_usa'
	query_all = 'SELECT id, name FROM states WHERE name=search ORDER BY states.id'

	cursor.execute(query_db)
	states = cursor.execute(query_all)
	for state in states:
		print(state)

	mydb.commit()
	cursor.close()
	mydb.close()

