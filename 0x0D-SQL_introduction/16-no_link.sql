-- Script lists all records of the table specified from the database
-- Doesn't list rows without a name value
-- Results displays the score and the name 

SELECT score, name 
FROM second_table
WHERE name IS NOT NULL 
AND name !=''
ORDER BY score DESC;
