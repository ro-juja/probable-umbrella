import yfinance as yf
import pandas as pd
from pandas.io import gbq
import json
from datetime import datetime, timedelta
import time
from google.cloud import storage, bigquery

def new_price(bucket, bucketauth):
    # Query last record of bitcoin price
    price = """SELECT * FROM `dpa-2022-itam.prueba_twits.bitcoin_price` ORDER BY Date DESC LIMIT 1"""
    price_data = gbq.read_gbq(price, project_id = "dpa-2022-itam")
    last_price=price_data['Date'][0]
    new_date=str(last_price + timedelta(days=1))[:10]
    today = str(datetime.today().strftime('%Y-%m-%d'))
    
    # Query the scores of the sentiment analysis of the new tweets
    score = f"""SELECT * FROM `dpa-2022-itam.prueba_twits.sentiment_scores` WHERE Date BETWEEN '{new_date}' AND '{today}'"""
    scores = gbq.read_gbq(score, project_id = "dpa-2022-itam")
    scores['Date'] = pd.to_datetime(scores['Date'])
    
    #Get new price
    symbol = 'BTC-USD'
    df = yf.download(symbol, start=new_date, end = today)
    x=df['Open'].diff()
    x1=x[1:].tolist()
    up_down = []
    for i in x1:
        if i < 0:
            up_down.append(0)
        else:
            up_down.append(1)
    df_scores=pd.merge(df, scores, on='Date')
    df_scores['up_down'] = up_down
    result=[]
    for i in range(len(df_scores)):
        result.append({'Date': str(df_scores['Date'][i]),
                       'Open': df_scores['Open'][i],
                       'High': df_scores['High'][i],
                       'Low': df_scores['Low'][i],
                       'Close': df_scores['Close'][i],
                       'Adj_close': df_scores['Adj Close'][i],
                       'Volume': int(df_scores['Volume'][i]),
                       'Up_down': int(df_scores['up_down'][i]),
                       'Mean_score': float(df_scores['Mean_score'][i]),
                       'Mean_magnitude': df_scores['Mean_magnitude'][i]
                      })
    
    # Inset new data to table
    client_big = bigquery.Client.from_service_account_json(bucketauth)
    table_id = 'dpa-2022-itam.prueba_twits.bitcoin_price'

    client_big.insert_rows_json(table_id, result)
    
    # Load new data to gcs
    client = storage.Client.from_service_account_json(bucketauth)
    gcs_bucket = client.get_bucket(bucket)
    
    if len(result) == 1:
        path = f"bitcoin/{result[0]['Date'][:4]}/price_{result[0]['Date'][5:10]}.json"
        blob = gcs_bucket.blob(path)
        with blob.open(mode = 'w') as file:
            json.dump(result, file)
    else:
        for row in result:
            path = f"bitcoin/{row['Date'][:4]}/price_{row['Date'][5:10]}.json"
            blob = gcs_bucket.blob(path)
            with blob.open(mode = 'w') as file:
                json.dump(row, file)