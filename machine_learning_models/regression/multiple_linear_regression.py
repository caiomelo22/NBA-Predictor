# -*- coding: utf-8 -*-
"""Multiple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D6a-WnlL7OP76nBIARsqRRDqLNMPC5x5
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import import_data_helper as idh

def multiple_linear_regression(season = '2018-2018'):
    " Importing the dataset "
    
    dataset, X, y, X_train, X_test, y_train, y_test = idh.import_data_regression(season)
    
    " Training the model on the Training set "
    
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    
    " Predicting the Test set results "
    
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred),2), y_test.reshape(len(y_test),2)),1))
    
    " Predicting a single game "
    
    # print(regressor.predict([[115.0, 114.3, 0.45280000000000004, 0.3868, 0.8552, 42.0, 11.1, 6.1, 0.6, 1525.012443981673, 117.5, 114.1, 0.48050000000000004, 0.4142, 0.7729000000000001, 48.2, 16.5, 4.4, 0.7, 1611.0511901230773]]))
    
    " Evaluating the Model Performance "
    
    from sklearn.metrics import r2_score, mean_squared_error
    # print("Model R2 Score and error")
    r2Score = r2_score(y_test, y_pred)
    m2e = mean_squared_error(y_test, y_pred)
    # print(r2Score)
    # print(m2e)
    
    return r2Score, m2e, regressor
    
    
if __name__ == "__main__":
    multiple_linear_regression()
