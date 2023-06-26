from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner': 'jwu29',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='dagdraft_v3',
    default_args=default_args,
    description='Dag son where did you find this',
    start_date=datetime(2023,5,28,00),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo Somebody once told me"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo The world is gonna roll me"
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo Never Gonna Give You Up"
    )
    task1 >> [task2, task3]
