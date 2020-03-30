import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import keras
import time
import vis
import os

print("Using Tensorflow \t{}".format(tf.__version__))
print("Using Keras \t\t{}".format(keras.__version__))

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras import activations

# model configuration
img_width, img_height = 28, 28
validation_split = 0.2
batch_size = 250
no_classes = 10
no_epochs = 25
verbosity = 1

# load MNIST
(input_train, target_train), (input_test, target_test) = mnist.load_data()

# Reshape data based on channels first / channels last strategy.
# This is dependent on whether you use TF, Theano or CNTK as backend.
# Source: https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py
if K.image_data_format() == 'channels_first':
    input_train = input_train.reshape(input_train.shape[0], 1, img_width, img_height)
    input_test = input_test.reshape(input_test.shape[0], 1, img_width, img_height)
    input_shape = (1, img_width, img_height)
else:
    input_train = input_train.reshape(input_train.shape[0], img_width, img_height, 1)
    input_test = input_test.reshape(input_test.shape[0], img_width, img_height, 1)
    input_shape = (img_width, img_height, 1)

# parse numbers as floats and normalize to [0, 1] interval
input_train = input_train.astype('float32')
input_train = input_train / 255
input_test  = input_test.astype('float32')
input_test  = input_test / 255

# convert vectors to binarized categories
target_train    = keras.utils.to_categorical(target_train, no_classes)
target_test     = keras.utils.to_categorical(target_test, no_classes)

# create the model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape, name='conv1'))
model.add(MaxPooling2D(pool_size=(2, 2), name='pool1'))
model.add(Dropout(0.25, name='drop1'))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', name='conv2'))
model.add(MaxPooling2D(pool_size=(2, 2), name='pool2'))
model.add(Dropout(0.25, name='drop2'))
model.add(Flatten(name='flatten1'))
model.add(Dense(256, activation='relu', name='dense1'))
model.add(Dense(no_classes, activation='softmax', name='dense2'))

# Compile the model
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

# Fit data to model
model.fit(
    input_train,
    target_train,
    batch_size=batch_size,
    epochs=no_epochs,
    verbose=verbosity,
    validation_split=validation_split
)

# Generate generalization metrics
score = model.evaluate(input_test, target_test, verbose=0)
print(f'Test loss: {score[0]} / Test accuracy: {score[1]}')

# save to disk
PATH_MNIST_KERAS_MODEL = 'mnist_original_model.h5'
model.save(PATH_MNIST_KERAS_MODEL)
print("Saved MNIST model to\t'{}'".format(PATH_MNIST_KERAS_MODEL))
