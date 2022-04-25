import tweepy
import yaml
import pandas as pd
import json
import datetime
import time
from google.cloud import storage

def new_tweets(api_key, api_key_secret, access_token, access_token_secret, bucket):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    data = []
    keywords = '#bitcoin'
    limit = 100
    for tweet in tweepy.Cursor(api.search_tweets, lang = 'en', q = keywords, count = 100, tweet_mode = 'extended').items(limit):
        data.append(tweet._json)
    
    data1=[]
    for i in data:
        if i["lang"] == "en":
            test = {
                "id": i["id"],
                "lang": i["lang"],
                "created_at": i["created_at"],
                "text": i["full_text"],
                "retweet_count": i["retweet_count"],
            }
            data1.append(test)
    
    client = storage.Client()
    gcs_bucket = client.get_bucket(bucket)
    
    for row in data1:
        path = f"tweets/{row['created_at'][:4]}/{row['created_at'][5:7]}/tweet_{row['id']}.json"
        blob = gcs_bucket.blob(path)
        with blob.open(mode = 'w') as file:
            json.dump(row, file)
