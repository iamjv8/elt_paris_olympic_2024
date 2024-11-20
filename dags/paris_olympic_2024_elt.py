from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from tasks.db import create_tables
from tasks.load_data import load_data

default_args = {
    "owner": "Jayesh Vekariya",
    "retry": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(dag_id="paris_olympic_2024_elt", default_args=default_args) as dag:
    create_table = PythonOperator(
        task_id="Create_Tables", python_callable=create_tables
    )

    extract_and_load_data = PythonOperator(
        task_id="Extract_and_Load", python_callable=load_data
    )

    create_table >> extract_and_load_data
