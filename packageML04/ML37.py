# 2. k-fold cross validation

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

num_folds = 10
#seed = 7
kfold = KFold(n_splits=num_folds)
result = cross_val_score(model , x,y,cv=kfold)      # Technique to cal accuracy kfold will devide the data into
                                                # 10 parts will train & test
print("\nResult = \n",result)
print("\nAcuuracy = %.3f %%"%(result.mean()*100.0))
print("\nStandard Deviation = %.3f"%(result.std()*100.0))
