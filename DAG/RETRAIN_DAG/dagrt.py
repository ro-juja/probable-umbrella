from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from ETL.new_price import new_price
from ETL.retrain import retrain_model
import os

params = {
    'bucket': Variable.get("bucket"),
    'bucketauth': Variable.get("bucketauth")
    }


args = {
    'owner': 'Juan Escalona',
    'email': 'jh.escalona.s@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}

dag = DAG(
    dag_id = 'RETRAIN_DAG',
    schedule_interval = '10 12 * * 0,2,5',
    start_date = days_ago(2),
    tags = ['bash', 'python', 'tweets_crypto'],
    max_active_runs = 1 
)

get_new_price = PythonOperator(
    dag=dag,
    task_id = 'Get_new_price',
    provide_context=True,
    python_callable=new_price,
    op_kwargs={
    'bucket': params['bucket'],
    'bucketauth': params['bucketauth']
    }
)

retraining_model = PythonOperator(
    dag=dag,
    task_id = 'Retrain_model',
    provide_context=True,
    python_callable=retrain_model,
    op_kwargs={'bucket': params['bucket'],
    'bucketauth': params['bucketauth']
    }
)


get_new_price >> retraining_model 
