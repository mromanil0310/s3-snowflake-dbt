from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

PROJECT_DIR = '~/s3-snowflake-dbt/snowflake'
PROFILES_DIR = '~/.dbt'

# Default args for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    'dbt_snowflake_pipeline',
    default_args=default_args,
    description='A simple pipeline to run dbt commands on Snowflake',
    schedule='@daily',  # Trigger manually or set your schedule
    start_date=datetime(2025, 12, 11),
    catchup=False,
) as dag:
    
    # dag to signify start of execution
    start = EmptyOperator(task_id='start_dag')

    # TaskGroup to  group and run together all dbt related tasks
    with TaskGroup(group_id='dbt_tasks') as dbt_tasks:
        # Task to run dbt debug
        dbt_debug = BashOperator(
            task_id="dbt_tasks.dbt_debug",
            bash_command="cd /opt/dbt && dbt debug",
        )

        # Task to run dbt run
        dbt_run = BashOperator(
            task_id="dbt_tasks.dbt_run",
            bash_command="cd /opt/dbt && dbt run",
        )
        # Task to run dbt test
        dbt_test = BashOperator(
            task_id="dbt_tasks.dbt_test",
            bash_command="cd /opt/dbt && dbt test",
        )

        dbt_debug >> dbt_run >> dbt_test

    # end dag
    end = EmptyOperator(task_id='end_dag')

    # Define task dependencies
    start >> dbt_tasks >> end
