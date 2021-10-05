# -*- coding: utf-8 -*-
"""LSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19NQOKEK4GUOpMOh9TDJ6NXjyNVafDuXI
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import keras

" Importing the dataset "

dataset = pd.read_csv('../../data/seasons/score/2010-2018.csv')
X = dataset.iloc[:, 4:-2].values
y = dataset.iloc[:, -2:].values

" Splitting the dataset into the Training set and Test set "

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
X_test, X_validation, y_test, y_validation = train_test_split(X_test, y_test, test_size=0.2)

" Feature Scaling "

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
X_validation = sc.transform(X_validation)

" Building the LSTM "

X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))
X_validation = np.reshape(X_validation, (X_validation.shape[0], 1, X_validation.shape[1]))

input_shape = (len(X_train), len(dataset.iloc[:, 4:-2].columns)) 

lstm = keras.Sequential()
lstm.add(keras.layers.LSTM(68, input_shape=input_shape, return_sequences=False))

# Output layer
lstm.add(tf.keras.layers.Dense(units=2))

" Compiling the LSTM "
optimiser = tf.keras.optimizers.Adam(learning_rate=0.0001)
lstm.compile(optimizer=optimiser,
              loss='mean_squared_error')
lstm.summary()

" Training the LSTM on the Training set "

history = lstm.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size = 32, epochs = 100)

" Predicting single result "

# print(lstm.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)

" Predicting results for all data"

y_pred = lstm.predict(X_validation)

" Evaluating the Model Performance "

from sklearn.metrics import r2_score, mean_squared_error
print("Model R2 Score and error")
print(r2_score(y_validation, y_pred))
print(mean_squared_error(y_validation, y_pred))