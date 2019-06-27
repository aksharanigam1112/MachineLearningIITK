from matplotlib import pyplot as plt
from pandas import read_csv
from pandas.plotting import scatter_matrix
import warnings
warnings.filterwarnings(action="ignore")

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df  = read_csv('indians-diabetes.data.csv' , names = hnames)

scatter_matrix(df)          # Creating scatter matrix
plt.show()

