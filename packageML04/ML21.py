# Using box and whisker plot

from matplotlib import pyplot as plt
import pandas

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pandas.read_csv(filename, names=hnames)

df.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
plt.show()

# Box represents middle 50 percentile data
# The line in the box represents the median line
# The circle is called Outliers, data that is too far from the median (1.5 times)

