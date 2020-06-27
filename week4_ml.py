# -*- coding: utf-8 -*-
"""week4_ml.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16tmRVvJCHitW8pJ8tjACs53yJQuTQh_U

**Naive Bayes Theorem**

Gaussian Model
"""

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_wine
from sklearn.metrics import precision_recall_curve
import pandas as pd

wine = load_wine()
x = wine.data
y = wine.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0)

gas = GaussianNB().fit(x_train, y_train)

print("Train", gas.score(x_train, y_train))
print("Test", gas.score(x_test, y_test))

"""Random Forest vs"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer

f = load_breast_cancer()
x = f.data
y = f.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0)
forest = RandomForestClassifier(n_estimators=22, random_state=0).fit(x_train, y_train)

print("Random Forest")
print("Test", forest.score(x_test,y_test))
print("Train", forest.score(x_train, y_train))

from sklearn.tree import DecisionTreeClassifier
des = DecisionTreeClassifier().fit(x_train, y_train)

print("Decision Tree")
print("Test", des.score(x_test,y_test))
print("Train", des.score(x_train, y_train))