# ETL 

## Resources 

## Bitcoin daily price 

## Historical tweets 

The data was extracted using the Twitter API and the Academic Research credentials. The data is from 2020 up today. Using the API we got a lot of raw data from each tweet. Therefore we transfromed and selected only the relevant fields such as username, created_at, location, followers_count, retweet_count, likes_count, and some other more. We stored each tweet as a json into a our bucket named **tweets_crypto** following this structured: `year/month/tweet_id.json`. Then it was created a *BigQuery* database named **prueba_twits**, which has the table **historical_tweets** with all the tweets.

The notebook [tweets.ipynb](https://github.com/ro-juja/probable-umbrella/blob/main/src/tweets.ipynb) contains all the details. 

## References

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- [Search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query)
