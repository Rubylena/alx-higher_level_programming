-- List all records in second_table with a score >= 10
-- records are ordered in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
