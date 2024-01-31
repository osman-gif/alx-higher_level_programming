-- displays the max temperature of each state (ordered by State name).
SELECT
city,
MAX(value) AS max_temperature
FROM
temperatures
WHERE
month IN (7, 8)
GROUP BY
city
ORDER BY
max_temperature DESC
LIMIT 3;

