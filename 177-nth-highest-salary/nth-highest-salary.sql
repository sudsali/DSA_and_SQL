CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT salary
        FROM (
            SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS ranked_salary
            FROM Employee
        ) AS cte
        WHERE ranked_salary = N
        LIMIT 1
  );
END