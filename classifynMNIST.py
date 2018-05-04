# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:01:04 2018

@author: divyanshu
"""
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(categorical_features = [0], sparse = False)
dataset = pickle.load(open("dataset.pickle", "rb"))
labels_list = dataset['labels']
features_list = dataset['features']
le = sklearn.preprocessing.LabelEncoder()
labels_list = le.fit_transform(labels_list)
new_cat_features = labels_list.reshape(-1, 1)
labels_list = enc.fit_transform(new_cat_features)
features  = np.array(features_list, 'float64')
labels  = np.array(labels_list, 'float64')
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)
features_train, features_val, labels_train, labels_val = train_test_split(features_train, labels_train, test_size=0.40, random_state=42)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors = 3)
from sklearn.model_selection import cross_val_score
cross_score = cross_val_score(clf, features_train, labels_train)
cross_score = (cross_score[0] + cross_score[1] + cross_score[2])/3 
clf.fit(features_train, labels_train)
X = clf.predict(features_test)
X_train = clf.predict(features_train)
acc_train = clf.score(features_train, labels_train)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test.max(axis=1), X.max(axis=1))