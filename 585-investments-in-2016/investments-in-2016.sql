# Write your MySQL query statement below
WITH inv_val AS (
    SELECT pid, tiv_2015, tiv_2016
    FROM Insurance
    WHERE tiv_2015 IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) > 1
    )
),
coordinates AS (
    SELECT pid, CONCAT(lat,lon)
    FROM Insurance
    WHERE CONCAT(lat,lon) NOT IN (
        SELECT CONCAT(lat,lon)
        FROM Insurance
        GROUP BY CONCAT(lat,lon)
        HAVING COUNT(*) > 1
    )   
)
SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM inv_val i
JOIN coordinates c ON i.pid = c.pid;