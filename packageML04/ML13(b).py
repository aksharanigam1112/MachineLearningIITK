import numpy as np

a = np.array( [1,2,3,4])
print("a+1 = \n",(a+1))
print(a)
print("a**2 = \n",a**2)         # Squaring each element in the matrix

# All Arithmetic operations
a = np.array([1,2,3,4])
b = np.ones(4)+1                # By default it has float nature
print(a)
print(b)
print("a-b=\n",a-b)
print("a*b = \n",a*b)

# for element by element broad casting shape must be same

j= np.arange(5)
print(j)
print(2**(j+1))         # 2**[1,2,3,4,5] = [2,4,8,16,32]
print( 2** (j+1)-j)