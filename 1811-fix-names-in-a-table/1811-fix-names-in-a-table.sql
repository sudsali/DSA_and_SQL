# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(substr(name,1,1)),LOWER(substr(name,2,LENGTH(name)))) AS name
FROM Users
ORDER BY user_id;