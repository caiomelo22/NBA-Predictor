# -*- coding: utf-8 -*-
"""Artificial Neural Network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aqQOyHl0GlK3nd_XP5EteZq_md234cat
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
import os.path

def ann_regression(season = '2018-2018'):

    " Importing the dataset "
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, '../../data/seasons/score/{}.csv'.format(season))
    dataset = pd.read_csv(path)
    X = dataset.iloc[:, 5:-2].values
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
    
    " Building the ANN "
    
    ann = keras.Sequential([
    
        # input layer
        tf.keras.layers.Dense(units=32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.9),
    
        # 1st dense layer
        tf.keras.layers.Dense(units=32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.9),
        
        # 2nd dense layer
        tf.keras.layers.Dense(units=32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        keras.layers.Dropout(0.9),
        
        tf.keras.layers.Dense(units=2)
    ])
    
    " Compiling the ANN "
    
    ann.compile(optimizer = 'adam', loss = 'mean_squared_error')
    
    " Training the ANN on the Training set "
    
    history = ann.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size = 32, epochs = 100)
    
    " Predicting single result "
    
    # print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)
    
    " Predicting results "
    
    y_pred = ann.predict(X_validation)
    # np.set_printoptions(precision=2)
    # print(y_pred)
    
    " Evaluating the Model Performance "
    
    from sklearn.metrics import r2_score, mean_squared_error
    # print("Model R2 Score and error")
    r2Score = r2_score(y_validation, y_pred)
    m2e = mean_squared_error(y_validation, y_pred)
    # print(r2Score)
    # print(m2e)
    
    return r2Score, m2e
    
    
if __name__ == "__main__":
    ann_regression()