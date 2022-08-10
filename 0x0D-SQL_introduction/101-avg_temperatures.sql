-- display the average temperature by city ordered by descending temperature
SELECT city, AVG(value) AS average_temp
FROM temperatures
GROUP BY city
ORDER BY average_temp DESC
