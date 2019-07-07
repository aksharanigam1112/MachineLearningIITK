# Unsupervised ML Algo (Clustering) (There is no dependent column)
# We do not predict anything

from copy import deepcopy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action="ignore")

# Importing the dataset
data = pd.read_csv('KMeansData.csv')

print("\nInput data & shape :", data.shape, "\n", data.head())

# Getting the values & plotting it
f1 = data['V1'].values
f2 = data['V2'].values

plt.scatter(f1, f2, c='black', s=10)
plt.show()

x = np.array(list(zip(f1, f2)))
print("x : \n", x)


# Euclidean Distance Calculator
def eud(a, b, ax=1):  # axis =0 is not possible since we have to calculate the difference column wise
    return np.linalg.norm(a - b, axis=ax)  # Linear Algebra is used to calculate the square root of sq of(a-b)


# Number of clusters
k = 3

# x coord of random centroids
cx = np.random.randint(0, np.max(x) - 20, size=k)
# We subtract some no. bcoz maybe the centroid is at the border , so we shift the centroid
print("\n cx : ", cx)

# y coord of random centroids
cy = np.random.randint(0, np.max(x) - 20, size=k)
print("\n cy : ", cy)

c = np.array(list(zip(cx, cy)), dtype=np.float32)
print("\nInitial centroids (Random position) : ", c)
print(c.shape)  # 3,2

# Plotting along with the centroids
plt.scatter(f1, f2, s=10, c='k')
plt.scatter(cx, cy, marker='*', s=300, c='r')  # or plt.scatter(c[:,0] , c[:,1], .... )
plt.show()

# To store the values of the centroids when it updates
c_old = np.zeros(c.shape)
print("C : \n", c)
print("c_old : \n", c_old)
print("\n len(x) : ", len(x))

# Cluster labels(0,1,2)
clusters = np.zeros(len(x))  # To store the index position of the shop from which there is min dist
# for the customer, 1D array of 3000 len

# zero filled numpy array of 3000 elements
print("\n clusters : ", clusters)

# Error function - Distance between new centroids & old centroids
error = eud(c, c_old)
print("\nError before loop: ", error)

# Loop will run till error becomes zero

while error.all():  # error!=0

    # Assigning value to the nearest cluster
    for i in range(len(x)):
        distances = eud(x[i], c)  # Calculating the dist for every customer's loc
        cluster = np.argmin(distances)  # Finding the min from that
        clusters[i] = cluster  # Storing the

    # Storing the old centroid values
    c_old = deepcopy(c)

    # Finding the new centroids by taking the average
    for i in range(k):
        points = [x[j] for j in range(len(x)) if clusters[j] == i]
        c[i] = np.mean(points, axis=0)
    error = eud(c, c_old)
    print("Error in loop :", error)

colors = ['b', 'c', 'r']
fig, ax = plt.subplots()  # Figure with the axes
for i in range(k):
    points = np.array([x[j] for j in range(len(x)) if clusters[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=25, c=colors[i])

ax.scatter(c[:, 0], c[:, 1], marker='*', s=100, c='y')
print("\nFinal centroid :", c)
plt.show()

# Using Library
from sklearn.cluster import KMeans

print("kmeans")
kmeans = KMeans(n_clusters=3)

data = pd.read_csv('KMeansData.csv')

f1 = data['V1'].values
f2 = data['V2'].values

x = np.array(list(zip(f1, f2)))
kmeans = kmeans.fit(x)
labels = kmeans.predict(x)
print("\n labels : ", labels)
centroids = kmeans.cluster_centers_

# Comparing with scikit-learn centroids
print("Kmeans centroid values : \n")
print("\nKmeans Manual Centroid : ", c)
print("\nKmeans sklearn centroid : ", centroids)
