# Write your MySQL query statement below
SELECT query_name, 
ROUND(SUM(rating/position)/COUNT(rating),2) as quality,
ROUND(SUM(rating<3)/COUNT(*) * 100,2) as poor_query_percentage
FROM Queries
WHERE query_name IS NOT null
GROUP BY query_name;