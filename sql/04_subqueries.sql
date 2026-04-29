-- ========================================
-- SQL PORTFOLIO: Subqueries
-- Author: Raida Islam
-- =======================================

-- Subquery 1: Above average earners
-- INNER Query calculate average first
-- OUTER Query filters using that result
SELECT name,
       department,
       salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- Subquery 2: Highest paid employee
-- INNER query finds maximum salary
-- OUTER query returns with the matching employee
SELECT name,
       department,
       salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees)
ORDER BY salary DESC;

-- Subquery 3: Department average above 80000
-- Inner query creates temporary department summary
-- Outer query filters that summary
SELECT dept_summary.department,
       dept_summary.avg_salary
FROM (
    SELECT department,
           AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department       
) AS dept_summary
WHERE dept_summary.avg_salary >80000;
  