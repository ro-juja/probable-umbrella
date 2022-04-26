# DAG 

This folder contains the files that are on the Airflow VM

|**File**|**Description**|
|:---:|:---:|
|**[dag.py](https://github.com/ro-juja/probable-umbrella/blob/main/DAG/dag.py)**|Airflow DAG Orchestration. The Dag runs every day at 00:00 to retrieve the tweets of day related to bitcoin. The tweets retrieved are then stored into our bucket with the historical database of tweets.|
|**[today_tweets.py](https://github.com/ro-juja/probable-umbrella/blob/main/DAG/today_tweets.py)**|This file contains the function that allow us to retrieved the tweets of the day.|

