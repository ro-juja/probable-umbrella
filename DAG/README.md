# DAG 

## Airflow instance description
We made and airflow instance on GCP by the name of “airflow3”. It automatically turns on at 00:00 and turs off at 00:40 (GTM time) every day. The instance has a bash script that allows it to copy documents from our bucket, so it has the code to run the different DAGs. 
To access the instance, we use the external IP and the port 8080. 

Inside of this instance we have: 


|**File**|**Description**|
|:---:|:---:|
|**[dag.py](https://github.com/ro-juja/probable-umbrella/blob/main/DAG/dag.py)**|Airflow DAG Orchestration. The Dag runs every day at 00:00 to retrieve the tweets of day related to bitcoin. The tweets retrieved are then stored into our bucket with the historical database of tweets.|
|**[today_tweets.py](https://github.com/ro-juja/probable-umbrella/blob/main/DAG/today_tweets.py)**|This file contains the function that allow us to retrieved the tweets of the day.|
| **[MLOPs dags](https://github.com/ro-juja/probable-umbrella/tree/main/DAG/MLOPsDAG)**  | This folder contains the dags for making continuous predictions automatically with airflow every day. |

The keys that allow us to access the Twitter API are set as variables into the Airflow Instance, as well as the name of our bucket in GCS and the auth json path. 

