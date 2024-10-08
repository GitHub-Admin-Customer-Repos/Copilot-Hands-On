# GitHub Copilot SQL Analytical Functions

We will be using a public data set in BigQuery as our data source.

[BigQuery – NCAA Basketball – Google Cloud console](https://console.cloud.google.com/bigquery(cameo:product/ncaa-bb-public/ncaa-basketball))

# Directions
Create an analytical SQL query that combines data from multiple tables to perform an analysis. Let's assume we want to analyze the total sales amount for each team, broken down by the mascot and the color of the team, and rank the teams based on their total sales amount.
- Aggregate the total sales amount for each team.
- Combine team colors and mascots information.
- Join the aggregated sales data with the team information.
- Rank the teams based on their total sales amount using the RANK() function.

Example output:
| team_market | color | mascot | total_sales | sales_rank
|--|--|--|--|--|
| Wildcats | Blue | Wildcat | 150000 | 1 |
| Tigers| Orange| Tiger| 120000| 2 |
| Bulldogs | Red | Bulldog| 110000 | 3 |
| Bears| Green | Bear | 90000 | 4 |