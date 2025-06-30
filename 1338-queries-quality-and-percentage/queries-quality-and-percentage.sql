# Write your MySQL query statement below
SELECT q.query_name, ROUND(SUM(q.rating/q.position) / COUNT(q.query_name),2) AS quality, ROUND((SUM(rating<3)/ COUNT(rating)) * 100,2) AS poor_query_percentage
FROM Queries q
GROUP BY q.query_name