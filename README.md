# Probable-Umbrella ☂

![](images/data_rain.gif)

Team members:

|**Name**|**Email**|**CU**|**Github handler**| 
|:---:|:---:|:---:|:---:|
| Victor Erasto Rivera | victor.rivera.gonzalez@gmail.com| 97105 | [@vviiccttoorr](https://github.com/vviiccttoorr)| 
| Alejandro Muñoz | alex.monfis@gmail.com | 203021 | [@Monfiz](https://github.com/Monfiz) | 
| Juan Humberto Escalona| jh.escalona.s@gmail.com | 203131 | [@Juanes8](https://github.com/Juanes8)| 
| Salvador García  | savrgg@gmail.com | 119718 | [@savrgg](https://github.com/savrgg) | 
| Rodrigo Juárez | rodrigo.juarezjaramillo@gmail.com | 145804 | [@ro-juja](https://github.com/ro-juja)| 

## Why are we an awesome team?

We are a multidisciplinary team (honestly, we have never met in person) capable of solving any given task thanks to our different perspectives (well, just perspectives from engineers and economists). Here is a sneak peek form us.
- Victor, Economist and Social Scientist with experience on public policy
- Alejandro Muñoz, Engineer in physics and Communicator of science, good at explaining and exploring ideas.  
- Juan Escalona, Mechanical and Electrical engineer with sales experience, customer driven and a Machine Learning enthusiast.
- Salvador García, Applied Mathematics with experience in Data Science
- Rodrigo Juárez, Business Engineer with a strong analytical and financial education.

All of us are currently pursuing a Master's degree on Data Science at ITAM.  🎓 

## Project Description
### **1. Objectives**

1. What is the problem that your Data Product  will solve?

Cryptocurrency prices heavily depend on the demand side of the market. The beliefs and expectations on prices make this market highly volatile. There are complications to aggregate beliefs and expectations of the market on cryptocurrency prices.

The problem we want to solve is the extraction of positive or negative sentiments from beliefs and expectations. This is very important for investment decision-making by traders, portfolio managers, and investors. Sentiment analysis models can provide an efficient method for extracting actionable signals. However, financial sentiment analysis is challenging due to domain-specific language and unavailability of large labeled datasets.

Our Data Product will predict cryptocurrencies prices, based on past and current prices movements, our model will take in count a general sentiment analysis, based on the latest news posted on Twitter.


2. If a company was to use this application, what would be their ML objectives and business objectives?

Machine Learning objectives:
We are planning to make a Sentiment Analysis and Neuronal Network to predict Bitcoin prices. Sentiment Analysis will be used in order to predict the confidence of the newspapers' headlines and people's tweets. 

Business objectives:
Our business plan is to develop a unique tool in the market with the most sophisticated technology in order to support all the financial stakeholders' decision-making. We want to make a powerful tool to bear the financial investment risk. As a starting point, we are going to predict Bitcoin's price, but our goal is to be able to predict the price of commodities, shares, etc. 

### **2. Users**

1. Who will be the users of your application?

Bitcoin investors in general and financial rating companies, such as Moddys, S&P, and Fitch. 

2. How are users going to interact with your application?

Users will make queries to our application about our prices forecasts.

### **3. Data Product Architecture  Diagram**

![](https://i.imgur.com/URvdJK6.png)


### **4. Data**

a. Where would you get your data from? How much data would you need? Is there anything publicly available or do you need to build your own dataset?

We will use YahooFinance API and Twitter's API in order to feed our model. We are planning to use only publicly available data for stakeholders. ALso we will make use of o track idividual prices of different coins.  

We will use 1 million tweets to train our model, which will be data from the last months of 2020 up today. For the bitcoin price forecast, we will use the data for this same period. 

[Coin market API](https://coinmarketcap.com/api/documentation/v1/)
[Yahoo Finance API](https://www.yahoofinanceapi.com/)
[Twitter API](https://developer.twitter.com/)

### **5. Modeling**

1. What types of models/architectures will you be using for this application? Which ones would you start with?

Our goal is to predict  bitcoin value, so we are facing a regression problem where we try to make a numeric prediction based on sentiment analisys of tweets related to bitcoin. So, some models that could manage to work well could be:

* Random forest
* Neural Network
* Regression with some Lasso or Ridge penalization

Random forest and neural networks adapt well to nonlinear behavior that could be found on the data. But as we start retrieving data and doing the EDA process, we will probably update or change these proposals. 

2. You’re free to train a model from scratch or use a pretrained model.

We are planning to use a pretrained model of Sentiment Analysis from [Hugging Face](https://huggingface.co/sagorsarker/codeswitch-spaeng-sentiment-analysis-lince) and [Custom sentiment analysis](https://cloud.google.com/natural-language#section-6) that is part of Google Natural Language API.


### **6. Evaluation**

1. How would you evaluate your model performance, both during training and inference?

As we said before this is a regression problem, so we will use metrics as mse(mean squared error), mae(mean absolute error), r squared to evaluate the performance of our model. 

2. How would you evaluate whether your application satisfies its objectives?

To be honest this relationship between the tweet’s sentiments and the price of coins is merely speculative from us. There may not be any relationship between them, and we may face the case that our models will perform poorly. So, our definition of success will be to portray honestly the relationship of the data. We may find a strong correlation, softer or none at all. It is an experiment, and anything can happen.


### **7. Inference**

1. Will you be doing online prediction or batch prediction or a combination of both?

We will be doing batch prediction, as we will retrieve the most relavant tweets of day to make our predictions. 

3. Will the inference run on-device or through a server?

The inference will run through a server. 

5. Can you run inference on CPUs or an edge device or do you need GPUs?

We plan to run it on CPUs. 

### **8. Compute**

1. How much compute do you need to develop this application as a market-ready product?
    1. To train your model (if you train your own model): do you need GPUs/TPUs or just CPUs? How many machines? For how long?
    It will depend on the model we will put to work. Maybe we find the problem can be solved using linear regression, and there is no need for GPUs and tons of computational power like with a neural network, or maybe the data requires that computational help. 
    
    3. To serve your model: can your models make predictions on CPUs?
    Probably yes, but again we will decide after exploring the data.
    
2. How much compute do you need to develop this application for this project?

We are planning to work with a Data Base of approximately 1,000,000 tweets. Also, the historical data of the past two years Bitcoin's price. 

We are estimating a memory usage in BigQuery of approx: 
1000,000 tweets = 170 Mb
Yahoo Finance Data Base of approx 100 Mb


4. Feel free to reference machine cost on AWS/GCP to get an estimate of compute cost.

According to [NetApp](https://cloud.netapp.com/blog/google-cloud-pricing-vs-aws-a-fair-comparison-gcp-aws-cvo-blg), the estimation price per hour used on Google Cloud is $0.813. 
    
### **9. MVP**

1. What would the MVP be?

Our main goal would be to predict Bitcoin's price, but the MVP would be a daily prediction of price increases or decreases of bitcoin based on historical data and sentiment analysis.


2. How difficult is it to get there?

The main difficulty would be to find a relationshing among the tweets and the price of bitcoin.  

### **10. Pre-mortems**

- What are the risky aspects of the project? i. e.g. not enough data, limited compute resources, not knowing how to implement an interface, network latency, inference latency, etc.

The risk we are facing on this project first is not to find a relationship between the tweets and the price of bitcoin. We still do not know if the compute resources we have are going to be enough to do the analysis we plan. 

- What are the limitations of your application?

Our application will only be able to predict whether the price will increase or decrease based on the tweets of the day. It won't be able to predict the exact price of the day.    

- What are the potential biases of your application?

The main bias for our application is that we are only going to use tweets in English. Perhaps there is a stronger relationship with another language than with English that we won't be able to notice.
