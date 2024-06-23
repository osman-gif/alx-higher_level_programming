#!/usr/bin/python3
#Write a script that takes in an argument and displays all values in the states table of
#hbtn_0e_0_usa where name matches the argument
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == '__main__':
	import MySQLdb
	mydb = MySQLdb.connect(host='localhost',
		user=username, password=password,db=database, port=3306)

	cursor = mydb.cursor()

	query_db = 'USE hbtn_0e_0_usa'
	query_all = 'SELECT * FROM states ORDER BY states.id HAVING "N"'

	cursor.execute(query_db)
	states = cursor.execute(query_all)
	for state in states:
		print(state)

	mydb.commit()
	cursor.close()
	mydb.close()

