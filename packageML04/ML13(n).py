import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-np.pi , np.pi , 256 , endpoint=True)

print("x = ",x)

s = np.sin(x)
c = np.cos(x)

plt.grid(True)
plt.axis([-4,4,-2,2])
plt.plot(x,s)
plt.plot(x,c)
plt.show()
