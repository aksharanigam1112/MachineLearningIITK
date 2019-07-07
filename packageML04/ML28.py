# Normalization

from sklearn.preprocessing import Normalizer
from numpy import set_printoptions
from pandas import  read_csv

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(filename, names=hnames)
array = df.values

# Separate array into input and output components

x = array[:, 0:8]                   # [rows , cols]
y = array[:, 8]

scaler = Normalizer()               # rescaling only b/w 0 to 1
normalizedx = scaler.fit_transform(x)

set_printoptions(precision=2)
print(normalizedx[0:10 , :])