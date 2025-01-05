# Write your MySQL query statement below
WITH FirstLogin AS (
    SELECT player_id , MIN(event_date) as first_login
    FROM Activity
    GROUP BY player_id
),
SecondLogin AS (
    SELECT a.player_id
    FROM Activity a
    JOIN FirstLogin b ON a.player_id = b.player_id
    WHERE DATEDIFF(a.event_date, b.first_login) = 1
)
SELECT ROUND(COUNT(DISTINCT SecondLogin.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM SecondLogin;
