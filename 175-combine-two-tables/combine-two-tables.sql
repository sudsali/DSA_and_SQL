# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Address t1
RIGHT JOIN Person t2 ON t1.personId = t2.personId;