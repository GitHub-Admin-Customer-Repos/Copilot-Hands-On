# GitHub Copilot SQL Procedures

# We will be using a public data set in BigQuery as our data source.

#[BigQuery – NCAA Basketball – Google Cloud console](https://console.cloud.google.com/bigquery(cameo:product/ncaa-bb-public/ncaa-basketball))


# Directions
# Use Copilot to explain what each part of the query below is doing.
# game_results
# team_performance
# team_info
# team_colors
# combined_data

# What does the query as a whole do?

# Add comments to the query to explain what each part is doing.


WITH game_results AS (
    SELECT 
        p.team_market,
        g.game_id,
        g.season,
        g.status,
        g.attendance,
        CASE 
            WHEN g.status = 'won' THEN 1
            ELSE 0
        END AS win,
        p.points_scored
    FROM 
        players p
    JOIN 
        games g ON p.game_id = g.game_id
),
team_performance AS (
    SELECT 
        gr.team_market,
        COUNT(gr.game_id) AS total_games,
        SUM(gr.win) AS total_wins,
        AVG(gr.points_scored) AS avg_points_scored,
        AVG(gr.attendance) AS avg_attendance
    FROM 
        game_results gr
    GROUP BY 
        gr.team_market
),
team_info AS (
    SELECT 
        t.market,
        t.color,
        m.mascot
    FROM 
        team_colors t
    JOIN 
        mascot m ON t.market = m.market
),
combined_data AS (
    SELECT 
        tp.team_market,
        tp.total_games,
        tp.total_wins,
        tp.avg_points_scored,
        tp.avg_attendance,
        ti.color,
        ti.mascot
    FROM 
        team_performance tp
    JOIN 
        team_info ti ON tp.team_market = ti.market
)
SELECT 
    team_market,
    color,
    mascot,
    total_games,
    total_wins,
    avg_points_scored,
    avg_attendance
FROM 
    combined_data
ORDER BY 
    total_wins DESC, avg_points_scored DESC;