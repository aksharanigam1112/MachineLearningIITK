import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
import warnings

warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values
x = array[:, 0:8]
y = array[:, 8]

kfold = KFold(n_splits=10, random_state=7)

# 1) Spot check for Logistic Regression
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
result = cross_val_score(model, x, y, cv=kfold)
print("\nValidation Score for Logistic Regression : ", result.mean())

# 2) Spot check for Linear Discriminant Analysis (LDA)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

model = LinearDiscriminantAnalysis()
result = cross_val_score(model, x, y, cv=kfold)
print("\nValidation Score for LDA : ", result.mean())

# 3) Spot check for k-Nearest Neighbours(KNN)
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
result = cross_val_score(model, x, y, cv=kfold)
print("\nValidation Score for KNN : ", result.mean())

# 4) Spot check for Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
result = cross_val_score(model, x, y, cv=kfold)
print("\nValidation Score for GaussianNB : ", result.mean())

# 5) Spot check for Classification & Regression Trees
# CART or just decision trees construct a binary tree from the training data
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
result = cross_val_score(model, x, y, cv=kfold)
print("\nValidation Score for CART Decision Tree: ", result.mean())

# 6) Spot check for Support Vector Machine(SVM)
# SVM seek a line that best separates two classes.
# Those data instances that are close to the line that
# best separates the classes are called support vectors
# and influence where the line is placed
from sklearn.svm import SVC

model = SVC()
result = cross_val_score(model, x, y, cv=kfold)
print("\nValidation Score for SVM : ", result.mean())
