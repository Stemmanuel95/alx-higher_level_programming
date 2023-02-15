-- Listing all records with a score in the table specified
-- Results should have both score and name in the order score,name

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
