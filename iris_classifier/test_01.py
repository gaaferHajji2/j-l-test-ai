import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt

data = datasets.load_iris()

data = pd.DataFrame(
    np.c_[data['data'], data['target']], columns=data['feature_names'] + ['Species'] # type: ignore
)

data['Species'] = data['Species'].astype(int)

print(data.head())

# Settings the color of palette to Greys
sns.displot(
    data, x='Species', discrete = True, hue='Species', shrink =0.8, palette='Greys'
)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(7, 7))
sns.boxplot(ax=axes[0, 0], data=data, x='Species', y = 'sepal length (cm)', hue='Species', palette='Greys')
sns.boxplot(ax=axes[0, 1], data=data, x='Species', y = 'petal length (cm)', hue='Species', palette='Greys')
sns.boxplot(ax=axes[1, 0], data=data, x='Species', y = 'sepal width (cm)', palette='Greys', hue='Species')
sns.boxplot(ax=axes[1,1], data = data,x='Species', y = 'petal width (cm)', palette='Greys', hue='Species')
plt.show()

# define x-y plot (pairplot)
sns.set_theme(
    rc={
        "axes.facecolor":"efefef",
        "figure.facecolor":"efefef"
    }
)

graphxy = sns.pairplot(data=data, hue="Species", palette="Greys")
graphxy.add_legend()
plt.show()

# Test the data
train_data, test_data = train_test_split(data, test_size=0.2, random_state=13)
print("The train_data is: ", train_data.shape)
print("The test_data is: ", test_data.shape)

# define the x-y training data for classification
x_training_data = train_data[[
    'sepal length (cm)', 'petal length (cm)', 
    'sepal width (cm)', 'petal width (cm)'
]]
print(x_training_data.head())

y_training_data = train_data[['Species']]
print(y_training_data.head())

# define the x-y testing data
x_testing_data = test_data[[
    'sepal length (cm)', 'petal length (cm)', 
    'sepal width (cm)', 'petal width (cm)'
]]
y_testing_data = test_data[['Species']]
print(x_testing_data.head())
print(y_testing_data.head())

# train and test the classifier
"""
XGBoost offers multiple evaluation metrics and can accept custom metrics as well. In addition to 
the AUC metric used here, there are over 20 options, including RMSE, mean absolute percentage 
error, and mean average precision.

auc: Area under the curve

A default metric is assigned based on whether the model is for prediction (the default is RMSE), 
classification (the default is logloss), or ranking (the default is map – mean average precision). 
"""
data_classifier = xgb.XGBClassifier(eval_metric='auc')
data_classifier.fit(
    x_training_data, y_training_data, 
    eval_set = [
        (x_testing_data, y_testing_data), 
        (x_training_data, y_training_data)
    ]
)

# check the results
t1 = data_classifier.predict(x_testing_data)
print(t1)

# test
t2 = np.array([4.2, 3.1, 1.2, 0.5])
t2 = t2.reshape(1, 4) # model expect array as 2-dimensio
t3 = data_classifier.predict(t2)
print(t3)
# make simple report
"""
precision = TP/(TP+FP), recall = TP/(TP+FN),  F1score = 2 ((precision ⋅ recall) / (precision + recall))
"""
print(classification_report(y_testing_data, t1))