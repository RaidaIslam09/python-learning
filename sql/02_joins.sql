-- ================================================
-- SQL Portfolio: JOINs
-- Author: Raida Tasnim Islam
-- ================================================

-- INNER JOIN
-- Returns only employees with valid department assignments
SELECT e.name,
       e.salary,
       e.city,
       d.dept_name,
       d.budget
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id
ORDER BY e.salary DESC;

-- LEFT JOIN
-- Returns ALL employees, NULL where no department match
SELECT e.name,
       e.salary,
       d.dept_name
FROM employees e
LEFT JOIN departments d
    ON e.dept_id = d.dept_id
ORDER BY e.salary DESC;

-- RIGHT JOIN simulation
-- Returns ALL departments including those with no employees
SELECT e.name,
       d.dept_name,
       d.budget,
       d.location
FROM departments d
LEFT JOIN employees e
    ON d.dept_id = e.dept_id
ORDER BY d.dept_name;

-- WHERE filters rows BEFORE grouping
SELECT d.dept_name,
       AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id
WHERE e.city = 'Dallas'
GROUP BY d.dept_name;

-- HAVING filters groups AFTER grouping
SELECT d.dept_name,
       AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING AVG(e.salary) > 80000
ORDER BY avg_salary DESC;