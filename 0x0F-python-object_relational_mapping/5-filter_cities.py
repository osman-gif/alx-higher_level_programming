#!/usr/bin/python3

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state = sys.argv[4]

if __name__ == '__main__':
	import MySQLdb
	mydb = MySQLdb.connect(host='localhost',
		user=username, password=password,db=database, port=3306)

	cursor = mydb.cursor()
	state_cities = 'SELECT * FROM cities INNER JOIN states ON state_id=state.id ORDER BY cities.id'
	
	for state in state_cities:
		print(state)
