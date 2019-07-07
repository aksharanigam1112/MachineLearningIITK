import matplotlib.pyplot as plt
import numpy as np
arr = np.arange(0.0 , 5.0 , 0.2)    # 0.0 - 4.8 s
print(arr)

# Drawing multiple lines with diff formattinf in one plotting attempt
plt.plot(arr , arr , 'r*-' , arr , arr+3 , 'bs-' , arr , arr+6 , 'r-' , arr , arr+6 , 'bo' , markersize=5)
plt.show()