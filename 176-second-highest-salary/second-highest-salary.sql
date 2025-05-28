# Write your MySQL query statement below
WITH cte AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as ranked_salary
    FROM Employee
)
SELECT MAX(CASE WHEN ranked_salary = 2 THEN salary ELSE NULL END) AS SecondHighestSalary
FROM cte;