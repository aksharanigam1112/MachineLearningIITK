# Recursive Feature Elimination

import pandas as pd
from sklearn.feature_selection import RFE               # RFE is algo specific
from sklearn.linear_model import LogisticRegression     # since o/p was discrete
import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values

x = array[:, 0:8]
y = array[:, 8]

model = LogisticRegression()
rfe = RFE(model,3)      # Use rfe for Logistic reg to select best 3 col
fit = rfe.fit(x,y)      # cols will be allocated ranking
result = fit.transform(x)

print("Num Feature : ", fit.n_features_)
print("Selected Feature : ",fit.support_)
print("Feature Ranking : ",fit.ranking_)
print("\n\n",result[:30 , :])