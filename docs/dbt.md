# dbt Workflow
dbt is used to transform data loaded into Snowflake, following a layered modeling approach that separates raw ingestion from analytical outputs.

---

## Environment Configuration
dbt is configured using environment variables to support portability across environments (local, Docker, CI).
Key variables include:

- `SNOWFLAKE_DATABASE`
- `SNOWFLAKE_SCHEMA`
- `SNOWFLAKE_WAREHOUSE`
- `SNOWFLAKE_ROLE`
- `SNOWFLAKE_ACCOUNT`
- `SNOWFLAKE_USER`
- `SNOWFLAKE_PASSWORD`

These variables are referenced in `profiles.yml` using `env_var()`.

---

## Execution Workflow
Typical dbt execution flow:
```bash
dbt debug
dbt run
dbt test

## Model Layers
The project follows a standard layered modeling approach:

staging
Cleans and standardizes ingested data from Snowflake STAGING / RAW tables

marts
Contains curated, analytics-ready models designed for reporting and BI use cases

This structure improves maintainability, testing, and data lineage clarity.
