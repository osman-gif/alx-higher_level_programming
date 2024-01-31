--  displays the top 3 of cities temperature during July and August ordered by temperature
SELECT
city,
MAX(value) AS max_temp
FROM
temperatures
WHERE
month IN (7, 8)
GROUP BY
city
ORDER BY
max_temp DESC
LIMIT 3;
