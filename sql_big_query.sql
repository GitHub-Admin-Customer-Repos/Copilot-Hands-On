-- Here's an example of a SQL query that involves multiple tables, joins, subqueries, and aggregate functions. This query is designed to retrieve detailed sales information from a hypothetical e-commerce database.

-- Schema:
-- `customers` Table

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO customers (customer_id, customer_name, email) VALUES
(1, 'John Doe', 'john.doe@example.com'),
(2, 'Jane Smith', 'jane.smith@example.com'),
(3, 'Alice Johnson', 'alice.johnson@example.com');

-- `orders` Table

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(101, 1, '2023-01-15'),
(102, 2, '2023-02-20'),
(103, 1, '2023-03-05'),
(104, 3, '2023-04-10');

-- `order_details` Table

CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_details (order_detail_id, order_id, product_id, quantity, unit_price) VALUES
(1001, 101, 201, 2, 50.00),
(1002, 101, 202, 1, 30.00),
(1003, 102, 203, 3, 20.00),
(1004, 103, 201, 1, 50.00),
(1005, 104, 204, 5, 10.00);

-- `products` Table

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

INSERT INTO products (product_id, product_name, price) VALUES
(201, 'Product A', 50.00),
(202, 'Product B', 30.00),
(203, 'Product C', 20.00),
(204, 'Product D', 10.00);

-- Create a SQL Query to retrieve detailed sales information from a the above e-commerce database.

SELECT
    c.customer_id,
    c.customer_name,
    c.email,
    o.order_id,
    o.order_date,
    p.product_id,
    p.product_name,
    od.quantity,
    od.unit_price,
    (od.quantity * od.unit_price) AS total_price,
    (SELECT SUM(od2.quantity * od2.unit_price)
    FROM order_details od2
    WHERE od2.order_id = o.order_id) AS order_total,
    (SELECT COUNT(*)
    FROM orders o2
    WHERE o2.customer_id = c.customer_id) AS total_orders,
    (SELECT SUM(od3.quantity * od3.unit_price)
    FROM orders o3
    JOIN order_details od3 ON o3.order_id = od3.order_id
    WHERE o3.customer_id = c.customer_id) AS total_spent
    FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    order_details od ON o.order_id = od.order_id
JOIN
    products p ON od.product_id = p.product_id
WHERE
    o.order_date BETWEEN '2023-01-01' AND '2023-12-31'
ORDER BY
    c.customer_id, o.order_date;

-- Use Copilot to explain and document what is happening in each clause of the query.
-- 1. **SELECT Clause**: 
    -- Retrieves customer details (`customer_id`, `customer_name`, `email`).
    -- Retrieves order details (`order_id`, `order_date`).
    -- Retrieves product details (`product_id`, `product_name`).
    -- Calculates the total price for each order line (`quantity * unit_price`).
    -- Uses subqueries to calculate the total order amount, total number of orders for the customer, and total amount spent by the customer.

-- 2. **FROM Clause**: 
    -- Joins the `customers`, `orders`, `order_details`, and `products` tables.

-- 3. **WHERE Clause**: 
    -- Filters orders to include only those placed within the year 2023.

-- 4. **ORDER BY Clause**: 
    -- Orders the results by `customer_id` and `order_date`.

