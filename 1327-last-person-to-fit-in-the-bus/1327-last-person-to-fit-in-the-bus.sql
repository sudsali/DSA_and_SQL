# Write your MySQL query statement below
WITH Ranking AS (
    SELECT DISTINCT person_name, turn
    FROM (
        SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS total, turn
        FROM Queue
    ) temp
    WHERE total <= 1000
)
SELECT person_name
FROM Ranking
WHERE turn = (
    SELECT MAX(turn)
    FROM Ranking
);