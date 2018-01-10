# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:35:51 2017

@author: dos
"""

import numpy as np
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing import image
from keras.optimizers import SGD
import matplotlib.pyplot as plt

json_file = open('json_model_cifar10.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('weight_model_cifar10.h5')

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

classes = ['samolet','automobil','ptica','kot','olen','sobaken','lyagush','loshad','korabl','gruzovik']

img_path = 'sails.jpg'
img = image.load_img(img_path, target_size=(32,32))
plt.imshow(img)
plt.show()

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

prediction = loaded_model.predict(x)
#prediction = np_utils.categorical_probas_to_classes(prediction)
print(prediction[0])
print(classes[np.argmax(prediction[0])])