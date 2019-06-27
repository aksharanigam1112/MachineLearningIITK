# 2. a) Loading csv using NumPy

import numpy
raw_data = open("indians-diabetes.data.csv","r")

data = numpy.loadtxt(raw_data,delimiter=',')

print("Numpy loadtxt:- ",data.shape) # shape function tells the no. of rows and no. of columns
raw_data.close()

print("\n\n")

for l in data:
    print(l)

# Capability to read live data and the data is already in 00