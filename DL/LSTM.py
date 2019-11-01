from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

data = [[[(i+j)/100] for i in range(5)]for j in range(100)]
target =  [(i+5)/100 for i in range(100)]

x = np.array(data,dtype=float)
y = np.array(target,dtype=float)

print(x.shape)
print(y.shape)

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3,random_state=4)

model = Sequential()

model.add(LSTM((1),batch_input_shape=(None,5,1),return_sequences=True))
model.add(LSTM((1),return_sequences=False))


model.compile(loss='mean_absolute_error',optimizer='adam',metrics=['accuracy'])

# print(model.summary())

history =  model.fit(xtrain,ytrain,epochs=1000,validation_data=(xtest,ytest))
# print(history)

results = model.predict(xtest)
plt.scatter(range(30),results,c='r')
plt.scatter(range(30),ytest,c='g')
plt.show()

plt.plot(history.history['loss'])
plt.show()
