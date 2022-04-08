import pandas as pd 
import numpy as np 
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import cross_validate
from sklearn.metrics import precision_score,log_loss


data_bitcoin = pd.read_csv('../data/clean_model.csv')


X=data_bitcoin.iloc[:, 9:11]
Y=data_bitcoin['up_down']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

RFC = RandomForestClassifier(n_estimators=1000, min_samples_split=2)

print("Exito")