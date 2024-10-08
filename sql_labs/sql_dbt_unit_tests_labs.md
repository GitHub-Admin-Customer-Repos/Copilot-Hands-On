# GitHub Copilot SQL DBT Unit Tests

We will be using a public data set in BigQuery as our data source.

[BigQuery – NCAA Basketball – Google Cloud console](https://console.cloud.google.com/bigquery(cameo:product/ncaa-bb-public/ncaa-basketball))

# Directions

First take some time to consider some unit tests that you would create yourself, before using Copilot to generate the tests it thinks you need.  Are there any missing? Any new ones?

- Create DBT Unit tests for your sql_merge.
- Create DBT Unit tests for your sql_join.
- Create DBT Unit tests for your analytical functions.
- Create DBT Unit tests for your sql_CTEs.

Use Copilot in a step-by-step manner to determine what coverage you need to test for each of the above, and generate the tests accordingly.

For Example: test for non-null values in key columns, and test for unique values in key columns.
