from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from ETL.today_tweets import new_tweets
import os

params = {
    'access_token': Variable.get("access_token"),
    'access_token_secret': Variable.get("access_token_secret"),
    'api_key': Variable.get("api_key"),
    'api_key_secret': Variable.get("api_key_secret"),
    'bearer_token': Variable.get("bearer_token"),
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
    dag_id = 'New-tweets',
    schedule_interval = '0 0 * * *',
    start_date = days_ago(2),
    tags = ['bash', 'python', 'tweets_crypto'],
    max_active_runs = 1 
)

task1 = PythonOperator(
    dag=dag,
    task_id = 'Get_new_tweets',
    provide_context=True,
    python_callable=new_tweets,
    op_kwargs={'bearer_token': params['bearer_token'],
    'bucket': params['bucket'],
    'bucketauth': params['bucketauth']
    }
)
