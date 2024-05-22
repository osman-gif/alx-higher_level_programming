-- lists all cities contained in the database hbtn_0d_usa.
SELECT city.id, city.name, state.name 
FROM cities city
INNER JOIN states state
ON city.state_id= state.id
ORDER BY city.id ASC;
