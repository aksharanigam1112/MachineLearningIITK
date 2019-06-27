list1 = [1,2,3]
print("list1*4 = " ,list1 * 4) # we want to broadcast the array but it doesn't support operation broadcasting

import numpy as np
arr = np.array([1,2,3])

print(arr)

print("arr  * 4 = ",arr*4)
print("arr + 4 = ",arr+4)
print("arr/2 = ",arr/2)
print("arr/2.0 = ",arr/2.0)
print("arr//2 = ",arr//2)
print("arr//2.0 = ",arr//2.0)
# Numpy supports operation braodcasting
# when operation is done with a single value then it is called scalar operation

a= 10
print(type(a))
a=12.5
print(type(a))

print(type(arr))
print("arr.dtype = ",arr.dtype)
print("arr.size = ",arr.size)

print("arr.shape = ",arr.shape)
