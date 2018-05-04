# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:01:04 2018

@author: divyanshu
"""
import pickle

dataset = pickle.load( open( "dataset.pickle", "rb" ) )
from sklearn.model_selection import train_test_split
features = dataset['features']
labels = dataset['labels']
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)
features_train, features_val, labels_train, labels_val = train_test_split(features_train, labels_train, test_size=0.40, random_state=42)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors = 3)
clf.fit(features_train, labels_train)