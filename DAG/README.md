# DAG 

This folder contains the files that are on the Airflow VM

|**File**|**Description**|
|:---:|:---:|
|**[dag.py](https://github.com/ro-juja/probable-umbrella/blob/main/DAG/dag.py)**|Airflow DAG Orchestration. The Dag runs every day at 00:00 to retrieve the tweets of day related to bitcoin. The tweets retrieved are then stored into our bucket with the historical database of tweets.|
|**[today_tweets.py](https://github.com/ro-juja/probable-umbrella/blob/main/DAG/today_tweets.py)**|This file contains the function that allow us to retrieved the tweets of the day.|
| **[MLOPs dags](https://github.com/ro-juja/probable-umbrella/tree/main/DAG/MLOPsDAG)**  | This folder contains the dags for making continuous predictions automatically with airflow every day. |

The keys that allow us to access the Twitter API are set as variables into the Airflow Instance, as well as the name of our bucket in GCS and the auth json path. 
