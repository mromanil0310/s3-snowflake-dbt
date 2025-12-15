# Setup Guide
This guide explains how to run the Snowflake ELT pipeline locally using Docker.

---

## Prerequisites
- Docker
- Docker Compose
- Snowflake account
- Git

---

## Environment Configuration
Create a `.env` file in the project root with the following variables:
```env
SNOWFLAKE_ACCOUNT=xxxx.ap-southeast-1
SNOWFLAKE_USER=xxxx
SNOWFLAKE_PASSWORD=xxxx
SNOWFLAKE_DATABASE=DBT_ELT
SNOWFLAKE_SCHEMA=STAGING
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_ROLE=ACCOUNTADMIN
These variables are used by both Airflow and dbt for Snowflake connectivity.

---

## Start the Pipeline
From the project root, start all services:

docker compose up -d

---

## Access Airflow
Once the services are running, open the Airflow UI:
http://localhost:8080

From the Airflow UI, trigger the ingestion DAG to begin the pipeline.
