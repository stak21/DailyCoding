# SQL statement to select rows where the countries poplation
# is greater than 3m or area is > 3m km
SELECT name, population, area FROM World
WHERE population > 25000000 OR area > 30000000;

# Using Union can be faster when searching multiple columns
SELECT name, population, area FROM World
WHERE population > 25000000 

UNION

SELECT name, population, area FROM World
WHERE area > 30000000;



