from airflow import DAG
from datetime import datetime
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
    dag_id="copy_into_raw",
    start_date=datetime(2025, 12, 11),
    schedule=None,
    catchup=False,
    tags=["snowflake", "copy_into"],
) as dag:

    copy_orders = SnowflakeOperator(
        task_id="copy_into_order",
        snowflake_conn_id="snowflake_default",
        sql="""
        COPY INTO DBT_ELT.STAGING.ORDERS
        FROM @DBT_ELT.STAGING.MY_INTERNAL_STAGE
        FILE_FORMAT = (TYPE=CSV SKIP_HEADER=1);
        """
    )

    trigger_dbt_pipeline = TriggerDagRunOperator(
        task_id="trigger_dbt_snowflake_pipeline",
        trigger_dag_id="dbt_snowflake_pipeline",
        wait_for_completion=False,   # set True if you want copy_into_raw to wait
        reset_dag_run=True,          # rerun if a run with same logical date exists
        conf={"source_dag": "copy_into_raw"}  # optional metadata
    )

    copy_orders >> trigger_dbt_pipeline
