# Write your MySQL query statement below
SELECT s.user_id,
ROUND(AVG(CASE 
        WHEN c.action IS NULL THEN 0
        WHEN c.action = 'timeout' THEN 0
        ELSE 1
    END),2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON c.user_id = s.user_id
GROUP BY user_id;