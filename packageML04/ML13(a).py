import numpy as np
n4 = np.array( [10,-1,0,90,300,3,-6,2])

print("n4 = ",n4)
n4.sort()           #In-place sorting

print("After sorting = ",n4)

n4 = np.array([10,-1,0,90,300,3,-6,2])

print("\nn4 = ",n4)
print("\nn4.argsort() = ",n4.argsort())       # Returns the index positions array for sorting
print("\nn4 = ",n4)

for i in n4.argsort():
    print(n4[i],end=" ")

