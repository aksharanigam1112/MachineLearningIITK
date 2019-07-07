# Repeated train test

import pandas as pd
from sklearn.model_selection import ShuffleSplit , cross_val_score
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
no_of_repetitions = 10
#seed = 7

shufflesplit = ShuffleSplit(n_splits=no_of_repetitions , test_size=test_data_size)

model = LogisticRegression()
result = cross_val_score(model,x,y,cv=shufflesplit)
print("\nResult = \n",result)
print("\nAccuracy = %.3f %%"%(result.mean()*100.0))
print("\nStd Dev = %.3f "%(result.std()*100))
