# 3) Cross validation Area under ROC curve

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
scoringMethod = 'roc_auc'   # Finding accuracy on the majority of the data (6Sigma)

result = cross_val_score(model , x,y,cv=kfold , scoring=scoringMethod)

print("\nAUC = %.3f (%.3f) "%(result.mean()*100.0, result.std()) )   # Loss is always b/w 0 & 1