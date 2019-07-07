import matplotlib.pyplot as plt
import numpy as np
n = 5+np.random.randn(10)       # Used to generated a bunch of random data

print("n =",n)
# m = [m for m in range(len(n))]

m = list(range(len(n)))
print("m = ",m)

plt.bar(m,n)
plt.title("Raw data")
plt.show()

plt.hist(n,bins=10)              # bins=10 is used to Divide the data into ten parts
plt.title("Histogram")
plt.show()