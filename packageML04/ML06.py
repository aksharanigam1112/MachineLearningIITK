# 3. load the data using pandas

import pandas

hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']

dataFrame = pandas.read_csv("indians-diabetes.data.csv",names = hnames) # inserts heading to the top of the data

#pandas by default uses the first row as the heading+

print("\npandas data : ",dataFrame.shape )

print(dataFrame)
print("\n\n")

print(type(dataFrame))
