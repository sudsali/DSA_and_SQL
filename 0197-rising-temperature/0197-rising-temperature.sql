# Write your MySQL query statement below
SELECT w2.id FROM Weather AS w1 JOIN Weather AS w2
 where datediff(w2.recordDate,w1.recordDate) = 1
 and w1.recordDate < w2.recordDate
 and w1.temperature < w2.temperature