# Write your MySQL query statement below
(SELECT u.name AS results
FROM Users u
LEFT JOIN MovieRating m ON u.user_id = m.user_id
GROUP BY m.user_id
ORDER BY COUNT(m.rating) DESC , u.name ASC
LIMIT 1)
UNION ALL
(SELECT mv.title AS results
FROM Movies mv
JOIN MovieRating mr ON mv.movie_id = mr.movie_id
GROUP BY mv.movie_id
ORDER BY (AVG(CASE WHEN created_at LIKE '2020-02%' THEN mr.rating ELSE NULL END)) DESC, mv.title ASC
LIMIT 1);