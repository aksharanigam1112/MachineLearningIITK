import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import random
import collections
import time

start_time = time.time()

def elapsed(sec):
    if sec<60:
        return str(sec)+" sec"
    elif sec<(60*60):
        return str(sec/60)+"  min"
    else:
        return str(sec/3600)+" hr"

logs_path = '/tmp/tensorflow/rnn_words'
writer = tf.summary.FileWriter(logs_path)

train = 'Story.txt'

def read_data(fname):
    with open(fname) as f:
         content = f.readlines()
    content = [x.strip() for x in content]
    content = [content[i].split() for i in range(len(content))]
    content = np.array(content)
    content = np.reshape(content , [-1,])
    return content

training_data = read_data(train)
print("Loaded training dataset")

def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()
    for word in count:
        dictionary[word] = len(dictionary)
    reverse_dictionary = dict(zip(dictionary.values(),dictionary.keys()))
    return reverse_dictionary

dictionary, reverse_dict = build_dataset(training_data)
vocab_size = len(dictionary)

learning_rate = 0.001
training_iters = 50000
display_step = 1000
n_input = 3
n_hidden = 512

x = tf.placeholder("float",[None,n_input,1])
y = tf.placeholder("float",[None,vocab_size])

weights = {
    'out':tf.Variable(tf.random_normal([n_hidden,vocab_size]))

}

baises = {
    'out':tf.Variable(tf.random_normal([vocab_size]))
}

def RNN(x,weights,baises):
    x = tf.reshape(x,[-1.n_input])
    x = tf.split(x,n_input,1)

    rnn_cell = rnn.MinimalRNNCell([rnn.BasicLSTMCell(n_hidden),rnn.BasicLSTMCell(n_hidden)])
    outputs,states = rnn.static_rnn(rnn_cell,x,dtype=tf.float32)

    return tf.matmul(outputs[-1],weights['out'])+baises['out']

pred = RNN(x,weights,baises)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,labels=y))
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init = tf.global_variables_initializer()


with tf.Session() as session:
    session.run(init)
    step = 0
    offset = random.randint(0,n_input+1)
    end_offset = n_input+1
    acc_total = 0
    loss_total = 0

    writer.add_graph(session.graph)

    while step<training_iters:

        if offset > (len(training_data)-end_offset) :
            offset = random.randint(0,n_input+1)
        symbols_in_keys = [[dictionary[str(training_data[i])]] for i in range(offset,offset+n_input)]


