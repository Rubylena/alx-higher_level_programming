-- list all cities in the database hbtn-od_usa
-- Records are sorted by cities.id
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN state AS s
	ON c.state_id = s.id
ORDER BY c.id;
