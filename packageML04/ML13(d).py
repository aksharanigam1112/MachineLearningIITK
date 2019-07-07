import numpy as np

print("--Trancedental Functions--")
a = np.arange(0,6)

print(np.sin(a))
print(np.log(a))
print(np.exp(a))

# Shape mismatches (Error)
# a = np.arange(4)
# print(a+np.arange([1,2]))