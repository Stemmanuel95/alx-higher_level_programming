-- Script displays the maximum temperatures of each state 
-- arranged by the by State name

SELECT state, MAX(value) as max_temp 
FROM temperatures 
GROUP BY state 
ORDER BY state;
