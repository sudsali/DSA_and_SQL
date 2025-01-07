# Write your MySQL query statement below
WITH FirstYear AS (
    SELECT 
        s.product_id, 
        MIN(s.year) AS first_year
    FROM 
        Sales s
    GROUP BY 
        s.product_id
)
SELECT 
    p.product_id, 
    f.first_year, 
    s.quantity, 
    s.price
FROM 
    FirstYear f
JOIN 
    Sales s ON f.product_id = s.product_id AND f.first_year = s.year
JOIN 
    Product p ON s.product_id = p.product_id;