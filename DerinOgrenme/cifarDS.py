import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import timedelta
#from datatime import timedelta
#cifar datasetinde hayvanlar insanlar araçlar bir sürü daha karmaşık resimler var.
'''
NOt
tanınması gereken ikiden fazla kategori varsa softmax kullanırız. İki tane kategori varsa sigmoid kullanırız. Mesela spam veya spam değil gibi 2 kategori olduğunda sigmoid kullanırı
'''

import cifar10

cifar10.download() # resimleri indirecek 10 dk sürebilir. :) ama bir sefere masustur.
#print(cifar10.load_class_names())

train_img, train_cls, train_labels = cifar10.load_training_data()
test_img, test_cls, test_labels = cifar10.load_test_data()

#print(len(train_img), len(test_img))#50K eğitim setimiz 10K de test setimiz var.

x = tf.placeholder(tf.float32, [None, 32,32,3]) # bu place holder resimlerimiz için yapılan tanımdır. 3 renkli resimler için. 1 siyahbeyaz
y_true = tf.placeholder(tf.float32, [None,10]) # etiketler için yapılan tanımdır.


#tek image için manuplatons
def pre_process_image(image):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_hue(image,max_delta=0.05)
    image = tf.image.random_contrast(image,lower=0.3, upper=1.0)
    image = tf.image.random_brightness(image, max_delta=0.2)
    image = tf.image.random_saturation(image,lower=0.0, upper=2.0)
    image = tf.minimum(image,1.0)
    image = tf.maximum(image,0.0)
    return image

#tüm resimlere üstteki fonksiyonu uygular
def pre_process(images):
    images = tf.map_fn(lambda image: pre_process_image(image), images)
    return images

#with tf.device('/cpu:0'): # eğer GPU kullanıyorsak burayı ekleyelim. bu kod için cpu kullan anlamına geliyor
distored_images = pre_process(images=x)


# tek tek layer tanımlamamak için fonksiyon yapıyoruz.
def conv_layer (input, size_in, size_out, use_pooling=True):
    w = tf.Variable(tf.truncated_normal([3,3, size_in, size_out], stddev=0.1)) #isabet oranı için 3 lerle oyna
    b = tf.Variable(tf.constant(0.1, shape=[size_out])) #beas tanımı

    conv = tf.nn.conv2d(input, w, strides=[1,1,1,1],padding='SAME') + b # resmin üzerinde 1 1 gezmek için
    y = tf.nn.relu(conv)

    if use_pooling:
        y = tf.nn.max_pool(y, ksize=[1,2,2,1], strides=[1,2,2,1],padding='SAME')
    return y

#full connected layer tanımlıyoruz.
def fc_layer(input, size_in, size_out, relu=True):
    w = tf.Variable(tf.truncated_normal([size_in, size_out], stddev=0.1))
    b = tf.Variable(tf.constant(0.1, shape=[size_out]))
    logits = tf.matmul(input,w) + b

    if relu:
        return tf.nn.relu(logits)
    else:
        return logits

# aşağıdaki kodlar ile modelimizi oluşturuyoruz.
conv1 = conv_layer(distored_images, 3, 32, use_pooling=True) # resim 16 16 32 boyutunda olacak. 32 adet filtre kullanıldı.
conv2 = conv_layer(conv1, 32, 64, use_pooling=True) # bir önceki conv1 kullanıldı. outpu 8 8 64 olacak. derinlik 64
conv3 = conv_layer(conv2, 64, 64, use_pooling=True) # output 4 4 64 oldu
flattend = tf.reshape(conv3, [-1, 4 * 4 * 64]) # düzleştirme işlemi yapıyoruz.
fc1 = fc_layer(flattend, 4 * 4 * 64, 512, relu=True) # nöron sayımız 512 belirledik.
fc2 = fc_layer(fc1, 512, 256, relu=True) # bu full conn layerda nöron sayısı 256 dır.
logits = fc_layer(fc2, 256, 10, relu=False)
y = tf.nn.softmax(logits)

# tahmin edilen sınıfımızı bir değişkene atıyoruz.
y_pred_cls = tf.argmax(y, 1)

xent = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_true)
loss = tf.reduce_mean(xent)

correct_prediction = tf.equal(y_pred_cls, tf.argmax(y_true, 1))

# oralamasını alıp yüzdesini göreceğiz
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#optimizasyon algoritmamızı yazabiliriz.
optimizer = tf.train.AdamOptimizer(52-4).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch_size = 128

def random_batch():
    index = np.random.choice(len(train_img), size=batch_size, replace=False)
    x_batch = train_img[index, :, :, :]
    y_batch = train_labels[index, :]

    return x_batch, y_batch

loss_graph =[]

# eğitmeye geçiyoruz.
def training_step(iterations):
    start_time = time.time()
    for i in range(iterations):
        x_batch, y_batch = random_batch()
        feed_dict_train = {x: x_batch, y_true: y_batch}
        [_, train_loss] = sess.run([optimizer, loss], feed_dict=feed_dict_train)
        loss_graph.append(train_loss)

        #eğitimi gözlemlemek için
        if i % 100 == 0:
            acc = sess.run(accuracy, feed_dict=feed_dict_train)
            print('iteration:',i,'Training accuracy:', acc, 'Training loss:', train_loss)
    end_time = time.time()
    time_dif = end_time - start_time
    print("Time usage:", timedelta(seconds=int(round(time_dif))))

batch_size_test = 256
def test_accuracy():
    num_images = len(test_img)
    cls_pred = np.zeros(shape=num_images, dtype=np.int)
    i = 0

    while i < num_images:
        j = min(i + batch_size_test, num_images)
        feed_dict = {x: test_img[i:j,:], y_true: test_labels[i:j,:]}
        cls_pred[i:j] = sess.run(y_pred_cls, feed_dict=feed_dict)
        i = j
    correct = (test_cls == cls_pred)
    print('Testing accuracy', correct.mean())

def distored_image(image, cls_true):
    image_dublicate = np.repeat(image[np.newaxis, :,:,:],9,axis=0)
    feed_dict = {x: image_dublicate}
    result = sess.run(distored_images,feed_dict=feed_dict)
    plot_images(images=result,cls_true=np.repeat(cls_true,9))
def plot_distorted_image(i):
    return distored_image(test_img[i,:,:,:],test_cls[i])

plot_distorted_image(8)

'''
training_step(10000)
test_accuracy()

plt.plot(loss_graph,'k-')
plt.title('Loss grafiği')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()
'''