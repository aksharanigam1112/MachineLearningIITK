# 1) Cross Val Classification Accuracy

import pandas as pd
from sklearn.model_selection import KFold , cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values
x = array[:, 0:8]
y = array[:, 8]

model = LogisticRegression()
kfold = KFold(n_splits=10)

scoringMethod = 'accuracy'      # Classification Accuracy is default so even if we delete it, it will still
                                # cal classification accuracy

result = cross_val_score(model , x,y,cv=kfold , scoring=scoringMethod)

print("\nAccuracy = %.3f (%.3f) "%(result.mean()*100.0 , result.std()*100.0) )

