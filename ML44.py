# 4) Cross Val Confusion Matrix

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values
x = array[:, 0:8]
y = array[:, 8]

test_size =0.33
seed = 7

xtrain, xtest, ytrain , ytest = train_test_split(x,y,test_size=test_size, random_state=seed )

model = LogisticRegression()
model.fit(xtrain , ytrain)          # from 67% training data we calculate best fit hypothesis para

predicted = model.predict(xtest)    # trained algo is tested for 33%
matrix = confusion_matrix(ytest , predicted)    # y and y' is passed

print("\nMatrix = \n",matrix)        # the sum of the matrix values is equal to the 33% of 768(total rows)