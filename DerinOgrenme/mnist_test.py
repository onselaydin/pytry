#windows için $ set TF_CPP_MIN_LOG_LEVEL=2
#mnist bir veri dataseti. içine harfler rakamlar vs resimler olan bir datasetdir. 
#https://www.tensorflow.org/guide/datasets
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("data/MNIST", one_hot = True) # buraya kadar resimlerimizi aldık
x = tf.placeholder(tf.float32, [None, 784])  # inputumuz x
y_true = tf.placeholder(tf.float32, [None,10]) # etiketlerde y_true

w = tf.Variable(tf.zeros([784,10])) # eğitiyoruz. 10 farklı tahmin yada 10 nöronumuz var.
b = tf.Variable(tf.zeros([10])) # bise 

logits = tf.matmul(x, w) + b
y = tf.nn.softmax(logits)

xent = tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_true) # tahminleri gerçek değerler ile karşılaştırdık.
loss = tf.reduce_mean(xent)

correct_prediction = tf.equal(tf.argmax(x, 1), tf.argmax(y_true,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

optimize = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch_size = 128

def training_step(iterations):
    for i in range(iterations):
        x_batch, y_batch = mnist.train.next_batch(batch_size)
        feed_dict_train = {x: x_batch,y_true: y_batch}
        sess.run(optimize, feed_dict=feed_dict_train)
def test_accuracy():
    feed_dict_test = {x: mnist.test.images, y_true: mnist.test.labels}
    acc = sess.run(accuracy, feed_dict = feed_dict_test)
    print('Testing accuracy:', acc)
training_step(2000)
test_accuracy()
