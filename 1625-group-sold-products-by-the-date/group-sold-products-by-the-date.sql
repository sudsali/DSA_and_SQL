# Write your MySQL query statement below
WITH Products AS (
    SELECT sell_date, GROUP_CONCAT(DISTINCT product ORDER BY product) as grouped_prod
    FROM Activities
    GROUP BY sell_date
)
SELECT a. sell_date, COUNT(DISTINCT a.product) AS num_sold, p.grouped_prod AS products
FROM Activities a
JOIN Products p ON p.sell_date = a.sell_date
GROUP BY sell_date;
