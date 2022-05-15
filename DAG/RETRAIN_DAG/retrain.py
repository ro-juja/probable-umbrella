import pandas as pd 
import numpy as np 
from pandas.io import gbq
import sklearn 
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import io
from google.cloud import storage, bigquery

def retrain_model(bucket, bucketauth):
    client = storage.Client.from_service_account_json(bucketauth)
    gcs_bucket = client.get_bucket(bucket)
    blob = gcs_bucket.blob('models/random_forest.pkl')
    pickle_in = blob.download_as_string()
    old_model = pickle.loads(pickle_in)
    
    price = """SELECT DISTINCT * FROM `dpa-2022-itam.prueba_twits.bitcoin_price`"""
    price_data = gbq.read_gbq(price, project_id = "dpa-2022-itam")
    
    X=price_data[['Mean_score', 'Mean_magnitude']]
    X.columns=['Mean Score', 'Mean Magnitude']
    Y=price_data['Up_down']
    Y=Y.astype('int')
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    new_model=RFC = RandomForestClassifier(n_estimators=1000, min_samples_split=2)
    
    print ("----Precision----")
    models= old_model, new_model
    spacing=max([len(models.__class__.__name__) for model in models])+4
    best_score=0
    for model in models:
        model.fit(x_train,y_train)
        model_score=model.score(x_test, y_test)
        if model_score > best_score:
            best_score =  model_score
            best_model = model
            model_name=model.__class__.__name__
            len_model_name=len(model_name)
        print(f"{model_name}:{model_score:>{spacing - len_model_name}.2f}")
    
    print(f'The best model is {best_model.__class__.__name__} with {best_score} of precision')
    
    path = 'models/random_forest.pkl'
    blob = gcs_bucket.blob(path)
    with blob.open(mode = 'wb') as file:
            pickle.dump(best_model, file)