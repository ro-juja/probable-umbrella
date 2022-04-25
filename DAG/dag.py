from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from new_tweets import new_tweets
import os

path = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(path, 'etl.py')

params = {
    'access_token': Variable.get("access_token"),
    'access_token_secret': Variable.get("access_token_secret"),
    'api_key': Variable.get("consumer_key"),
    'api_key_secret': Variable.get("consumer_secret"),
    'bearer_token': Variable.get("bearer_token"),
    'bucket': Variable.get("bucket")
    }


args = {
    'owner': 'Juan Escalona',
    'email': 'jh.escalona.s@gmail.com',
    'retries': 3,
    'depends_on_past': True,
}

dag = DAG(
    dag_id = 'New-tweets',
    schedule_interval = '0 0 * * *'
    start_date = days_ago(2)
    tags = ['bash', 'python', 'tweets_crypto']
    mas_active_runs = 1 
)


task1 = BashOperator(
    dag=dag,
    task_id='Install tweepy',
    bash_command='pip install tweepy'
)

task2 = PythonOperator(
    dag=dag,
    task_id = 'Get_new_tweets',
    provide_context=True,
    python_callable=new_tweets,
    op_kwargs={'access_token': params['access_token'], 'access_token_secret': params['access_token_secret'],
    'api_key': params['api_key'],'api_secret_key': params['api_secret_key'],
    'bucket': params['bucket']
    }
)