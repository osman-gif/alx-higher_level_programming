-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
SELECT score, name FROM second_table GROUP BY score, name ORDER BY score DESC;

