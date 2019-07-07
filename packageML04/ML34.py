# Feature importance selection with ExtraTreesClassifier
# Also known as Extremely Randomized Tree Classifier

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier   # Uses Ginny Coefficient importance to rank the cols
import  warnings
warnings.filterwarnings(action="ignore")

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values

x = array[:, 0:8]
y = array[:, 8]

# Feature Extraction
model = ExtraTreesClassifier()
model.fit(x,y)                      # It assigns ranking based on ginny coeff
scores = model.feature_importances_
print(scores)

# for imp in zip(hnames,scores):      # 1st method
#     print(imp)

result = list(zip(hnames,scores))   #2nd Method
print("\n\n",result,"\n\n\n")

from operator import itemgetter
print(sorted(result,key=itemgetter(1),reverse = True))      # itemgetter(1) tells that on which item of the tuple we have to sort
