# Machine Learning DAG Operations with Airflow 

Here you can find the dags for making continuous predictions automatically with airflow every day. This process runs every day at 00:10am(GMT time). The prediction will tell us if the price of bitcoin will rise or go down based on the sentiment analysis of tweets form the last day.  
The flow of this process is separated on three tasks:

1.	[today_tweets_bq.py]( https://github.com/ro-juja/probable-umbrella/blob/main/DAG/MLOPsDAG/today_tweets_bq.py) retrieve tweets .
2.	[analysis_tweets.py]( https://github.com/ro-juja/probable-umbrella/blob/main/DAG/MLOPsDAG/analysis_tweets.py ) sentiment analysis of the tweets.  
3.	[predict.py]( https://github.com/ro-juja/probable-umbrella/blob/main/DAG/MLOPsDAG/predict.py ) makes prediction of the day. 

### 1 Retrieve tweets
This DAG collects approximately 1000 tweets (relevant to #bitcoin) from the last day. They are uploaded to storage on a bucket in the folder “tweets2”, they are organized in more folders by year and month. 
Also, this task creates a .csv with the tweets to read them more easily for the next task in the flow. 

### 2 Sentiment analysis of the tweets
This DAG calls the tweets collected by the last tag, order them by importance (number of retweets) and sends them to the API of sentiment analysis from google. Then it calculates the average score and magnitude of the day and saves it on a csv. 

### 3 Predictions
This last DAG calls the csv of the sentiment analysis of the tweets, calls the model (random forest) already trained and makes the prediction of the day. The results (up or down of the price) are saved on a JSON on the bucket in the folder “tweets2” and then in the folder “predictions”.
