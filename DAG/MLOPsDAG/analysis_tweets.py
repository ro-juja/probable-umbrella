import pandas as pd
import numpy as np 
import json
import csv
from datetime import datetime, timedelta
import time
import io
import os
from google.cloud import storage
from google.cloud import language

def analysis(bucket, bucketauth):
    def analyze_text_sentiment(text):
        client = language.LanguageServiceClient()
        document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
        
        response = client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment
        results = dict(
            text=text,
            score=sentiment.score,
            magnitude=sentiment.magnitude,
        )
        return (results)
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = bucketauth

    client = storage.Client.from_service_account_json(bucketauth)
    gcs_bucket = client.get_bucket(bucket)
    blob = gcs_bucket.blob('tweets2/tweets_day.csv')
    data = blob.download_as_string()
    tweets_hoy = pd.read_csv(io.BytesIO(data))

    tweets_relevant = tweets_hoy.sort_values(by='retweets',ascending=False)
    tweets_important = tweets_relevant[0:10]
    
    score=[]
    magnitude=[]
    for i in range(len(tweets_important)):
        analysis=analyze_text_sentiment(tweets_important.iloc[i][8])
        score.append(analysis['score'])
        magnitude.append(analysis['magnitude'])
        
    predict = []
    predict.append({'Mean Score': sum(score)/len(score), 
                    'Mean Magnitude': sum(magnitude)/len(magnitude)
                   })

    predict_df = pd.DataFrame(predict)
    gcs_bucket.blob('tweets2/predict.csv').upload_from_string(predict_df.to_csv(), 'text/csv')