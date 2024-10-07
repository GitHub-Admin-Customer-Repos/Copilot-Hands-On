# GitHub Copilot SQL Procedures

We will be using a public data set in BigQuery as our data source.

[BigQuery – NCAA Basketball – Google Cloud console](https://console.cloud.google.com/bigquery(cameo:product/ncaa-bb-public/ncaa-basketball))


# Directions
- Analyze the total number of games played by each team, the average attendance for those games, and the mascot and color associated with each team.
- Aggregate the total number of games played and the average attendance for each team.
- Combines team colors and mascots information
- Aggregate game counts and average attendance data with the team information.

Example output:
| team_market | color       | mascot         | total_games | avg_attendance |
|-------------|-------------|----------------|-------------|----------------|
| Wildcats    | Blue        | Wildcat        | 25          | 15000          |
| Tigers      | Orange      | Tiger          | 22          | 14000          |
| Bulldogs    | Red         | Bulldog        | 20          | 13500          |
| Bears       | Green       | Bear           | 18          | 13000          |
| Eagles      | Yellow      | Eagle          | 15          | 12500          |



## Tables and Schema

Below is the json that details the schema of the Mascots table and the Team Colors table.

<details>

<summary>BigQuery – NCAA Basketball – Mascots</summary>

[BigQuery – NCAA Basketball – Mascots](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sncaa_basketball!3smascots)
```
  
  {
    "name": "id",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "University unique ID from Sportradar",
    "fields": []
  },
  {
    "name": "market",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The university to which the mascot belongs",
    "fields": []
  },
  {
    "name": "name",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The name of the university’s team",
    "fields": []
  },
  {
    "name": "mascot",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The name of the university's mascot",
    "fields": []
  },
  {
    "name": "mascot_name",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The proper name of the university's mascot, if available (e.g. a character)",
    "fields": []
  },
  {
    "name": "mascot_common_name",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The type of being or creature that the mascot embodies",
    "fields": []
  },
  {
    "name": "tax_subspecies",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The subspecies to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_species",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The species to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_genus",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The genus to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_family",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The family to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_order",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The order to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_class",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The class to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_phylum",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The phylum to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_kingdom",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The kingdom to which the mascot belongs",
    "fields": []
  },
  {
    "name": "tax_domain",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The domain to which the mascot belongs",
    "fields": []
  },
  {
    "name": "non_tax_type",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The non-Linnean type of being or creature to which the mascot belongs, if applicable",
    "fields": []
  }

```
</details>

<details>

<summary>BigQuery – NCAA Basketball – Team Colors</summary>

[BigQuery – NCAA Basketball – Team Colors](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sncaa_basketball!3steam_colors)

```[
  {
    "name": "market",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "",
    "fields": []
  },
  {
    "name": "id",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "",
    "fields": []
  },
  {
    "name": "code_ncaa",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "",
    "fields": []
  },
  {
    "name": "color",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "",
    "fields": []
  }
]
```
</details>

<details>

<summary>BigQuery – NCAA Basketball – Players</summary>

[NCAA Players Schema](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sncaa_basketball!3smbb_players_games_sr)

```
[

{

"name": "game_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Unique identifier for the game",

"fields": []

},

{

"name": "season",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game data] Season the game was played in",

"fields": []

},

{

"name": "neutral_site",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Game data] Indicator of whether the game was played on a neutral court",

"fields": []

},

{

"name": "scheduled_date",

"mode": "NULLABLE",

"type": "DATE",

"description": "[Game data] Date the game was played",

"fields": []

},

{

"name": "gametime",

"mode": "NULLABLE",

"type": "TIMESTAMP",

"description": "[Game data] Date and time the game was played",

"fields": []

},

{

"name": "tournament",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Whether the game was played in a post-season tournament",

"fields": []

},

{

"name": "tournament_type",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Type of post-season tournament a game was in played",

"fields": []

},

{

"name": "tournament_round",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Tournament round",

"fields": []

},

{

"name": "tournament_game_no",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Tournament game number",

"fields": []

},

{

"name": "player_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player Sportradar player ID",

"fields": []

},

{

"name": "last_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player last name",

"fields": []

},

{

"name": "first_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player first name",

"fields": []

},

{

"name": "full_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player full name",

"fields": []

},

{

"name": "abbr_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player abbreviated name (\"F.Last\")",

"fields": []

},

{

"name": "status",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player status as of 2017-18 season",

"fields": []

},

{

"name": "jersey_number",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player info] Player jersey number",

"fields": []

},

{

"name": "height",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player info] Player height",

"fields": []

},

{

"name": "weight",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player info] Player weight",

"fields": []

},

{

"name": "birth_place",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player birth place or home (Note: this information comes from the school's website, via Sportradar. While many of these entries indicate the player's birthplace, some of them may instead indicate the town that the players most identifies with.)",

"fields": []

},

{

"name": "birthplace_city",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player's home city (Note: this information comes from the school's website, via Sportradar. While many of these entries indicate the player's birthplace, some of them may instead indicate the town that the players most identifies with.)",

"fields": []

},

{

"name": "birthplace_state",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player's home state (Note: this information comes from the school's website, via Sportradar. While many of these entries indicate the player's birthplace, some of them may instead indicate the town that the players most identifies with.)",

"fields": []

},

{

"name": "birthplace_country",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player's home country (Note: this information comes from the school's website, via Sportradar. While many of these entries indicate the player's birthplace, some of them may instead indicate the town that the players most identifies with.)",

"fields": []

},

{

"name": "class",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player info] Player's class at game time (Note: this information comes from the school's website, via Sportradar.)",

"fields": []

},

{

"name": "team_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team name",

"fields": []

},

{

"name": "team_market",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team school name (using Sportradar names)",

"fields": []

},

{

"name": "team_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Sportradar team ID",

"fields": []

},

{

"name": "team_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team alias",

"fields": []

},

{

"name": "conf_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team current conference name",

"fields": []

},

{

"name": "conf_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team current conference alias",

"fields": []

},

{

"name": "division_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team current division name",

"fields": []

},

{

"name": "division_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team current division alias",

"fields": []

},

{

"name": "league_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Team info] Team current league name",

"fields": []

},

{

"name": "home_team",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Team info] Indicator of whether the team was the home team",

"fields": []

},

{

"name": "active",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Player stats] Indicator of whether the player was active for the game",

"fields": []

},

{

"name": "played",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Player stats] Indicator of whether the player played in the game",

"fields": []

},

{

"name": "starter",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Player stats] Indicator of whether the player started the game",

"fields": []

},

{

"name": "minutes",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player stats] Minutes played",

"fields": []

},

{

"name": "minutes_int64",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Minutes played (as integer)",

"fields": []

},

{

"name": "position",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player stats] Position",

"fields": []

},

{

"name": "primary_position",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Player stats] Primary position",

"fields": []

},

{

"name": "field_goals_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Field goals made",

"fields": []

},

{

"name": "field_goals_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Field goals attempted",

"fields": []

},

{

"name": "field_goals_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Player stats] Field goal percentage",

"fields": []

},

{

"name": "three_points_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Three-pointers made",

"fields": []

},

{

"name": "three_points_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Three-pointers attempted",

"fields": []

},

{

"name": "three_points_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Player stats] Three-point shot percentage",

"fields": []

},

{

"name": "two_points_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Two-pointers made",

"fields": []

},

{

"name": "two_points_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Two-pointers attempted",

"fields": []

},

{

"name": "two_points_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Player stats] Two-point shot percentage",

"fields": []

},

{

"name": "blocked_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Number of shots blocked by the other team",

"fields": []

},

{

"name": "free_throws_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Free throws made",

"fields": []

},

{

"name": "free_throws_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Free throws attempted",

"fields": []

},

{

"name": "free_throws_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Player stats] Free throw percentage",

"fields": []

},

{

"name": "offensive_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Offensive rebounds",

"fields": []

},

{

"name": "defensive_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Defensive rebounds",

"fields": []

},

{

"name": "rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Total rebounds",

"fields": []

},

{

"name": "assists",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Assists",

"fields": []

},

{

"name": "turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Turnovers",

"fields": []

},

{

"name": "steals",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Steals",

"fields": []

},

{

"name": "blocks",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Blocks",

"fields": []

},

{

"name": "assists_turnover_ratio",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Player stats] Assist-to-turnover ratio",

"fields": []

},

{

"name": "personal_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Personal fouls committed",

"fields": []

},

{

"name": "tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Technical fouls committed",

"fields": []

},

{

"name": "flagrant_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Flagrant fouls committed",

"fields": []

},

{

"name": "points",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Player stats] Points scored",

"fields": []

},

{

"name": "sp_created",

"mode": "NULLABLE",

"type": "TIMESTAMP",

"description": "[Table data] Box score data entry time",

"fields": []

}

]
```

</details>


<details>

<summary>BigQuery – NCAA Basketball – Games</summary>

[NCAA Games Schema](https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sbigquery-public-data!2sncaa_basketball!3smbb_players_games_sr)

```
[

{

"name": "game_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Unique identifier for the game",

"fields": []

},

{

"name": "season",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game data] Season the game was played in",

"fields": []

},

{

"name": "status",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Indicates the last state of Sportradar's game file",

"fields": []

},

{

"name": "coverage",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Type of coverage provided by Sportradar",

"fields": []

},

{

"name": "neutral_site",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Game data] Indicator of whether the game was played on a neutral court",

"fields": []

},

{

"name": "scheduled_date",

"mode": "NULLABLE",

"type": "DATE",

"description": "[Game data] Date the game was played",

"fields": []

},

{

"name": "gametime",

"mode": "NULLABLE",

"type": "TIMESTAMP",

"description": "[Game data] Date and time the game was played",

"fields": []

},

{

"name": "conference_game",

"mode": "NULLABLE",

"type": "BOOLEAN",

"description": "[Game data] Indicator of whether the two teams were in the same conference at the time the game was played",

"fields": []

},

{

"name": "tournament",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Whether the game was played in a post-season tournament",

"fields": []

},

{

"name": "tournament_type",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Type of post-season tournament a game was in played",

"fields": []

},

{

"name": "tournament_round",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Tournament round",

"fields": []

},

{

"name": "tournament_game_no",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Tournament game number",

"fields": []

},

{

"name": "attendance",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game data] Attendance of the game",

"fields": []

},

{

"name": "lead_changes",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game stats] Number of lead changes in the game",

"fields": []

},

{

"name": "times_tied",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game stats] Number of ties in the game",

"fields": []

},

{

"name": "periods",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game stats] Number of periods the game",

"fields": []

},

{

"name": "possession_arrow",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game stats] The unique identifier of the team that would receive the ball the next time a jump ball is called, see https://en.wikipedia.org/wiki/Jump_ball for more information",

"fields": []

},

{

"name": "venue_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Unique identifier for the venue where the game was played",

"fields": []

},

{

"name": "venue_city",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] City where the game was played",

"fields": []

},

{

"name": "venue_state",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] State where the game was played",

"fields": []

},

{

"name": "venue_address",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Address of the venue where the game was played",

"fields": []

},

{

"name": "venue_zip",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Address of the venue where the game was played",

"fields": []

},

{

"name": "venue_country",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Country where the game was played",

"fields": []

},

{

"name": "venue_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Game data] Name of the venue where the game was played",

"fields": []

},

{

"name": "venue_capacity",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Game data] Current capacity of the venue where the game was played",

"fields": []

},

{

"name": "h_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team name",

"fields": []

},

{

"name": "h_market",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team school name",

"fields": []

},

{

"name": "h_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team school ID from SportRadar (unique)",

"fields": []

},

{

"name": "h_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team school alias (unique)",

"fields": []

},

{

"name": "h_league_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team school league ID (not unique)",

"fields": []

},

{

"name": "h_league_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team school league name (not unique)",

"fields": []

},

{

"name": "h_league_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team school league alias (not unique)",

"fields": []

},

{

"name": "h_conf_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team current conference ID (not unique)",

"fields": []

},

{

"name": "h_conf_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team current conference name (not unique)",

"fields": []

},

{

"name": "h_conf_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team current conference alias (not unique)",

"fields": []

},

{

"name": "h_division_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team current division ID (not unique)",

"fields": []

},

{

"name": "h_division_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team current division name (not unique)",

"fields": []

},

{

"name": "h_division_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team current division alias (not unique)",

"fields": []

},

{

"name": "h_logo_large",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team logo 200x200",

"fields": []

},

{

"name": "h_logo_medium",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team logo 70x70",

"fields": []

},

{

"name": "h_logo_small",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team data] Home team logo 24x24",

"fields": []

},

{

"name": "h_points_game",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home points scored",

"fields": []

},

{

"name": "h_rank",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home rank",

"fields": []

},

{

"name": "h_minutes",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Home Team stats] Home total minutes played",

"fields": []

},

{

"name": "h_field_goals_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home field goals made",

"fields": []

},

{

"name": "h_field_goals_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home field goals attempted",

"fields": []

},

{

"name": "h_field_goals_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Home Team stats] Home field goal percentage",

"fields": []

},

{

"name": "h_three_points_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home three-pointers made",

"fields": []

},

{

"name": "h_three_points_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home three-pointers attempted",

"fields": []

},

{

"name": "h_three_points_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Home Team stats] Home three-point shot percentage",

"fields": []

},

{

"name": "h_two_points_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home two-pointers made",

"fields": []

},

{

"name": "h_two_points_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home two-pointers attempted",

"fields": []

},

{

"name": "h_two_points_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Home Team stats] Home two-point shot percentage",

"fields": []

},

{

"name": "h_blocked_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Number of the home team's shots blocked by the away team",

"fields": []

},

{

"name": "h_free_throws_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home free throws made",

"fields": []

},

{

"name": "h_free_throws_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home free throws attempted",

"fields": []

},

{

"name": "h_free_throws_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Home Team stats] Home free throw percentage",

"fields": []

},

{

"name": "h_offensive_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home offensive rebounds",

"fields": []

},

{

"name": "h_defensive_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home defensive rebounds",

"fields": []

},

{

"name": "h_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home total rebounds",

"fields": []

},

{

"name": "h_assists",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home assists",

"fields": []

},

{

"name": "h_turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home turnovers",

"fields": []

},

{

"name": "h_steals",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home steals",

"fields": []

},

{

"name": "h_blocks",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home blocks",

"fields": []

},

{

"name": "h_assists_turnover_ratio",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Home Team stats] Home assist-to-turnover ratio",

"fields": []

},

{

"name": "h_personal_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home personal fouls committed",

"fields": []

},

{

"name": "h_ejections",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home player ejections",

"fields": []

},

{

"name": "h_foulouts",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home player foul-outs",

"fields": []

},

{

"name": "h_points",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home total points scored",

"fields": []

},

{

"name": "h_fast_break_pts",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home fast-break points scored",

"fields": []

},

{

"name": "h_second_chance_pts",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home second-chance points scored",

"fields": []

},

{

"name": "h_team_turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home team turnovers",

"fields": []

},

{

"name": "h_points_off_turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home points off turnovers",

"fields": []

},

{

"name": "h_team_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home team rebounds",

"fields": []

},

{

"name": "h_flagrant_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home flagrant fouls committed",

"fields": []

},

{

"name": "h_player_tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home technical fouls committed",

"fields": []

},

{

"name": "h_team_tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home technical fouls committed by team",

"fields": []

},

{

"name": "h_coach_tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Home Team stats] Home technical fouls committed by coach",

"fields": []

},

{

"name": "a_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team name",

"fields": []

},

{

"name": "a_market",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team school name",

"fields": []

},

{

"name": "a_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team school ID from SportRadar (unique)",

"fields": []

},

{

"name": "a_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team school alias (unique)",

"fields": []

},

{

"name": "a_league_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team school league ID (not unique)",

"fields": []

},

{

"name": "a_league_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team school league name (not unique)",

"fields": []

},

{

"name": "a_league_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team school league alias (not unique)",

"fields": []

},

{

"name": "a_conf_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team current conference ID (not unique)",

"fields": []

},

{

"name": "a_conf_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team current conference name (not unique)",

"fields": []

},

{

"name": "a_conf_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team current conference alias (not unique)",

"fields": []

},

{

"name": "a_division_id",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team current division ID (not unique)",

"fields": []

},

{

"name": "a_division_name",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team current division name (not unique)",

"fields": []

},

{

"name": "a_division_alias",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team current division alias (not unique)",

"fields": []

},

{

"name": "a_logo_large",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team logo 200x200",

"fields": []

},

{

"name": "a_logo_medium",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team logo 70x70",

"fields": []

},

{

"name": "a_logo_small",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team data] Away team logo 24x24",

"fields": []

},

{

"name": "a_points_game",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away points scored",

"fields": []

},

{

"name": "a_rank",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away rank",

"fields": []

},

{

"name": "a_minutes",

"mode": "NULLABLE",

"type": "STRING",

"description": "[Away Team stats] Away total minutes played",

"fields": []

},

{

"name": "a_field_goals_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away field goals made",

"fields": []

},

{

"name": "a_field_goals_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away field goals attempted",

"fields": []

},

{

"name": "a_field_goals_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Away Team stats] Away field goal percentage",

"fields": []

},

{

"name": "a_three_points_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away three-pointers made",

"fields": []

},

{

"name": "a_three_points_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away three-pointers attempted",

"fields": []

},

{

"name": "a_three_points_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Away Team stats] Away three-point shot percentage",

"fields": []

},

{

"name": "a_two_points_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away two-pointers made",

"fields": []

},

{

"name": "a_two_points_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away two-pointers attempted",

"fields": []

},

{

"name": "a_two_points_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Away Team stats] Away two-point shot percentage",

"fields": []

},

{

"name": "a_blocked_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Number of the away team's shots blocked by the away team",

"fields": []

},

{

"name": "a_free_throws_made",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away free throws made",

"fields": []

},

{

"name": "a_free_throws_att",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away free throws attempted",

"fields": []

},

{

"name": "a_free_throws_pct",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Away Team stats] Away free throw percentage",

"fields": []

},

{

"name": "a_offensive_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away offensive rebounds",

"fields": []

},

{

"name": "a_defensive_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away defensive rebounds",

"fields": []

},

{

"name": "a_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away total rebounds",

"fields": []

},

{

"name": "a_assists",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away assists",

"fields": []

},

{

"name": "a_turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away turnovers",

"fields": []

},

{

"name": "a_steals",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away steals",

"fields": []

},

{

"name": "a_blocks",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away blocks",

"fields": []

},

{

"name": "a_assists_turnover_ratio",

"mode": "NULLABLE",

"type": "FLOAT",

"description": "[Away Team stats] Away assist-to-turnover ratio",

"fields": []

},

{

"name": "a_personal_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away personal fouls committed",

"fields": []

},

{

"name": "a_ejections",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away player ejections",

"fields": []

},

{

"name": "a_foulouts",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away player foul-outs",

"fields": []

},

{

"name": "a_points",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away total points scored",

"fields": []

},

{

"name": "a_fast_break_pts",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away fast-break points scored",

"fields": []

},

{

"name": "a_second_chance_pts",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away second-chance points scored",

"fields": []

},

{

"name": "a_team_turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away team turnovers",

"fields": []

},

{

"name": "a_points_off_turnovers",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away points off turnovers",

"fields": []

},

{

"name": "a_team_rebounds",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away team rebounds",

"fields": []

},

{

"name": "a_flagrant_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away flagrant fouls committed",

"fields": []

},

{

"name": "a_player_tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away technical fouls committed",

"fields": []

},

{

"name": "a_team_tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away technical fouls committed by team",

"fields": []

},

{

"name": "a_coach_tech_fouls",

"mode": "NULLABLE",

"type": "INTEGER",

"description": "[Away Team stats] Away technical fouls committed by coach",

"fields": []

},

{

"name": "created",

"mode": "NULLABLE",

"type": "TIMESTAMP",

"description": "[Table data] Box score data entry time",

"fields": []

}

]

</details>