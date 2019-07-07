# 3. Leave one out

import pandas as pd
from sklearn.model_selection import LeaveOneOut, cross_val_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values
x = array[:, 0:8]
y = array[:, 8]

loocv = LeaveOneOut()
model = LogisticRegression()
result = cross_val_score(model , x,y,cv=loocv)

print("\nResult = \n",result)
print("\nResult Size = ",result.size)
print("\nSum of Positive results : %i"%(result.sum()))
print("\nAccuracy = %.2f %%"%(result.sum()*100/result.size))        # or simply use result.mean()*100.0

