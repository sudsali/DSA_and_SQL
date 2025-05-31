# Write your MySQL query statement below
WITH cte AS (
    SELECT num AS current_num,
    LAG(num,1) OVER (ORDER BY id) AS prev_num1,
    LAG(num,2) OVER (ORDER BY id) AS prev_num2,
    LEAD(num,1) OVER (ORDER BY id) AS next_num1,
    LEAD(num,2) OVER (ORDER BY id) AS next_num2
    FROM Logs
)
SELECT DISTINCT(current_num) AS ConsecutiveNums
FROM cte
WHERE (current_num = prev_num1 AND current_num = prev_num2) OR (current_num = next_num1 AND current_num = next_num2);