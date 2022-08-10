-- list all records of the second_table in descending order
-- do not list rows without a name value
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
