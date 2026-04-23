-- =============================================
-- SQL Portfolio : Aggregations
-- Author: Raida Islam
-- =============================================

-- Full Department Summary
SELECT department,
       COUNT(*)     AS  total_employees,
       SUM(salary)  AS total_salary_cost,
       AVG(average) AS avg_salary,
       MAX(salary)  AS highest_salary,
       MIN(salary)  AS lowerst_salary 
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- Employees per city
SELECT city,
       COUNT(id) AS total_employees
FROM employees
GROUP BY city
ORDER BY total_employees DESC;

-- Departments with total salary above 200000
SELECT department,
       SUM(salary) AS total_salary_cost
FROM employees
GROUP BY department
HAVING SUM(salary) > 200000
ORDER BY total_salary_cost DESC;

-- COUNT DISTINCT example
SELECT COUNT(DISTINCT city) AS unique_cities
FROM employees;

-- Aggregations with JOIN
SELECT d.dept_name,
       d.budget,
       COUNT(e.id)   AS total_employees,
       AVG(e.salary) AS avg_salary,
       SUM(e.salary) AS total_salary_cost
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name, d.budget
ORDER BY avg_salary DESC;
