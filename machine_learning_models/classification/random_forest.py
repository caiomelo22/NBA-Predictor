# -*- coding: utf-8 -*-
"""Random Forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EpWKqumrQ-O9IhL-QVqg2kW1pRhif6dl
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
import import_data_helper as idh

def random_forest(season = '2018-2018', no_test = False):
    " Importing the dataset "
    
    dataset, X, y, X_train, X_test, y_train, y_test = idh.import_data_classification(season)
    
    " Training the model on the Training set "
    
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import RandomizedSearchCV
    
    # Prameters achieved by running the Random Search CV Optmizer code below
    classifier = RandomForestClassifier(n_estimators = 1000, min_samples_leaf=2, min_samples_split=5, max_features='sqrt', 
                                        max_depth=10, bootstrap = True, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, y_train.ravel())
    
    # " Random Search CV Optmizer "
    # # Number of trees in random forest
    # n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
    # # Number of features to consider at every split
    # max_features = ['auto', 'sqrt']
    # # Maximum number of levels in tree
    # max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
    # max_depth.append(None)
    # # Minimum number of samples required to split a node
    # min_samples_split = [2, 5, 10]
    # # Minimum number of samples required at each leaf node
    # min_samples_leaf = [1, 2, 4]
    # # Method of selecting samples for training each tree
    # bootstrap = [True, False]
    # # Create the random grid
    # random_grid = {'n_estimators': n_estimators,
    #                 'max_features': max_features,
    #                 'max_depth': max_depth,
    #                 'min_samples_split': min_samples_split,
    #                 'min_samples_leaf': min_samples_leaf,
    #                 'bootstrap': bootstrap}
                   
    # rf_random = RandomizedSearchCV(estimator = classifier, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
    
    # rf_random.fit(X_train, y_train)
    
    # best_random = rf_random.best_estimator_
    # best_parameters = rf_random.cv_results_
    # print(best_parameters)
    # print(best_random)
    # predictions = best_random.predict(X_test)
    # cm = confusion_matrix(y_test, predictions)
    # print(cm)
    # accuracy_score(y_test, predictions)
    
    # """Feature Importance"""
    
    # from sklearn.ensemble import ExtraTreesClassifier
    # print("Feature importance")
    feat_importances = pd.Series(classifier.feature_importances_, index=dataset.iloc[:, 5:-1].columns)
    feat_importances.nlargest(30).plot(kind='barh')
    title = 'Feature Importance'
    plt.ylabel('Features')
    plt.xlabel("Feature Importance")
    plt.title(title)
    plt.savefig('{}.png'.format(title.replace(' ','_').lower()), dpi=300)
    plt.show()
    
    # " Feature Correlation "
    
    # import seaborn as sns
    
    # dependent_variables_a = dataset.iloc[:,4:18]
    # corrmat_a = dependent_variables_a.corr()
    # top_corr_features_a = corrmat_a.index
    # plt.figure(figsize=(13,13))
    # #plot heat map
    # g=sns.heatmap(dependent_variables_a.corr(),annot=True,cmap="RdYlGn")
    
    # dependent_variables_b = dataset.iloc[:,18:-1]
    # corrmat_b = dependent_variables_b.corr()
    # top_corr_features_b = corrmat_b.index
    # plt.figure(figsize=(13,13))
    # #plot heat map
    # g=sns.heatmap(dependent_variables_b.corr(),annot=True,cmap="RdYlGn")
    
    " Predicting a new result "
    
    # print('CHA x DEN', classifier.predict_proba(sc.transform([[109.9, 109.8, 0.45630000000000004, 0.3693, 0.6975, 44.1, 12.7, 5.7, 0.4852941176470588, 0.4, 1453.4539592152416, -1, 113.2, 109.9, 0.47219999999999995, 0.34249999999999997, 0.8288999999999997, 42.4, 13.2, 5.5, 0.6470588235294118, 0.8, 1622.89716558378, -2]])))
    # print('DET x MIN', classifier.predict_proba(sc.transform([[102.1, 107.3, 0.4635000000000001, 0.3419, 0.6912999999999999, 44.2, 14.9, 5.6, 0.2898550724637681, 0.1, 1383.6380085968874, -2, 121.6, 116.5, 0.4859, 0.3638, 0.7134999999999999, 47.4, 14.4, 5.0, 0.3088235294117647, 0.6, 1406.9521244180135, 1]])))
    # print('TOR x LAC', classifier.predict_proba(sc.transform([[109.4, 112.1, 0.4474, 0.3677, 0.7647, 42.5, 12.0, 4.2, 0.39705882352941174, 0.2, 1472.0215044626073, -3, 109.4, 106.5, 0.4689, 0.3974, 0.8352, 44.6, 14.5, 3.3, 0.6617647058823529, 0.8, 1638.7949682476099, -1]])))
    # print('BOS x MIA', classifier.predict_proba(sc.transform([[115.9, 116.6, 0.45499999999999996, 0.37489999999999996, 0.8012, 45.9, 15.3, 5.8, 0.5147058823529411, 0.6, 1518.3317265330202, -2, 114.3, 110.8, 0.493, 0.3793, 0.8304, 38.3, 10.9, 2.6, 0.5441176470588235, 0.7, 1535.5451820677981, 2]])))
    # print('MEM x DAL', classifier.predict_proba(sc.transform([[109.2, 112.3, 0.4403, 0.3324, 0.7484, 49.4, 13.8, 7.7, 0.5147058823529411, 0.5, 1528.5880036844899, 2, 116.0, 105.8, 0.48949999999999994, 0.3881, 0.7643999999999999, 43.4, 12.8, 3.9, 0.5882352941176471, 0.6, 1592.071212115205, 4]])))
    # print('IND x PHI', classifier.predict_proba(sc.transform([[123.3, 119.8, 0.5044000000000001, 0.396, 0.8138, 44.1, 13.6, 7.7, 0.47058823529411764, 0.7, 1474.198522227209, 1, 116.6, 106.4, 0.48810000000000003, 0.38409999999999994, 0.7738999999999999, 44.6, 13.3, 6.1, 0.6911764705882353, 0.7, 1642.0676841322731, 8]])))
    # print('CHI x BKN', classifier.predict_proba(sc.transform([[105.1, 102.8, 0.46869999999999995, 0.358, 0.7369000000000001, 46.6, 14.1, 3.4, 0.4264705882352941, 0.4, 1481.7323289280403, 3, 116.1, 115.4, 0.47539999999999993, 0.3922, 0.8439, 45.2, 12.7, 4.7, 0.6470588235294118, 0.8, 1582.8343413358632, 1]])))
    # print('MIL x ORL', classifier.predict_proba(sc.transform([[123.6, 119.5, 0.5011, 0.3762, 0.7584, 46.5, 13.6, 5.4, 0.6323529411764706, 0.5, 1601.562206599367, -1, 103.4, 118.1, 0.4217000000000001, 0.33549999999999996, 0.7750000000000001, 44.6, 12.0, 5.2, 0.3088235294117647, 0.1, 1306.8775630320504, -3]])))
    # print('GSW x PHX', classifier.predict_proba(sc.transform([[116.4, 108.2, 0.487, 0.39320000000000005, 0.7826000000000001, 45.4, 15.3, 5.1, 0.5217391304347826, 0.5, 1523.24240665872, 3, 115.1, 113.9, 0.49260000000000004, 0.36479999999999996, 0.8422000000000001, 40.1, 11.2, 5.2, 0.7058823529411765, 0.9, 1625.7685114254296, -1]])))
    # print('LAL x NYK', classifier.predict_proba(sc.transform([[105.5, 109.6, 0.45490000000000014, 0.3389, 0.7090000000000001, 42.0, 14.1, 6.1, 0.5588235294117647, 0.3, 1533.0816400885722, 1, 113.7, 108.1, 0.4891, 0.4471, 0.8347999999999999, 41.9, 12.0, 5.1, 0.5588235294117647, 0.8, 1585.6510310862843, 1]])))
    # print('SAC x OKC', classifier.predict_proba(sc.transform([[111.7, 111.0, 0.49499999999999994, 0.381, 0.7786, 39.8, 14.8, 5.5, 0.4411764705882353, 0.5, 1454.69152221966, 1, 101.9, 123.2, 0.41229999999999994, 0.2972, 0.6943999999999999, 45.2, 17.2, 3.1, 0.30434782608695654, 0, 1253.1531691380874, -7]])))
    
    " Predicting the Test set results and"
    " Making the Confusion Matrix "
    from sklearn.metrics import confusion_matrix, accuracy_score
    cm = None
    acc_score = None
    
    if not no_test:
        y_pred = classifier.predict(X_test)
        cm = confusion_matrix(y_test.ravel(), y_pred.ravel())
        acc_score = accuracy_score(y_test, y_pred)
    
    return cm, acc_score, classifier
    

if __name__ == "__main__":
    random_forest()

