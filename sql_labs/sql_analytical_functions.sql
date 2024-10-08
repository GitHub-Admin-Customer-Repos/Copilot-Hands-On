WITH aggregated_sales AS (
    SELECT
        team_market,
        SUM(sales_amount) AS total_sales
    FROM
        sales
    GROUP BY
        team_market
),
team_info AS (
    SELECT
        tc.market AS team_market,
        tc.color,
        m.mascot
    FROM
        `team-colors` tc
    JOIN
        `mascot` m
    ON
        tc.id = m.id
)
SELECT
    ti.team_market,
    ti.color,
    ti.mascot,
    ag.total_sales,
    RANK() OVER (ORDER BY ag.total_sales DESC) AS sales_rank
FROM
    aggregated_sales ag
JOIN
    team_info ti
ON
    ag.team_market = ti.team_market
ORDER BY
    sales_rank;