# Machine Learning DAG Operations with Airflow 

Here you can find the dags for making continuous predictions automatically with airflow every day. The prediction will tell us if the price of bitcoin will rise or go down based on the sentiment analysis of tweets form the last day. 
The flow of this process is separated on three tasks:

1.	[today_tweets_bq.py]( https://github.com/ro-juja/probable-umbrella/blob/main/DAG/MLOPsDAG/today_tweets_bq.py) retrieve tweets .
2.	[analysis_tweets.py]( https://github.com/ro-juja/probable-umbrella/blob/main/DAG/MLOPsDAG/analysis_tweets.py ) sentiment analysis of the tweets.  
3.	[predict.py]( https://github.com/ro-juja/probable-umbrella/blob/main/DAG/MLOPsDAG/predict.py ) makes prediction of the day. 
