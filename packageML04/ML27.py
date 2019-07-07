# Standardization ( data is converted into standard normal distribution mean = 0 var =1 )
# Values are smaller and for each column the avg is 0

from sklearn.preprocessing import StandardScaler
from numpy import set_printoptions
from pandas import  read_csv
import numpy as np

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(filename, names=hnames)
array = df.values

# Separate array into input and output components

x = array[:, 0:8]                   # [rows , cols]
y = array[:, 8]

scaler = StandardScaler()
rescaledx = scaler.fit_transform(x)

print(rescaledx[:30 , :])

# Summarize the data
set_printoptions(precision=1)
print(rescaledx[0:20 , :])
print("Mean of first Column\n",(np.mean(rescaledx[:,0]) ) )
