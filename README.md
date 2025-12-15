# End-to-End Snowflake ELT Pipeline  
**(Airflow · dbt · Snowflake · MinIO · Docker)**

This repository implements a **production-style ELT data pipeline** using **Snowflake** as the cloud data warehouse, **Apache Airflow** for orchestration, and **dbt** for transformations. Data is ingested from **S3-compatible object storage (MinIO)** and loaded using **Snowflake-native `PUT` and `COPY INTO` commands**.

The solution demonstrates modern **cloud data engineering best practices**, including separation of ingestion and transformation layers, environment-driven configuration, and automated orchestration.

---

## Business Use Case
This pipeline simulates a **real-world operational data ingestion scenario** where CSV or CDC-style files are continuously delivered to object storage and must be reliably ingested into a cloud data warehouse for analytics and reporting. The design supports scalable batch ingestion, repeatable loads, and downstream transformations, making it suitable for use cases such as **order processing analytics, operational reporting, and BI dashboards**.

---

## Architecture Overview
MinIO / File Drop (CSV, CDC-style)  
                ↓  
Snowflake Internal Stage (`PUT`)  
                ↓  
Snowflake `COPY INTO` (RAW / STAGING layer)  
                ↓  
dbt Transformations (STAGING → MART)

---

## Technology Stack
| Layer              | Technology            |
|--------------------|-----------------------|
| Object Storage     | MinIO (S3-compatible) |
| Data Warehouse     | Snowflake             |
| Orchestration      | Apache Airflow        |
| Transformations    | dbt                   |
| Containerization   | Docker                |

---

## Key Features
- End-to-end ELT pipeline using **Snowflake, Airflow, and dbt**
- Snowflake-native ingestion using **internal stages, `PUT`, and `COPY INTO`**
- Automated DAG-based orchestration in **Apache Airflow**
- dbt models executed after successful data ingestion
- Environment-variable–driven configuration for portability
- Supports incremental / CDC-style file ingestion patterns

---

## How to Run
Detailed setup and execution instructions are available in the documentation:
- [`docs/setup.md`](docs/setup.md)
- [`docs/airflow.md`](docs/airflow.md)
- [`docs/dbt.md`](docs/dbt.md)