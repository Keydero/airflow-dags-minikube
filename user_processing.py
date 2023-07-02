import json

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor

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
                country TEXT NOT NULL
            );
        '''
    )

    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',
        endpoint='api/'
    )

    extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='user_api',
        endpoint='api/',
        method='GET',
        response_filter= lambda response: json.load(response.text),
        log_response=True
    )
