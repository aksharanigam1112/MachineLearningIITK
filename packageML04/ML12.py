import numpy as np
arr = np.array([11,22,33,0.,44,55])
print("arr.sum() = ",arr.sum())
print("arr.std() = ",arr.std())         # Standard Deviation
print("arr.mean() = ",arr.mean())
print("arr.max() = ",arr.max())
print("arr.min() = ",arr.min())
print("arr.size = ",arr.size)

#Following line will print (index of nonzero)
print("arr.nonzero() = ",arr.nonzero())         # Returns the position of all non-zero values
print("arr.dtype = ",arr.dtype)

# Are all the elements are non-zero ??
print(np.all([1,2,-3,4]))
print(np.all([1,2,0,3,4]))

#Is any element greater than zero
print(np.any([1,2,3,4]))
print(np.any([1,2,0,3,4]))
print(np.any([0,0,0,0.,0]))
print(np.any([0,0,0.,1]))

n1 = np.array([4,5,6])
n2 = np.array([1,2,3])

print("\n\n")
print("n1 = ",n1)
print("n2 = ",n2)

# For these operations shape must be same this is called vector broadcasting
print("n1 + n2 = " , n1+n2 )
print("n1 - n2 = ",n1-n2)

n3 = np.array([4,5,6,7])
# operands could not be broadcast together with shapes (3,) (4,)
# print(n1+n3)
