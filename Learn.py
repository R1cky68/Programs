# This program takes in user input data (feature vectors) and examines the relationship to the output classes, which it can use to predict patterns with new datasets
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# First section here is about training the model by feeding it this dataset

X = [[1, 2, 3], [4, 5, 6], [23, 52, 68], [32, 255, 526], [141, 1513, 1244], 
     [1515, 76363, 252726], [15315, 15137, 34773], 
     [1241, 1415, 1512], [5135, 1631, 7175], 
     [1422, 9889, 7562], [1241, 1515, 15135], 
     [1241, 531515, 15155], [124124, 98797, 65773]]
y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]

y = np.array(y).reshape(-1, 1)

clf = RandomForestClassifier(random_state=0)
scores = cross_val_score(clf, X, y, cv=7)
clf.fit(X, y)

# Second section is creating new variables and datasets which the model can predict stuff about, based on previous data and how the model was fitted
XPredictions = clf.predict(X)
print("This is the predicted data for X: ", XPredictions)

new_data = [[22, 23, 24], [36, 37, 38]]
NewPredictions = clf.predict(new_data)
print("This is the new prediction data: ", NewPredictions)

# This section judges the accuracy of the dataset and keeps a score for it
print("Accuracy: ", scores)
print("Average accuracy", scores.mean())
