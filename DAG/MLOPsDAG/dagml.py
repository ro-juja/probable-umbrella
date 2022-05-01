from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from airflow.utils.dates import days_ago
from ETL.today_tweets_bq import new_tweets
from ETL.analysis_tweets import analysis
from ETL.predict import predict 
import os

params = {
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
    dag_id = 'MLOPs_DAG',
    schedule_interval = '10 0 * * *',
    start_date = days_ago(2),
    tags = ['bash', 'python', 'tweets_crypto'],
    max_active_runs = 1 
)

get_new_tweets = PythonOperator(
    dag=dag,
    task_id = 'Get_new_tweets',
    provide_context=True,
    python_callable=new_tweets,
    op_kwargs={'bearer_token': params['bearer_token'],
    'bucket': params['bucket'],
    'bucketauth': params['bucketauth']
    }
)

analyze_tweets = PythonOperator(
    dag=dag,
    task_id = 'Sentiment-analysis',
    provide_context=True,
    python_callable=analysis,
    op_kwargs={'bucket': params['bucket'],
    'bucketauth': params['bucketauth']
    }
)

predictions = PythonOperator(
    dag=dag,
    task_id = 'Predict',
    provide_context=True,
    python_callable=predict,
    op_kwargs={'bucket': params['bucket'],
    'bucketauth': params['bucketauth']
    }
)

get_new_tweets >> analyze_tweets >> predictions
