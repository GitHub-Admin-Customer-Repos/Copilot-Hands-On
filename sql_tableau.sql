-- Building code optimized for Tableau involves several best practices to ensure 
-- that your data sources, calculations, and visualizations perform efficiently.

-- Use Copilot to detail how to optimize queries for Tableau
-- 1. Optimize Data Sources

-- **Use Extracts**: Use Tableau Data Extracts (TDE) instead of live connections for faster performance. Extracts are optimized for Tableau's in-memory data engine.
-- **Filter Data**: Reduce the amount of data by applying filters at the data source level. Only bring in the data you need.
-- **Aggregate Data**: Aggregate data at the data source level to reduce the volume of data Tableau needs to process.
-- **Use Efficient Data Types**: Ensure that data types are correctly defined and optimized for performance.

-- 2. Optimize Calculations

-- **Use Context Filters**: Context filters can improve performance by reducing the number of records Tableau needs to process.
-- **Minimize Calculated Fields**: Perform calculations at the data source level whenever possible. Calculated fields in Tableau can be slower.
-- **Avoid Row-Level Calculations**: Use aggregate calculations instead of row-level calculations to improve performance.

-- 3. Optimize Visualizations

-- **Limit Marks**: Reduce the number of marks in your visualizations. Too many marks can slow down rendering.
-- **Use Efficient Charts**: Some chart types are more efficient than others. For example, bar charts and line charts are generally faster than scatter plots with many points.
-- **Optimize Dashboards**: Limit the number of visualizations on a single dashboard. Use actions and filters to switch between views instead of displaying everything at once.

-- 4. Optimize Queries

-- **Use Indexes**: Ensure that your database tables have appropriate indexes to speed up query performance.
-- **Optimize SQL**: Write efficient SQL queries. Avoid complex joins and subqueries if possible.
-- **Use Materialized Views**: Consider using materialized views in your database to precompute and store complex queries.


-- Original Query

SELECT
    orders.order_id,
    orders.order_date,
    customers.customer_name,
    products.product_name,
    order_details.quantity,
    order_details.unit_price,
    (order_details.quantity * order_details.unit_price) AS total_price
FROM
    orders
JOIN
    customers ON orders.customer_id = customers.customer_id
JOIN
    order_details ON orders.order_id = order_details.order_id
JOIN
    products ON order_details.product_id = products.product_id
WHERE
    orders.order_date BETWEEN '2023-01-01' AND '2023-12-31';


-- Optimize the above Query

-- 1. **Filter Data**: Apply filters to reduce the data volume.
-- 2. **Aggregate Data**: Aggregate data at the source to reduce the number of rows.

SELECT
    orders.order_id,
    orders.order_date,
    customers.customer_name,
    products.product_name,
    SUM(order_details.quantity) AS total_quantity,
    AVG(order_details.unit_price) AS avg_unit_price,
    SUM(order_details.quantity * order_details.unit_price) AS total_price
FROM
    orders
JOIN
    customers ON orders.customer_id = customers.customer_id
JOIN
    order_details ON orders.order_id = order_details.order_id
JOIN
    products ON order_details.product_id = products.product_id
WHERE
    orders.order_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY
    orders.order_id,
    orders.order_date,
    customers.customer_name,
    products.product_name;

-- Explanation

-- **Filter Data**: The `WHERE` clause filters the data to only include orders from 2023.
-- **Aggregate Data**: The `GROUP BY` clause aggregates the data by order, customer, and product, reducing the number of rows Tableau needs to process.
