-- Let's assume we have the following tables:

-- 1. **customers**: Stores customer information.
-- 2. **orders**: Stores order information.
-- 3. **order_items**: Stores items in each order.
-- 4. **products**: Stores product information.

-- Schema Definition

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Sample Data

INSERT INTO customers (customer_id, customer_name) VALUES
(1, 'Alice'),
(2, 'Bob');

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 1, '2023-01-01'),
(2, 2, '2023-01-02');

INSERT INTO order_items (order_item_id, order_id, product_id, quantity) VALUES
(1, 1, 101, 2),
(2, 1, 102, 1),
(3, 2, 101, 1);

INSERT INTO products (product_id, product_name, price) VALUES
(101, 'Product A', 10.00),
(102, 'Product B', 20.00);


-- The following query should retrieve detailed order information, including
-- customer names, product names, quantities, and total prices for each order
-- item. It uses multiple joins to combine data from all four tables.
