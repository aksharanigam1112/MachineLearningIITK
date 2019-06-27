import numpy as np
print("-"*20)
darr = np.array([ [1,2,3] , [4,5,6] ])

print("darr.ndim = ",darr.ndim) # to find the dimensions
print("darr.shape = ",darr.shape)   # it returns a tuple with (r,c) format
                                    # while in the previous example it uses the format (value,)
print("darr.size = ",darr.size)
print("darr.dtype = ",darr.dtype)
print(darr)
print("darr[0,1] = ", darr[0,1])
print("darr[0] = ",darr[0])
print("darr[:,0] = " , darr[: ,0])          # : means all
print("darr[1, : ] = ",darr[1, : ])
print("darr[: ,0:2] =\n",darr[: ,0:2])
