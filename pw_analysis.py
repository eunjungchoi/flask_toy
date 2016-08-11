import sklearn as sk
from sklearn import clone
from sklearn.ensemble import (RandomForestClassifier, ExtraTreesClassifier)
from sklearn.externals.six.moves import xrange
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn import svm
import pandas as pd

import csv

def pw_analysis(test_array):
	datafile = pd.read_csv("password_out.csv", header=0)

	n_classes = 2
	n_estimators = 30

	X = datafile.ix[:, 2:]
	y = datafile.ix[:, 1]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=1)
	model = RandomForestClassifier(n_estimators=n_estimators)

	clf = model.fit(X_train, y_train)

	y_pred = clf.predict(test_array)

	return y_pred
