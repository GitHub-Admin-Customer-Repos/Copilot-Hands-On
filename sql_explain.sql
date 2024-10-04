-- Below is an example of a complex SQL statement that involves multiple joins, 
-- subqueries, Common Table Expressions (CTEs), window functions, and analytical
-- functions. This query is designed to analyze sales data, calculate various 
-- metrics, and rank products based on their performance.

-- Let's assume we have the following tables:

-- 1. **sales**: Stores sales transactions.
-- 2. **products**: Stores product information.
-- 3. **customers**: Stores customer information.
-- 4. **categories**: Stores product category information.
-- 5. **regions**: Stores sales region information.

-- Schema Definition

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    sale_date DATE,
    sale_amount DECIMAL(10, 2),
    region_id INT
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

CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE regions (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(100)
);


-- The following SQL statement calculates various metrics such as total sales, average sales, and ranks products based on their total sales within each category and region.

WITH SalesData AS (
    SELECT
        s.sale_id,
        s.product_id,
        s.customer_id,
        s.sale_date,
        s.sale_amount,
        s.region_id,
        p.product_name,
        p.category_id,
        p.price,
        c.customer_name,
        c.email,
        cat.category_name,
        r.region_name
    FROM
        sales s
        INNER JOIN products p ON s.product_id = p.product_id
        INNER JOIN customers c ON s.customer_id = c.customer_id
        INNER JOIN categories cat ON p.category_id = cat.category_id
        INNER JOIN regions r ON s.region_id = r.region_id
),
AggregatedSales AS (
    SELECT
        sd.product_id,
        sd.category_id,
        sd.region_id,
        SUM(sd.sale_amount) AS total_sales,
        AVG(sd.sale_amount) AS avg_sales,
        COUNT(sd.sale_id) AS total_transactions
    FROM
        SalesData sd
    GROUP BY
        sd.product_id, sd.category_id, sd.region_id
),
RankedProducts AS (
    SELECT
        asd.product_id,
        asd.category_id,
        asd.region_id,
        asd.total_sales,
        asd.avg_sales,
        asd.total_transactions,
        RANK() OVER (PARTITION BY asd.category_id, asd.region_id ORDER BY asd.total_sales DESC) AS sales_rank
    FROM
        AggregatedSales asd
)
SELECT
    rp.product_id,
    p.product_name,
    rp.category_id,
    cat.category_name,
    rp.region_id,
    r.region_name,
    rp.total_sales,
    rp.avg_sales,
    rp.total_transactions,
    rp.sales_rank
FROM
    RankedProducts rp
    INNER JOIN products p ON rp.product_id = p.product_id
    INNER JOIN categories cat ON rp.category_id = cat.category_id
    INNER JOIN regions r ON rp.region_id = r.region_id
ORDER BY
    rp.category_id, rp.region_id, rp.sales_rank;

-- Explain:

-- 1. **SalesData CTE**:
-- Joins the `sales`, `products`, `customers`, `categories`, and `regions` tables to create a comprehensive dataset with all relevant information.

-- 2. **AggregatedSales CTE**:
-- Aggregates the sales data to calculate total sales, average sales, and total transactions for each product within each category and region.

-- 3. **RankedProducts CTE**:
-- Ranks the products based on their total sales within each category and region using the `RANK()` window function.

-- 4. **Final SELECT Statement**:
-- Joins the `RankedProducts` CTE with the `products`, `categories`, and `regions` tables to retrieve the product names, category names, and region names.
-- Orders the results by category, region, and sales rank.

-- Document the SQL statement with comments to explain the purpose of each part of the query and how the different parts are connected.