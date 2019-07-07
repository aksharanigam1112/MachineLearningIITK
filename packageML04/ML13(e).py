import numpy as np

x = np.array([1,2,3,4])
print("np.sum(x) = ",np.sum(x)) # This is external sum and we can pass a simple array as well not necessarily numpy array
print("x.sum() = ",x.sum())     # This is internal sum and we are bound to use it only with a numpy array

print("\nSum by rows & by columns\n")
x = np.array( [ [1,2] , [3,4] ] )
print(x)

print(x.sum())

print("x.sum(axis=0) = ",x.sum(axis=0))        # adding column wise 1st method axis = 0 is library specific
print(x[: ,0].sum() , x[: ,1].sum())            # 2nd method

print(x.sum(axis=1))                            # row wise addition 1st method axis = 1 is library specific
print(x[0 ,: ].sum() , x[1, : ].sum())          # 2nd Method

print("\nExtrema\n")
x = np.array([1,3,2])

print(x.min())
print(x.max())

# Logical Operations
print(np.all( [ True , True , False]))
print(np.any([True , True , False]))

print("\n\nNumpy can be used for array comparisons ")
a = np.zeros((10,10))
print("a = ",a)
print(np.any(a!=0))             # Scalar broadcasting
print(np.all(a==a))
print(np.any(a>0))

print("\nStatistics\n")
x = np.array([1,2,3,1,1])
print("x.mean() = ",x.mean())               # internal func
print("np.median(x) = ",np.median(x))       # it is external function
print("x.std() = ",x.std())                 # internal func
                                            # mode is neither