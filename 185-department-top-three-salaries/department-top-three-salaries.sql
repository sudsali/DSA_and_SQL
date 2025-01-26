# Write your MySQL query statement below
WITH ranked_tab AS (
    SELECT e.name,e.salary, d.name as DepartmentName, DENSE_RANK() OVER (PARTITION BY e.departmentId  ORDER BY e.departmentId ASC ,salary DESC) AS ranking
    FROM Employee e
    LEFT JOIN Department d ON e.departmentId= d.id 
    ORDER BY e.departmentId ASC,salary DESC
)
SELECT DepartmentName AS Department, name AS Employee, salary AS Salary
FROM ranked_tab
WHERE ranking < 4
ORDER BY Department ASC, Salary DESC;