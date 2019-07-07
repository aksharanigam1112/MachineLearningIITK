# 3D Bar plots

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = np.random.randint(10,size=10)       # all these are the starting points
z = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)                        # all these are the ending points
dz = [1,2,3,4,5,6,7,8,9,10]

ax.bar3d(x,y,z,dx,dy,dz,color='g')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.title("3D Bar Chart")
plt.tight_layout()
plt.show()