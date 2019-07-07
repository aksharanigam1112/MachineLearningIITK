# 1. Train & Test set split

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values
x = array[:, 0:8]
y = array[:, 8]

test_data_size = 0.33
seed = 4               # it restricts the fluctuation, bt it will be diff for diff nos. passed to the seed

# Pass the i/p o/p and test karne ke liye kitna hide karna hai test-size tells that
xtrain, xtest, ytrain , ytest = train_test_split(x,y,test_size=test_data_size, random_state=seed )


model = LogisticRegression()
model.fit(xtrain , ytrain)      # We get best fit from xtrain & ytrain

result = model.score(xtest , ytest)     # matching the ans with the predicted ans

print("\nAccuracy = %f %%"%(result*100))