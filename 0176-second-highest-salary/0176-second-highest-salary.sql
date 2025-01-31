# Write your MySQL query statement below
WITH cte AS (
    SELECT salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as ranked
    FROM Employee
)
SELECT MAX(CASE WHEN ranked = 2 THEN salary ELSE NULL END) AS SecondHighestSalary
FROM cte;
