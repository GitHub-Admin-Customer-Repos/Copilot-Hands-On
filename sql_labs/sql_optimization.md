# GitHub Copilot SQL Optimization

-- SQL optimization involves improving the performance of SQL queries to make them run faster and use fewer resources. This can be achieved through various techniques such as indexing, query rewriting, and using appropriate SQL functions.

# Directions

-- Initial Query

-- Let's start with a complex query that retrieves the total sales amount for 
-- each product category, along with the number of orders and the average order 
-- value for each customer.

```
SELECT 
    p.first_name,
    p.last_name,
    p.team_name,
    p.team_market,
    t.color,
    m.mascot,
    g.scheduled_date,
    g.gametime
FROM 
    players p
JOIN 
    team_colors t ON p.team_market = t.market
JOIN 
    mascot m ON p.team_market = m.market
JOIN 
    games g ON p.game_id = g.game_id
WHERE 
    g.season = 2022;
```

-- To optimize this query, use Copilot to understand best practices for SQL query optimization, and apply them to the query above.

-- 1. **Indexing**: Create indexes on columns that are frequently used in joins and where clauses.
-- 2. **Filtering** Filtering the data before performing the joins reduces the size of the intermediate result sets, making the joins more efficient.
-- 3. **Efficient Joins**: Ensuring that the joins are performed on indexed columns helps the database engine to quickly locate the matching rows.