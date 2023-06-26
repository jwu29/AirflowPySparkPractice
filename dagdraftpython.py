from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'jwu29',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

def greet(trophies,ti):
    name = ti.xcom_pull(task_ids='get_name', key='first_name')
    print(f"Hello I am {name}!",
    f"and I have won {trophies} trophies!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Harry')
    ti.xcom_push(key='last_name', value='Kane')

with DAG(
    default_args=default_args,
    dag_id='TottenhamSucksv3',
    description='COYG',
    start_date=datetime(2023,5,28),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'trophies':0}
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )
    task2 >> task1
