-- SQL optimization involves improving the performance of SQL queries to make 
-- them run faster and use fewer resources. This can be achieved through various
-- techniques such as indexing, query rewriting, and using appropriate SQL functions.

-- Let's assume we have a large e-commerce database with the following tables:

-- 1. **orders**: Stores order information.
-- 2. **order_items**: Stores items in each order.
-- 3. **products**: Stores product information.
-- 4. **customers**: Stores customer information.

-- Schema Definition

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT,
    price DECIMAL(10, 2)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);


-- Initial Query

-- Let's start with a complex query that retrieves the total sales amount for 
-- each product category, along with the number of orders and the average order 
-- value for each customer.

SELECT
    p.category_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity * oi.price) AS total_sales,
    AVG(o.total_amount) AS avg_order_value
FROM
    orders o
    INNER JOIN order_items oi ON o.order_id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.product_id
    INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY
    p.category_id;


-- To optimize this query, use the following techniques:

-- 1. **Indexing**: Create indexes on columns that are frequently used in joins and where clauses.
-- 2. **Query Rewriting**: Simplify the query to reduce the number of joins and calculations.
-- 3. **Subqueries**: Use subqueries to pre-aggregate data and reduce the amount of data processed in the main query.
