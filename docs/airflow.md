# Airflow Orchestration
Apache Airflow is used to orchestrate the end-to-end ELT workflow, ensuring that data ingestion completes successfully before downstream transformations are executed.

---

## DAGs
### copy_into_raw
Handles data ingestion into Snowflake.
Responsibilities:
- Uploads files to a Snowflake internal stage (`PUT`)
- Executes Snowflake `COPY INTO` to load data into the STAGING layer
- Triggers the downstream dbt pipeline only on successful load

---

### dbt_snowflake_pipeline
Handles data transformation using dbt.
Responsibilities:
- Validates Snowflake connectivity (`dbt debug`)
- Executes dbt staging models
- Executes dbt mart models

---

## Execution Flow
copy_into_raw -> TriggerDagRunOperator -> dbt_snowflake_pipeline

This design enforces clear dependency management and ensures transformations run only after successful ingestion.
