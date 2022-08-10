-- display the top 3 cities with the highest temperature
-- between july and august ordered by temp.
SELECT CITY, AVG(value) AS average_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY average_temp
LIMIT 3;
