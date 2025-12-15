# Architecture Overview
This project implements a modern **ELT (Extract–Load–Transform)** architecture using Snowflake-native ingestion, Airflow orchestration, and dbt transformations.
The design follows industry best practices by separating ingestion, orchestration, and transformation responsibilities across dedicated tools.

---

## High-Level Architecture
Source Files (CSV / CDC-style)
        ↓ 
MinIO (S3-compatible Object Storage)
        ↓ 
Snowflake Internal Stage
        ↓ 
Snowflake COPY INTO
(RAW / STAGING Tables)
        ↓ 
dbt Transformations
(STAGING → MART Models)
        ↓ 
Analytics / BI Consumption

---

## Component Responsibilities
### Object Storage (MinIO)
- Acts as the landing zone for batch and CDC-style CSV files
- Provides S3-compatible APIs for portability
- Decouples file delivery from warehouse ingestion

---

### Snowflake
Snowflake serves as the central data warehouse and ingestion engine.

Responsibilities:
- Stores raw and transformed data
- Manages internal stages for file ingestion
- Executes scalable, parallelized `COPY INTO` operations
- Maintains load history to prevent duplicate ingestion

Schemas are logically separated to support data lineage:
- RAW / STAGING for ingested data
- ANALYTICS / BASE for curated marts

---

### Apache Airflow
Airflow orchestrates the end-to-end pipeline.

Responsibilities:
- Coordinates ingestion and transformation steps
- Ensures dbt runs only after successful data loading
- Manages task dependencies and execution order
- Provides operational visibility and retry control

DAGs are intentionally scoped to single responsibilities:
- ingestion (`copy_into_raw`)
- transformation (`dbt_snowflake_pipeline`)

---

### dbt
dbt handles all transformation logic within Snowflake.

Responsibilities:
- Applies business logic and data modeling
- Implements staging and mart layers
- Enables testing, documentation, and lineage tracking
- Keeps transformation logic version-controlled

---

## Design Principles
- **ELT-first approach**: raw data is loaded before transformation
- **Separation of concerns**: ingestion, orchestration, and transformation are isolated
- **Snowflake-native ingestion**: avoids custom extract logic
- **Environment-driven configuration**: supports portability and reproducibility
- **Scalable by design**: leverages Snowflake’s compute model

---

## Extensibility
This architecture can be extended to support:
- External stages (S3 / ADLS / GCS)
- Incremental and micro-batch ingestion
- Data quality checks using dbt tests
- BI tools such as Power BI or Tableau
- CI/CD pipelines for dbt deployments

---
