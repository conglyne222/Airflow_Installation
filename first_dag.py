from asyncio.base_tasks import _task_get_stack
import os
import pandas as pd
from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable


def process_datetime(ti):
    dt = ti.xcom_pull(task_ids=['get_datetime'])
    dt1 = ti.xcom_pull(task_ids=['get_datetime'])

    if not dt:
        raise Exception('No datetime value.')

    dt = str(dt[0]).split() 
    dt1 = str(dt[1]).split(",")
    
    return {
        'year': int(dt[6]),
        'month': dt[4],
        'day': int(dt[2]),
        'day_of_week': str("Thu" + " " + dt1[0])
    }

with DAG(
    dag_id='first_airflow_dag',
    schedule_interval='* * * * *',
    start_date=datetime(year=2022,month=2,day=1),
    catchup=False
) as dag:
    # 1. Get current datetime
    task_get_datetime = BashOperator(
        task_id='get_datetime',
        bash_command='date',
    )
    # 2. Process current datetime
    task_process_datetime=PythonOperator(
        task_id='process_datetime',
        python_callable=process_datetime,
    )

    task_get_datetime >> task_process_datetime