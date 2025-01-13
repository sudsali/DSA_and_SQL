# Write your MySQL query statement below
WITH l AS
(
    SELECT num,
    LAG(num,1) OVER (ORDER BY id) AS prev_num,
    LAG(num,2) OVER (ORDER BY id) AS prev_num2,
    LEAD(num,1) OVER (ORDER BY id) AS next_num,
    LEAD (num,2) OVER (ORDER BY id) AS next_num2
    FROM Logs
)
SELECT DISTINCT(num) AS ConsecutiveNums
FROM l
WHERE (num = prev_num AND num = prev_num2) OR (num = next_num AND num=next_num2);