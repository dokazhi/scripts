# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:49:33 2017

@author: dos
"""

import numpy
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils

numpy.random.seed(42)
(X_train,y_train),(X_test,y_test) = cifar10.load_data()
#normalization of data
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
#preobrazvanie metki
Y_train = np_utils.to_categorical(y_train,10)
Y_test = np_utils.to_categorical(y_test,10)

#Neural
model = Sequential()
#1st layer of SVERTKA
model.add(Convolution2D(32,3,3, border_mode='same',input_shape=(3,32,32),
                        activation='relu'))
#2nd
model.add(Convolution2D(32,3,3, activation='relu'))
#layer subchoice
model.add(MaxPooling2D(pool_size=(2,2)))
#regulation layer
model.add(Dropout(0.25))

#2nd cascade
model.add(Convolution2D(64,3,3, border_mode='same',activation='relu'))
#4th layer of svertka
model.add(Convolution2D(64,3,3, activation='relu'))
#layer of subchoice #2
model.add(MaxPooling2D(pool_size=(2,2)))
#regurelation
model.add(Dropout(0.25))

#Классификатор
model.add(Flatten())#Преобразование из 2D и плоскость
#Полносвязный слой
model.add(Dense(512, activation='relu'))#512 нейронов на вход
model.add(Dropout(0.5))
#Exit layer
model.add(Dense(10, activation='softmax'))

#Компиляция сети
model.compile(loss='categorical_crossentropy',optimizer='SGD',metrics=['accuracy'])
#Обучение сети
model.fit(X_train,Y_train,batch_size=32,nb_epoch=25,validation_split=0.1,shuffle=True)
json_model = model.to_json()
json_file = open("cifar10_model.json","w")
json_file.write(json_model)
json_file.close()
model.save_weights('cifar10_weights.h5')
#Тестим точность модели на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose=0)
print('accurary:',scores[1]*100)
