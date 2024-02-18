# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:50:07 2024

@author: charl
"""

import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import (StandardScaler, normalize)
import matplotlib.pyplot as plt


df = pd.read_csv("../MTG-ABC/data/winners.txt",sep="\t",header=0,low_memory=False)
df['wincount'] = df['winner'] * 1
agg_by_name = df[['deckname','deckcost','sidebarcost','wincount']].groupby('deckname')

agg_data = pd.DataFrame(agg_by_name.mean())

#agg_data.plot(x='deckcost',y='wincount',kind='scatter')
agg_data.mean()
agg_data.corr()

X = agg_data[(agg_data['wincount'] > 0) & (agg_data.wincount < 1)]['deckcost'].values.reshape(-1,1)
y = agg_data[(agg_data['wincount'] > 0) & (agg_data.wincount < 1)]['wincount'].values.reshape(-1,1)

X_norm = normalize(X,copy=False,return_norm=True)
X_train, X_test, y_train, y_test =  train_test_split(X_norm,y,test_size=0.3,random_state=42)

reg = linear_model.LinearRegression()

reg.fit(X_train,y_train)

y_pred = reg.predict(X_test)


mse = sk.metrics.mean_squared_error(y_test,y_pred)

print("MSE:", mse)

plt.scatter(X_test,y_test,color="blue")
plt.plot(X_test,y_pred,color="red",linewidth=3)
#plt.xticks(())
#plt.yticks(())
plt.show()

#KNN
n_neighbors = 5

for i, weights in enumerate(["uniform", "distance"]):
    knn = sk.neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X_train, y_train).predict(X_test)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, color="darkorange", label="data")
    plt.plot(X_test, y_, color="navy", label="prediction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.tight_layout()
plt.show()

