# Write your MySQL query statement below
SELECT em1.name
FROM Employee em1 join Employee em2 
ON em1.id = em2.managerId
GROUP By em1.id
HAVING COUNT( distinct em2.id) >= 5;



