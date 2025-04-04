# Write your MySQL query statement below
WITH single AS (
    SELECT employee_id, department_id 
    FROM Employee
    GROUP BY employee_id 
    HAVING COUNT(department_id) = 1
)
SELECT DISTINCT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' 
UNION 
SELECT * FROM single;