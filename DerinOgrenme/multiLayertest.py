import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/MNIST/",one_hot=True)

x= tf.placeholder(tf.float32,[None,784])
y_true = tf.placeholder(tf.float32,[None,10])
pkeep = tf.placeholder(tf.float32) #dropout modelimiz için. kullanılmayan nöronların drop edilmesi.


layer_1 = 128 # layer tanımlıyoruz ve içindeki nöron sayısını belirtiyoruz.
layer_2 = 64
layer_3 = 32
layer_out = 10

weight_1 = tf.Variable(tf.truncated_normal([784, layer_1], stddev=0.1))
bias_1 = tf.Variable(tf.constant(0.1, shape=[layer_1]))

weight_2 = tf.Variable(tf.truncated_normal([layer_1, layer_2], stddev=0.1))
bias_2 = tf.Variable(tf.constant(0.1, shape=[layer_2]))

weight_3 = tf.Variable(tf.truncated_normal([layer_2, layer_3], stddev=0.1))
bias_3 = tf.Variable(tf.constant(0.1, shape=[layer_3]))

#output layerımız
weight_4 = tf.Variable(tf.truncated_normal([layer_3, layer_out], stddev=0.1))
bias_4 = tf.Variable(tf.constant(0.1, shape=[layer_out]))

#aktivasyon fonksiyonları nn kütüphanesinde yer alır.
y1 = tf.nn.relu(tf.matmul(x, weight_1) + bias_1)
y1d = tf.nn.dropout(y1,pkeep)
y2 = tf.nn.relu(tf.matmul(y1d, weight_2) + bias_2)
y2d = tf.nn.dropout(y2,pkeep)
y3 = tf.nn.relu(tf.matmul(y2d, weight_3) + bias_3)
y3d = tf.nn.dropout(y3,pkeep)

logits = tf.matmul(y3, weight_4) + bias_4
y4 = tf.nn.softmax(logits)

xent = tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = y_true)
loss = tf.reduce_mean(xent)

correct_prediction = tf.equal(tf.argmax(y4,1), tf.argmax(y_true, 1)) # doğru_tahmin
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32)) #doğruluk

optimize = tf.train.AdamOptimizer(0.001).minimize(loss) # kaybı minimize etmek istiyoruz.
# Buraya kadar tanımlamalardı.

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch_size = 128
loss_graph = []

# buradan sonra modelimizi eğitiyoruz.
def training_step (iterations):
    for i in range(iterations):
        x_batch, y_batch = mnist.train.next_batch(batch_size) # resimlerimizi giriyoruz.
        feed_dict_train = {x: x_batch, y_true: y_batch, pkeep: 0.75} #pkeep oranı aktif olacak nöron oranı bu örnekte %75 nöron kullan diyoruz.
        [_, train_loss] = sess.run([optimize, loss], feed_dict=feed_dict_train)

        loss_graph.append(train_loss)

        #burada her 100 iterasyonda bir çalıştırıyoruz.
        if i % 100 == 0:
            train_acc = sess.run(accuracy, feed_dict=feed_dict_train)
            print('Iterations:', i, 'Training accuracy:', train_acc, 'Training loss:',train_loss)

# burası test_acc içindeydi daha sonradan yukarı çıkarttık. Hata yaptığı resimleri incelemek için yaptık.
feed_dict_test = {x: mnist.test.images, y_true: mnist.test.labels, pkeep: 1} # pkeep parametresi tüm nöronlar çalışsın
def test_accuracy():
    acc = sess.run(accuracy, feed_dict = feed_dict_test)
    print('Testing accuracy:', acc)

# sistem nerelerde hangi resimlerde hata yapıyor görmemiz için
# plot_images ve plot_exampla_errors metodlarını kullandık...
def plot_images(images, cls_true, cls_pred=None):
    assert len(images) == len(cls_true) == 9
    fig, axes = plt.subplots(3, 3)
    fig.subplots_adjust(hspace=0.3, wspace=0.3)

    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i].reshape(28, 28), cmap='binary')
        if cls_pred is None:
            xlabel = "True: {0}".format(cls_true[i])
        else:
            xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

        ax.set_xlabel(xlabel)
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()


def plot_example_errors():
    mnist.test.cls = np.argmax(mnist.test.labels, axis=1)
    y_pred_cls = tf.argmax(y4, 1)
    correct, cls_pred = sess.run([correct_prediction, y_pred_cls], feed_dict=feed_dict_test)
    incorrect = (correct == False)

    images = mnist.test.images[incorrect]
    cls_pred = cls_pred[incorrect]
    cls_true = mnist.test.cls[incorrect]

    plot_images(images=images[0:9], cls_true=cls_true[0:9], cls_pred=cls_pred[0:9])


training_step(10000)
test_accuracy()


plt.plot(loss_graph, 'k-')
plt.title('Loss Grafiği')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.show()

plot_example_errors()


#NOT: dropout ile isabet oranımız artırırız.