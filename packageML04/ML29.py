# Binarize (upgrade a continuous feature of data into discrete based upon the threshold value)

from sklearn.preprocessing import Binarizer
from numpy import set_printoptions
from pandas import  read_csv

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(filename, names=hnames)
array = df.values

# Separate array into input and output components

x = array[:, 0:8]                   # [rows , cols]
y = array[:, 8]

binarizer = Binarizer(threshold=6)      # Values>=threshold become 1 while values<threshold become 0,
                                        # all these convertions are not in same data
binaryx = binarizer.fit_transform(x)

set_printoptions(precision=2)
print(binaryx[0:20 , :])