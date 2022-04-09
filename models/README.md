# Machine Learning Model Training

The Machine Learning model training was developed in three steps that are depicted in the next image:

<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg4_diagram.png">

1. First, all the Twitter data and Yahoo Finance was retrieved from the Twitter API and the Yahoo Finance API. Although there were some restrictions, for the purpouse of the project it was possible to retrieve all the required data. 
- Some considerations were taken, for example, the volumetry of the Twitter API was millions of tweets, of which only verified accounts and popular tweets were taken into consideration (only 300k tweets)

2. Second, data munging and feature engineering were performed with python and bigquery. And in this steps some important features were included. For example, the Sentiment Score for each tweet was added and then an average per day is calculated. Finally, the training table is made with the join by day of the tweets sentiment per day and the Daily Bitcoin prices. 

3. Multiple ML models were performed to compare the prediction score metrics. Among them were ensemble models, linear models and decision tree models. Finally an approach of Random Forest was the best one. 


## Exploratory Data Analysis 

- Mini EDA: casi nada de relación, pequeña pendiente. Mini exploración del UPdown vs sentimiento
<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg1_closing.png">
<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg2_variation.png">
<img src="https://github.com/ro-juja/probable-umbrella/blob/main/images/gg3_linearcor.png">





## Data Retrieval
- Seleccionar los twitter más importantes, son los que tienen más reelevancia 
- Se envian a la API de sentimiento 600 por día. Sentimiento por día No saturar las APIs de sentimiento
## Data Engineering
- Datos de bitcoin (se crea de 0 o 1 si sube o baja)(sube 1, baja 0): Feature engineering (updown)
- Ese promedio se agrega a la base de bitcoin ()
- API de sentimiento (y uno de magnitud)
# Model training
- 3 modelos (regression lineal), 0.49
-  (el arbol y el random forest de .60)
# Vertex and cloud
- Después lo que se hizo con la nube
- Guardarlo en un bucket (gcp)
- Incluir el dockerfile ()
# Conclusions
- se tuvo exito?







