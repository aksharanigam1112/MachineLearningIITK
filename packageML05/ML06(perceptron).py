import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
# from sklearn.linear_model import Perceptron
# import seaborn as sbn

x , y = make_blobs(n_samples=500 , centers=2 ,n_features=2,random_state= 11)
print(x.shape , y.shape)

# plt.style.use("seaborn")
plt.scatter(x[:,0] ,x[:,1], c='y',s=10) #cmap=plt.cm.Accent)
plt.show()

# model = Perceptron()

def Sigmoid(z):
    return 1.0/(1+np.exp(-z))

def predict(x,weights):
    z = np.dot(x,weights)
    prediction = Sigmoid(z)
    return prediction

def loss(x,y,weights):
    # Binary cross entropy

    y_pred = predict(x,weights)
    cost = np.mean(-y*np.log(y_pred)-(1-y)*np.log(1-y_pred))
    return cost

def update(x,y,weights,learning_rate):
    y_pred = predict(x,weights)
    dw = np.dot(x.T , y_pred-y)
    m = x.shape[0]

    weights  = weights - learning_rate*dw(float(m))
    return weights

def train(x,y,learning_rate=0.5,maxEpochs=100):

    ones = np.ones((x.shape[0],1))
    x = np.hstack((ones,x))

    weights = np.zeros(x.shape[1])


    for epoch in range(maxEpochs):
        weights = update(x,y,weights,learning_rate)

        if(epoch%20 ==0):
            l = loss(x,y,weights)
            print("Epoch: ",epoch)
            print("Loss rate: ",l)

    return weights

train(x,y)


