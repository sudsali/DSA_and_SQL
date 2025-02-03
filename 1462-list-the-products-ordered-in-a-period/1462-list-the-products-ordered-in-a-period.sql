# Write your MySQL query statement below
    SELECT p.product_name, SUM(o.unit) AS unit
    FROM Products p 
    JOIN Orders o ON p.product_id = o.product_id
    WHERE o.order_date LIKE '2020-02%'
    GROUP BY product_name
    HAVING SUM(o.unit) >= 100;