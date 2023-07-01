#!/usr/bin/python3
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

my_dag_id = "my_first_dag"

default_args = {
    'owner': 'keyproco',
    'depends_on_past': False,
    'retries': 10,
    'concurrency': 1
}

# dag declaration

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2023, 7, 1),
    schedule_interval='@daily'
)


# Here's a task based on Bash Operator!

bash_task = BashOperator(task_id='bash_task_1',
                         bash_command="echo 'Hello Airflow!'",
                         dag=dag)