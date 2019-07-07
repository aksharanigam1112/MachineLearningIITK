# Univariate feature selection

import pandas as pd
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest,chi2  # acc to the basis of chi2 value best k features are selected
import warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values

x = array[:, 0:8]
y = array[:, 8]

# Feature extraction
test = SelectKBest(score_func=chi2 , k=4)       # selecting best columns for prediction, applying chi2 formula to select 4 cols
fit = test.fit(x,y)                             #fit funct stores the rating/scores for each feature internally

# Summarize scores
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(x)             # Select the best rating columns 2 5 6 8

# Summarize selected features
print("\n\n")
print(features[0:20 , :])