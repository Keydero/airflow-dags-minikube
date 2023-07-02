from airflow import DAG

from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime

with DAG(
    'user_processing',
    start_date=datetime(2023, 7, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    create_table = PostgresOperator(
        task_id='Create_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NIT NULL
            );
        '''
    )