# ETL 

## Resources 

## Historical tweets 

The data was extracted using the [Twitter API](https://developer.twitter.com/en/docs/twitter-api) and the [Academic Research credentials](https://developer.twitter.com/en/products/twitter-api/academic-research). The data is from 2020 up today. Using the API we got a lot of raw data from each tweet. Therefore we transfromed and selected only the relevant fields such as username, created_at, location, followers_count, retweet_count, likes_count, and some other more. We stored each tweet as a json into a our bucket named **tweets_crypto** following this structured: `year/month/tweet_id.json`. Then it was created a *BigQuery* database named **prueba_twits**, which has the table **historical_tweets** with all the tweets.

The notebook [tweets.ipynb](https://github.com/ro-juja/probable-umbrella/blob/main/src/tweets.ipynb) contains all the details. 


## Bitcoin daily price 

We extracted The Historical Bitcoin prices from [Cryptocurrencies, Yahoo Finance](https://finance.yahoo.com/cryptocurrencies), the data is from 2014-09-17 to 2022-04-12. We added an index to the data in order to identify each price. We stored the historical data as a DataFrame and uploaded to the Bucket as a .csv in order to be able to work with such file easier. 

The notebook [Yahoo_bitcoin.ipynb](https://github.com/ro-juja/probable-umbrella/blob/main/src/Yahoo_bitcoin.ipynb) contains all the details, as well


## References

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- [Search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query)
- [Upload an object, Google Cloud](https://cloud.google.com/storage/docs/samples/storage-upload-file#storage_upload_file-python)
- [Cryptocurrencies, Yahoo Finance](https://finance.yahoo.com/cryptocurrencies)
- [Bitcoin and cryptocurrency price data from Yahoo! Finance, Data Ops](https://www.youtube.com/watch?v=x58MJUVNKMg)
