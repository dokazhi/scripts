# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:19:59 2017

@author: dos
"""

import numpy
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import cv2

numpy.random.seed(42)
(X_train,y_train),(X_test,y_test) = cifar10.load_data()
print(X_train)
