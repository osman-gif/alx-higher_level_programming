-- cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT name
FROM cities
WHERE state_id = (SELECT state_id
	FROM states
	WHERE name = california
)
ORDER BY cities.id ASC;
