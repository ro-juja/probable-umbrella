import tweepy
import yaml
import pandas as pd
import json
from datetime import datetime, timedelta
import time
from google.cloud import storage

def new_tweets(bearer_token, bucket, bucketauth):
    client = tweepy.Client(bearer_token, wait_on_rate_limit=True)
    today = str(datetime.today().strftime('%Y-%m-%d')) + 'T00:00:00Z'
    d = datetime.today()- timedelta(days=1)
    yesterday = str(d.strftime('%Y-%m-%d')) +'T00:00:00Z'
    tweets_day=[]
    for response in tweepy.Paginator(client.search_all_tweets, 
                                 query = 'Bitcoin -is:retweet lang:en is:verified',
                                 user_fields = ['username', 'public_metrics', 'description', 'location'],
                                 tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                 expansions = 'author_id',
                                 start_time = yesterday,
                                 end_time = today,
                              max_results=10):
                              time.sleep(1)
                              tweets_day.append(response)
    
    result = []
    user_dict = {}
    # Loop through each response object
    for response in tweets_day:
    # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
        for user in response.includes['users']:
            user_dict[user.id] = {'username': user.username, 
            'followers': user.public_metrics['followers_count'],
            'tweets': user.public_metrics['tweet_count'],
            'description': user.description,
            'location': user.location
            }
        for tweet in response.data:
            # For each tweet, find the author's information
            author_info = user_dict[tweet.author_id]
            # Put all of the information we want to keep in a single dictionary for each tweet
            result.append({'id': str(tweet.id), 
                       'author_id': str(tweet.author_id),
                       'username': author_info['username'],
                       'author_followers': author_info['followers'],
                       'author_tweets': author_info['tweets'],
                       'author_description': author_info['description'],
                       'author_location': author_info['location'],
                       'text': tweet.text,
                       'created_at': str(tweet.created_at),
                       'retweets': tweet.public_metrics['retweet_count'],
                       'replies': tweet.public_metrics['reply_count'],
                       'likes': tweet.public_metrics['like_count'],
                       'quote_count': tweet.public_metrics['quote_count']
                      })
    
    client = storage.Client.from_service_account_json(bucketauth)
    gcs_bucket = client.get_bucket(bucket)

    for row in result:
        path = f"tweets2/{row['created_at'][:4]}/{row['created_at'][5:7]}/tweet_{row['id']}.json"
        blob = gcs_bucket.blob(path)
        with blob.open(mode = 'w') as file:
            json.dump(row, file)
    
    tweets = pd.DataFrame(result)
    gcs_bucket.blob('tweets2/tweets_day.csv').upload_from_string(tweets.to_csv(), 'text/csv')