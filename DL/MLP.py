import numpy as np 

input_size = 2
layers = [4,3]

output_size = 2

def softmax(a):

    e_a = np.exp(a)
    ans = e_a/np.sum(e_a,axis=1,keepdims=True)

    return ans

class NeuralNetwork:

    def __init__(self, input_size , layers , output_size):
        
        np.random.seed(0)
        
        model = {}

        #First Layer
        model['w1'] = np.random.randn(input_size,layers[0])
        model['b1'] = np.zeros(1,layers[0])

        # Second Layer
        model['w2'] = np.random.randn(layers[0],layers[1])
        model['b2'] = np.zeros(1,layers[1])

        # Output Layer
        model['w3'] = np.random.randn(layers[1],output_size)
        model['b3'] = np.zeros(1,output_size)
        self.model = model

    def forward(self,x):

        w1,w2,w3 = self.model['w1'],self.model['w2'] , self.model['w3']
        b1,b2,b3 = self.model['b1'],self.model['b2'] , self.model['b3']
        
        z1 = np.dot(x,w1)+b1
        a1 = np.tanh(z1)

        z2 = np.dot(a1,w2) + b2
        a2 = np.tanh(z2)

        z3 = np.dot(a2.w3)+b3

        y_ = softmax(z3)


        
