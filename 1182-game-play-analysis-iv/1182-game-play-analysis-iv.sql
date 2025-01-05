# Write your MySQL query statement below
WITH Firstlogin AS (
    SELECT player_id, MIN(event_date) as first_login
    FROM Activity
    GROUP BY player_id
),
Secondlogin AS(
    SELECT a.player_id
    FROM Activity a
    JOIN Firstlogin b ON a.player_id = b.player_id
    WHERE DATEDIFF(a.event_date, b.first_login) = 1
)
SELECT ROUND(COUNT(DISTINCT Secondlogin.player_id) /  (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS Fraction
FROM Secondlogin;
