from  __future__ import absolute_import, division, print_function, unicode_literals

#tensorflow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
#numpy
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import gc
import random
import cv2
import seaborn as sns

train_dir = '/home/hoaithuong/PycharmProjects/multiple_fruits/train'
test_dir = '/home/hoaithuong/PycharmProjects/multiple_fruits/test'
test_images = ['/home/hoaithuong/PycharmProjects/multiple_fruits/test/{}'.format(i) for i in os.listdir(test_dir)]

fruits = {
    'apple':0,
    'banana':1,
    'plum':2,
    'kiwi':3,
    'pinea':4,
    'mango':5,
    'peach':6,
    'blueberry':7,
    'orange':8,
    'grape_white': 9
}
class_name= ['apple', 'banana', 'plum', 'kiwi', 'pinea', 'mango','peach', 'blueberry', 'orange', 'grape_white']
t=len(class_name)
print(t)
#sys.exit()

nrows = 50
ncolumns = 50
channels = 3
#print(fruits.items())
train_images = ['/home/hoaithuong/PycharmProjects/multiple_fruits/train/{}'.format(i)
                for i in os.listdir(train_dir)
                    for a in fruits
                        if a in i]
#print(train_images.shape)
print(len(train_images))
random.shuffle(train_images)
#sys.exit()
def read_and_process_image(list_of_images):
    x=[] #images
    y=[]  #labels
    for image in list_of_images:
        z=cv2.imread(image)
        z=cv2.cvtColor(z,cv2.COLOR_BGR2RGB)
        z=cv2.resize(z,(nrows, ncolumns))
        x.append(z)
        for i,j in fruits.items():
            if i in image:
                y.append(j)
    return x,y
x,y = read_and_process_image(train_images)

print(len(x))
print(len(y))
#sys.exit()
x=np.array(x)
y=np.array(y)
plt.figure(figsize=(10, 10))
#a = fruits
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x[i], cmap=plt.cm.binary)
    plt.xlabel(class_name[y[i]])
plt.show()
#sys.exit()

sns.countplot(y)
plt.title('labels for fruits')
print(x.shape)
print(y.shape)
ntrain=len(x)
batch_size=32
#sys.exit()
#setup the layers
model = keras.Sequential(
    [
        keras.layers.Conv2D(32,(3,3), activation='relu',input_shape=(50, 50, 3)),
        keras.layers.MaxPooling2D((2,2)),
        keras.layers.Conv2D(64,(3,3), activation='relu'),
        keras.layers.MaxPooling2D((2,2)),
        keras.layers.Conv2D(128,(3,3), activation='relu'),
        keras.layers.MaxPooling2D((2,2)),
        keras.layers.Conv2D(128,(3,3), activation='relu'),
        keras.layers.MaxPooling2D((2,2)),
        keras.layers.Flatten(),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dense(t, activation='softmax')
    ]
)
model.compile(optimizer= 'adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

train_datagen = ImageDataGenerator( rescale=1./255.0,
                                    rotation_range=40,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True,)
train_generator = train_datagen.flow(x, y, batch_size= batch_size)
history = model.fit_generator(train_generator,
               steps_per_epoch=ntrain,
                epochs = 10)
model.save_weights('model_weights.h5')
model.save('model_keras.h5')
acc = history.history['acc']
loss = history.history['loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'b', label='Training accurarcy')
plt.title('Training accurarcy')
plt.legend()

plt.figure()
#Train loss
plt.plot(epochs, loss, 'b', label='Training loss')
plt.title('Training loss')
plt.legend()
plt.show()
#sys.exit()
#evaluate accuracy

#make predictions
x_test, y_test = read_and_process_image(test_images[0:15])
print(y_test)
#sys.exit()
X = np.array(x_test)
X= X/255.0
test_datagen = ImageDataGenerator(rescale=1./255)
#for batch in test_datagen.flow(X, batch_size=1):
prediction = model.predict(X)
print(prediction)
pred= np.array(prediction)
print(pred)
    #break
#sys.exit()
#test_labels = ['apple', 'banana', 'plum']
def plot_image(i, predictions_array, true_label, img):
    prediction_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    predict_label = np.argmax(predictions_array)
    print(predict_label)
    print(true_label)
    print(predictions_array)
    if predict_label == true_label:
        color='blue'
    else:
        color='red'
    plt.xlabel("{} {:1.0f}% ({})".format(class_name[predict_label],
                                        100*np.max(predictions_array),
                                         class_name[true_label]),
                                         color='blue')

def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array, true_label[i]
    plt.grid(False)
    plt.grid(False)
    plt.xticks(range(t))
    plt.yticks([])
    thisplot=plt.bar(range(t), predictions_array, color="#777777")
    plt.ylim([0,1])
    predict_label = np.argmax(predictions_array)
    thisplot[predict_label].set_color('red')
    thisplot[true_label].set_color('blue')


#plot several images with their predictions
num_rows=3
num_cols=5
num_images=num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, pred[i], y_test, X)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, pred[i], y_test)
    plt.tight_layout()
plt.show()

img = x_test[1]
img = (np.expand_dims(img,0))
predictions_single = model.predict(img)
print(predictions_single)
plot_value_array(1, predictions_single[0], y_test)
_= plt.xticks(range(10), class_name, rotation=45)
