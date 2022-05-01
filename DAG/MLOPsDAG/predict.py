import pandas as pd 
import numpy as np 
import sklearn 
import pickle
import json
import os
import io
from datetime import datetime, timedelta 
from google.cloud import storage

def predict(bucket, bucketauth):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = bucketauth
    
    client = storage.Client.from_service_account_json(bucketauth)
    gcs_bucket = client.get_bucket(bucket)
    blob = gcs_bucket.blob('models/random_forest.pkl')
    pickle_in = blob.download_as_string()
    model = pickle.loads(pickle_in)
    
    blob2 = gcs_bucket.blob('tweets2/predict.csv')
    data = blob2.download_as_string()
    pd_predict = pd.read_csv(io.BytesIO(data))
    
    pd_predict = pd_predict.iloc[: , 1:]

    y=model.predict(pd_predict)
    
    if y[0] == 1:
        bitcoin_status = 'Bitcoin going up'
        print (bitcoin_status)
    else:
        bitcoin_status = 'Bitcoin going down'
        print(bitcoin_status)
        
    prediction = []
    d = datetime.today()- timedelta(days=1)
    yesterday = str(d.strftime('%Y-%m-%d'))
    
    prediction.append({'Date': yesterday, 
                       'Prediction': str(y[0]),
                       'Description': bitcoin_status
                      })
    
    
    path = f"tweets2/predictions/{yesterday[:4]}/{yesterday[5:7]}/prediction_{yesterday[8:]}.json"
    blob = gcs_bucket.blob(path)
    with blob.open(mode = 'w') as file:
            json.dump(prediction, file)
    