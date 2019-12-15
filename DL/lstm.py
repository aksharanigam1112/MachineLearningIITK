import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

filename="macbeth.txt"
text=(open(filename).read()).lower()

#mapping chars with integer

unique_chars=sorted(list(set(text)))

char_to_int={}
int_to_char={}

for i,c in enumerate(unique_chars):
    char_to_int.update({c:i})
    int_to_char.update({i:c})

#preparing the dataset
X=[]
Y=[]

for i in range(0,len(text)-50,1):
    sequence=text[i:i+50]
    label=text[i+50]
    X.append([char_to_int[char] for char in sequence])
    Y.append(char_to_int[label])


#reshaping ,nomrmalizing and one hot encoding
X_modified=np.reshape(X,(len(X),50,1))
X_modified=X_modified/float(len(unique_chars))#Scaling X between 0 to 1
Y_modified=np_utils.to_categorical(Y)#Converts a class vector (integers) to binary class matrix.
print(Y_modified)

# #defining lstm model

model=Sequential()
model.add(LSTM(300, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
# #lstm has 300 memory units and returns sequences,This ensures that LStm next layer recieves sequences and not randomly scattered data

model.add(Dropout(0.2))
# # A dropout layer is applied after each LSTM layer to avoid overfitting of the model.

model.add(LSTM(300))
model.add(Dropout(0.2))

# # Finally, we have the last layer as a fully connected layer with a ‘softmax’ activation and neurons equal to the number of unique characters, because we need to output one hot encoded result. 
model.add(Dense(Y_modified.shape[1],activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
print(X_modified)
model.fit(X_modified,Y_modified,epochs=1,batch_size=30)

# #picking a random seed
start_index=np.random.randint(0,len(X)-1)
new_string=X[start_index]

# # generating characters
for i in range(50):
    x = np.reshape(new_string, (1, len(new_string), 1))
    x = x / float(len(unique_chars))

    #predicting
    pred_index = np.argmax(model.predict(x, verbose=0))
    char_out = int_to_char[pred_index]
    seq_in = [int_to_char[value] for value in new_string]
    print(char_out)

    new_string.append(pred_index)
    new_string = new_string[1:len(new_string)]