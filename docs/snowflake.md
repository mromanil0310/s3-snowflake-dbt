# Snowflake Design
This project uses Snowflake-native features for scalable, reliable data ingestion and transformation.

---

## Schema Design
The database is organized using a layered schema approach:

- **RAW / STAGING**  
  Stores ingested data loaded directly from files using `COPY INTO`

- **ANALYTICS / BASE**  
  Stores transformed and curated data models produced by dbt (marts)

This separation supports clear data lineage and simplifies downstream analytics.

---

## Loading Strategy
Data ingestion is handled using Snowflake-native mechanisms:

- Files uploaded to an internal Snowflake stage using `PUT`
- Data loaded into tables using `COPY INTO`
- Automatic file compression (`.csv.gz`)
- Optional regex-based file selection for CDC-style ingestion

Snowflake load history is leveraged to prevent accidental duplicate loads.

---

## Example: COPY INTO
```sql
COPY INTO DBT_ELT.STAGING.ORDERS
FROM @DBT_ELT.STAGING.MY_INTERNAL_STAGE
FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1);

This approach minimizes custom ingestion logic and delegates scalability and reliability to Snowflake.