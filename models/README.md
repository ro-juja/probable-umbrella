# Machine Learning Model Training

The Machine Learning model training was developed in three steps that are depicted in the next image:

<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg4_diagram.png">

1. First, all the Twitter data and Yahoo Finance was retrieved from the Twitter API and the Yahoo Finance API. Although there were some restrictions, for the purpose of the project it was possible to retrieve all the required data. Some considerations were taken, for example, the Twitter API outputs millions of tweets, of which only verified accounts and popular tweets were taken into consideration (only 300k tweets)

2. Second, data munging and feature engineering were performed with Python and BigQuery. Important features were included: the Sentiment Score for each tweet was added and then an average per day is calculated. Finally, the training table is made with the join by day of the tweets sentiment per day and the Daily Bitcoin prices. 

3. Multiple ML models were performed to compare the prediction score metrics. Among them are ensemble models, linear models and decision tree models. Finally an approach of Random Forest was the best one. 


## Data Retrieval & Exploratory Data Analysis

For the data retrieval, two data sources are considered:

- *Twitter API:* For the twitter API some aspects were taken into consideration. The first of these was the amount of data to be retrieved. As Twitter has massive amounts of data, careful selection of it should be done. Only the most important tweets were taken into consideration (for example, only 21k users were analyzed). It was found that there are a large dispersion in the tweets number of likes and retweets. As the purpose of the project is to measure the impact of the sentiment towards Bitcoin price, only the most important were taken into consideration.

For this reason, only the most 10 popular tweets per day were considered for the analysis and for each of the tweets the sentiment analysis score was performed with the NLP API from GCP, which contains a restriction of calls per minute. The number 10 was selected because of both reasons, to measure only the most important tweets and because of the NLP API restriction (it was very expensive to perform Sentiment Analysis across all table). The NLP API score the tweets with 1 positive, -1 negative and 0 neutral. It also outputs a magnitude of the sentiment from 0 to infinite. These two variables are considered for the model

Some examples of the most popular tweets are from Elon Musk, MrBeast and Cashapp. For example: 'You can now buy a Tesla with Bitcoin' with acccounts more than 100k retweets

- *Bitcoin Price from Yahoo Finance API*:

The Bitcoin price can be explored as a time series variable:

<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg1_closing.png">

An important increase and decrease occurs during 2021, and also the Bitcoin price is an intra day volative measure, sometimes varying more than 10% in the price in one day:

<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg2_variation.png">


This shows us that there may be important factors that could contribute to Bitcoin price, but for now only the sentiment is analyzed. If we analyze this relation, we can notice that the linear correlation is almost zero, so linear models may not perform well:

<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg3_linearcor.png">

For this reason another family of models will be tested. 

## Data Engineering
- For the analysis some feature engineering was performed. The first was to encode the increase decrease of the Bitcoin as 1 (increase) and 0 (decrease). The main reason was that sentiment is only one of many factors that could lead to an increase or decrease, so for the project is easier to predict this binary variable instead of the closing price.

The second feature engineering was to aggregate per day the sentiment of the tweets. This can lead us to a table that contains one day per row, this registry contains the average sentiment in that day for the Bitcoin.

## Model training

For the trainig a train test split was performed. The test size was 20% of the table and the remaining the training set. The first model to be tested was Logistic Regression which achieves an accuracy of 0.49 which is a low accuracy considering that the benchmark is 0.54 (if we always outputs up). For this reason this model was not considered. After this, a logistic regression with regularization was performed, that also leads to a bad performance. We can conclude that linear models are not good for this problem. For the third model, Gradient Boosting Classifier, Random Forest Classifier and Voting Classifiers were attempted:

<center>

|**Model**|**Metric**|
|:---:|:---:|:---:|:---:|
| Voting Classifier |  0.54 | 
| Gradient Boosting Classifier | 0.56 | 
| Random Forest Classifier | 0.60 | 
    
</center>

From this table we can conclude that the model that beats the benchmark is the Random Forest Classifier. 

## References:
* [Sklearn linear regresion](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
* [Sentiment Analysis Tutorial Google](https://cloud.google.com/natural-language/docs/sentiment-tutorial)



