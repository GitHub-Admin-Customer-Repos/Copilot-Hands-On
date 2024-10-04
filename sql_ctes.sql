-- Common Table Expressions (CTEs) are a powerful feature in SQL that allow you 
-- to define temporary result sets that can be referenced within a `SELECT`, 
-- `INSERT`, `UPDATE`, or `DELETE` statement. CTEs can be particularly useful 
-- for breaking down complex queries into more manageable parts.


-- Let's assume we have the following tables:

-- 1. **employees**: Stores employee information.
-- 2. **departments**: Stores department information.
-- 3. **salaries**: Stores salary information for employees.

-- Schema Definition

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE salaries (
    employee_id INT,
    salary DECIMAL(10, 2),
    salary_date DATE,
    PRIMARY KEY (employee_id, salary_date)
);

-- Sample Data

INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(1, 'Alice', 1),
(2, 'Bob', 2),
(3, 'Charlie', 1),
(4, 'David', 3);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Marketing');

INSERT INTO salaries (employee_id, salary, salary_date) VALUES
(1, 50000, '2023-01-01'),
(2, 60000, '2023-01-01'),
(3, 55000, '2023-01-01'),
(4, 45000, '2023-01-01'),
(1, 52000, '2023-07-01'),
(2, 62000, '2023-07-01'),
(3, 57000, '2023-07-01'),
(4, 47000, '2023-07-01');

-- Task:
-- The following query should use multiple CTEs to calculate the average salary per
-- department and then find the departments with an average salary above a certain threshold.