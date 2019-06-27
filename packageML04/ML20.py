# Using univariate density plot

from matplotlib import pyplot as plt
import pandas

filename = 'indians-diabetes.data.csv'

hnames = [ 'preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' ,'class']

df = pandas.read_csv(filename , names=hnames)

df.plot(kind = 'density' , subplots = True , layout= (3,3) , sharex = False , sharey=False)

# kind tell that density plot is drawn
# Subplot divides the drawing area into small parts, by default it is always true
# Share tell that the ticks in every diagram are independent (Scalling) for both x and y by  default it is False
# Layout tells the way the small graphs will be divided

plt.show()

