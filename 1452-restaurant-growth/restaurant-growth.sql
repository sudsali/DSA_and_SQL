# Write your MySQL query statement below
WITH daily AS (
    SELECT visited_on, SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY 1
)
SELECT visited_on, SUM(daily_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
ROUND(AVG(daily_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
FROM daily
LIMIT 1000 OFFSET 6;
