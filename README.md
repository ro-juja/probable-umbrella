# Cryptomaniatics

  <img width="400" height="400" src="https://github.com/ro-juja/probable-umbrella/blob/ca82415746efb7da244d8d6236340324158a555d/images/crypto.gif">


<center>

|**Name**|**Email**|**CU**|**Github handler**| 
|:---:|:---:|:---:|:---:|
| Victor Erasto Rivera | victor.rivera.gonzalez@gmail.com| 97105 | [@vviiccttoorr](https://github.com/vviiccttoorr)| 
| Alejandro Muñoz | alex.monfis@gmail.com | 203021 | [@Monfiz](https://github.com/Monfiz) | 
| Juan Humberto Escalona| jh.escalona.s@gmail.com | 203131 | [@Juanes8](https://github.com/Juanes8)| 
| Salvador García  | savrgg@gmail.com | 119718 | [@savrgg](https://github.com/savrgg) | 
| Rodrigo Juárez | rodrigo.juarezjaramillo@gmail.com | 145804 | [@ro-juja](https://github.com/ro-juja)| 
    
</center>

## About us:

We are a multidisciplinary team (honestly, we have never met in person) capable of solving any given task thanks to our different perspectives (well, just perspectives from engineers and economists). Here is a sneak peek form us.
- Victor, Economist and Social Scientist with experience on public policy
- Alejandro Muñoz, Engineer in physics and Communicator of science, good at explaining and exploring ideas.  
- Juan Escalona, Mechanical and Electrical engineer with sales experience, customer driven and a Machine Learning enthusiast.
- Salvador García, Applied Mathematics with experience in Data Science
- Rodrigo Juárez, Business Engineer with a strong analytical and financial education.

All of us are currently pursuing a Master's degree on Data Science at ITAM.  🎓 

## Project Description
### **Objectives**

Cryptocurrency prices heavily depend on the demand side of the market. The beliefs and expectations on prices make this market highly volatile. There are complications to aggregate beliefs and expectations of the market on cryptocurrency prices.

The problem we want to solve is the extraction of positive or negative sentiments from beliefs and expectations. This is very important for investment decision-making by traders, portfolio managers, and investors. Sentiment analysis models can provide an efficient method for extracting actionable signals. However, financial sentiment analysis is challenging due to domain-specific language and unavailability of large labeled datasets.

Our Data Product will predict cryptocurrencies prices, based on past and current prices movements, our model will take in count a general sentiment analysis, based on the latest news posted on Twitter.

In order to solve the problem we had discussed before, we are planning to make a Sentiment Analysis and Neuronal Network to predict Bitcoin prices. Sentiment Analysis will be used in order to predict the confidence of the newspapers' headlines and people's tweets.  

Of course, our main goal is to help the society with our work, so we are planning to develop a unique tool in the market with the most sophisticated technology in order to support all the financial stakeholders' decision-making. We want to make a powerful tool to bear the financial investment risk. As a starting point, we are going to predict Bitcoin's price, but our goal is to be able to predict the price of commodities, shares, etc. 

Society, as a whole, will benefit from our work, however, the channels through which we hope it will be positively affected are:

Bitcoin investors in general and financial rating companies, such as Moddys, S&P, and Fitch, making queries to our application about our prices forecasts.


### **Our Product Architecture  Diagram looks like this:**

![](https://i.imgur.com/URvdJK6.png)


So that our users trust our platform, we will explain what data we will use to carry out our project:
We will use YahooFinance API and Twitter's API in order to feed our model. We are planning to use only publicly available data for stakeholders. ALso we will make use of o track idividual prices of different coins. We will use 10,000 tweets to train our model, which will be data from the last months of 2020 up today. For the bitcoin price forecast, we will use the data for this same period. 

Our Data sources are public and available to everyone. If you want to investigate more about the origin, we leave you the following hyperlinks:

[Coin market API](https://coinmarketcap.com/api/documentation/v1/)
[Yahoo Finance API](https://www.yahoofinanceapi.com/)
[Twitter API](https://developer.twitter.com/)

### **Modeling**

Our goal is to predict  bitcoin value, so we are facing a regression problem where we try to make a numeric prediction based on sentiment analisys of tweets related to bitcoin. So, some models that could manage to work well could be:

* Random forest
* Neural Network
* Regression with some Lasso or Ridge penalization

Random forest and neural networks adapt well to nonlinear behavior that could be found on the data. But as we start retrieving data and doing the EDA process, we will probably update or change these proposals. 

We are planning to use a pretrained model of Sentiment Analysis from [Hugging Face](https://huggingface.co/sagorsarker/codeswitch-spaeng-sentiment-analysis-lince) and [Custom sentiment analysis](https://cloud.google.com/natural-language#section-6) that is part of Google Natural Language API.


### **Evaluation**

As we said before this is a regression problem, so we will use metrics as mse(mean squared error), mae(mean absolute error), r squared to evaluate the performance of our model. The tweet’s sentiments and the price of coins is merely speculative from us. There may not be any relationship between them, and we may face the case that our models will perform poorly. So, our definition of success will be to portray honestly the relationship of the data. We may find a strong correlation, softer or none at all. It is an experiment, and anything can happen.


We will be doing batch prediction, as we will retrieve the most relavant tweets of day to make our predictions. We are planning to run  inference on CPUs,  through a server..To train our model, we are planning to use linear regression, and there is no need for GPUs and tons of computational power like with a neural network, or maybe the data requires that computational help. Our model might be able to  make predictions on CPU, but, again, we will decide after exploring the data.
    

We are planning to work with a Data Base of approximately 10,000 tweets. Also, the historical data of the past two years Bitcoin's price. 

We are estimating a memory usage in BigQuery of approx: 
10,000 tweets = 17 Mb
Yahoo Finance Data Base of approx 100 Mb

According to [NetApp](https://cloud.netapp.com/blog/google-cloud-pricing-vs-aws-a-fair-comparison-gcp-aws-cvo-blg), the estimation price per hour used on Google Cloud is $0.813. Which is the platform we are planning to use. 
    

Our main goal would be to predict Bitcoin's price, but the MVP would be a daily prediction of price increases or decreases of bitcoin based on historical data and sentiment analysis. The main difficulty would be to find a relationshing among the tweets and the price of bitcoin.  

### **Pre-mortems**

Handling this project, we are exposed to certain risks, the risk we are facing on this project first is not to find a relationship between the tweets and the price of bitcoin. We still do not know if the compute resources we have are going to be enough to do the analysis we plan. 

Our application will only be able to predict whether the price will increase or decrease based on the tweets of the day. It won't be able to predict the exact price of the day.    

The main bias for our application is that we are only going to use tweets in English. Perhaps there is a stronger relationship with another language than with English that we won't be able to notice.
