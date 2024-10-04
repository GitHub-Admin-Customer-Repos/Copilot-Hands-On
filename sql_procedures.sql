-- Below is an example of a complex SQL stored procedure that performs multiple 
-- operations, including inserting, updating, and deleting records, as well as 
-- handling transactions and error handling.

-- Let's assume we have a database for an e-commerce application with tables for 
-- `orders` and `order_items`. We want to create a stored procedure that processes 
-- an order, including inserting the order and its items, updating inventory, 
-- and handling potential errors.

--Schema:
CREATE TABLE orders (
    order_id INT PRIMARY KEY IDENTITY(1,1),
    customer_id INT,
    order_date DATETIME,
    total_amount DECIMAL
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY IDENTITY(1,1),
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL
);

CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    stock INT
);


-- The stored procedure `process_order` will:
-- 1. Insert a new order.
-- 2. Insert order items.
-- 3. Update inventory.
-- 4. Handle transactions and errors.
