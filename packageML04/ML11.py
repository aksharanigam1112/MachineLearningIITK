import numpy as np
zr = np.zeros([3,4])
print("0's filled array : \n",zr)
ar = np.ones([4,4])

print("1's filled array : \n" , ar)

print(ar*4)
print(ar.dtype)

#We create numpy array from range

arr = np.arange(1,6)
print("\narr = ",arr)
arr[3] = 16
print("After updating arr : ",arr)