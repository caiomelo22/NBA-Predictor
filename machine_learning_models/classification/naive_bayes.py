# -*- coding: utf-8 -*-
"""Naive Bayes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13rNQtD1n9fIjiM50BHVBjczBb64MzjzQ
"""

import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import pandas as pd

" Importing the dataset "

dataset = pd.read_csv('../../data/seasons/winner/2000-2020.csv')
X = dataset.iloc[:, 4:-1].values
y = dataset.iloc[:, -1].values

" Splitting the dataset into the Training set and Test set "

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

" Feature Scaling "

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

" Training the model on the Training set "

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

" Predicting a new result "

# print(classifier.predict(sc.transform([[30,87000]])))

" Predicting the Test set results "

y_pred = classifier.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

" Cross Validation Score "

from sklearn.model_selection import cross_val_score

print("Predictions for the test set with the cross validation score")
crossValScores = cross_val_score(classifier, X_test, y_test)
print(mean(crossValScores), crossValScores)

" Making the Confusion Matrix "

from sklearn.metrics import confusion_matrix, accuracy_score
print("Predictions for the test set")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))