# Using correlation matrix plot for multi-variate input values

from matplotlib import pyplot as plt
import pandas as pd
import numpy
import warnings
warnings.filterwarnings(action="ignore")

# Correlations matrix plot
pd.set_option("display.width" , 2000)
pd.set_option('display.max_column' , 9)

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df  = pd.read_csv('indians-diabetes.data.csv' , names = hnames)

# Plot correlation matrix
correlation = df.corr()         # Calculates correlation coeff from each row value with each value
print(correlation)

fig = plt.figure()              # To show the pop-up

# Following will add matrix & slide bar in entire area
subfig = fig.add_subplot(111)

cax = subfig.matshow(correlation , vmin = -1 , vmax = 1)    # nos of the matrix are converted to the graphical matrix
                                                            # vertica min & vertical max values always lie b/w (-1,1)
                                                            # By Default its values lies b/w (0,1)

fig.colorbar(cax)               # Paints the matrix according to the colour bar

ticks = numpy.arange(0,9)       # It will take values from 0,8
subfig.set_xticks(ticks)
subfig.set_yticks(ticks)
subfig.set_xticklabels(hnames)
subfig.set_yticklabels(hnames)

plt.show()
