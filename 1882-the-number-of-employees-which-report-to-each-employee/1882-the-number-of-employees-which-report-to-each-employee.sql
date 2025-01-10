# Write your MySQL query statement below
WITH manager AS (
    SELECT name, reports_to AS manager_id, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)
SELECT DISTINCT e.employee_id, e.name, m.reports_count, m.average_age
FROM Employees e, manager m
WHERE e.employee_id = m.manager_id
ORDER BY employee_id;