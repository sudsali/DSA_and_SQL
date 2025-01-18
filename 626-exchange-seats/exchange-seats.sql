# Write your MySQL query statement below
WITH even AS (
    SELECT id, student, LAG(student) OVER (ORDER BY id) AS prev_name, LEAD(student) OVER (ORDER BY id) AS next_name
    FROM Seat
)
SELECT id, 
CASE 
    WHEN id % 2 = 0 THEN prev_name
    WHEN id % 2 = 1 AND next_name IS NOT NULL THEN next_name 
    ELSE student
END AS student
FROM even;