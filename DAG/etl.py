import tweepy
import yaml
import pandas as pd
import json
import datetime
import time
from google.cloud import storage

#Setting keys and auth for twitter API
config_path = open("twitter_keys.yaml")
config = yaml.safe_load(config_path)
api_key = config['API Key']
api_key_secret = config['API Key Secret']
access_token = config['Access token']
access_token_secret = config['Access token secret']
bearer_token = config['Bearer token']

client = tweepy.Client(bearer_token, wait_on_rate_limit=True)

# Start date to query tweets 
start_date = datetime.date(2020,1,1)
end_date = datetime.date(2020,4,20)

# Function to generate dates
def gen_dates(start_date, end_date):
    new_start = start_date
    while new_start != end_date:
        new_start += datetime.timedelta(days=1)
        yield new_start
        
dates=[]
# Date in the right format to query
for d in gen_dates(start_date, end_date):
    new_date = str(d) + 'T00:00:00Z'
    dates.append(new_date)

final_tweets = []

print('Retrieving tweets from ' + str(start_date) + ' to ' + str(end_date))
for i in range (len(dates)-1):
    bitcoin_tweets = []
    for response in tweepy.Paginator(client.search_all_tweets, 
                                 query = 'Bitcoin -is:retweet lang:en is:verified',
                                 user_fields = ['username', 'public_metrics', 'description', 'location'],
                                 tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                 expansions = 'author_id',
                                 start_time = dates[i],
                                 end_time = dates[i+1],
                              max_results=200):
                              time.sleep(5)
                              bitcoin_tweets.append(response)
                              final_tweets.append(response)
                              if len(bitcoin_tweets) == 20:
                                  break

print('Tweets Retrieved')

result = []
user_dict = {}
# Loop through each response object
for response in final_tweets:
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

print ('There are '+ str(len(result)) + ' tweets')        
bucket = config['bucket']
client = storage.Client()
gcs_bucket = client.get_bucket(bucket)

print ('Conecting to bucket ' + bucket)

for row in result:
    path = f"tweets2/{row['created_at'][:4]}/{row['created_at'][5:7]}/tweet_{row['id']}.json"
    blob = gcs_bucket.blob(path)
    with blob.open(mode = 'w') as file:
        json.dump(row, file)

print('Tweets in bucket')