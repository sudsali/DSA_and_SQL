# Write your MySQL query statement below
SELECT project_id , ROUND(SUM(em.experience_years)/COUNT(em.employee_id),2) as average_years
FROM Project p
JOIN Employee em
ON p.employee_id = em.employee_id
GROUP BY project_id;