-- Script that lists the number of records with same score from the table

SELECT score, COUNT(*) AS number FROM second_table
ORDER BY number DESC;

