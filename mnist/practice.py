# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:02:44 2017

@author: dos
"""

import numpy as np
from keras.preprocessing import image
from keras.utils import np_utils
from keras.models import model_from_json
import matplotlib.pyplot as plt


json_file = open('json_model_rn6.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('weights_model_rn6.h5')

loaded_model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])
img_path = '4.png'
img = image.load_img(img_path,target_size=(28,28),grayscale=True)
plt.imshow(img,cmap='gray')
plt.show()

x = image.img_to_array(img)
x = 255 - x
x /= 255
x = np.expand_dims(x,axis=0)

prediction = loaded_model.predict(x)
#prediction = np_utils.to_categorical(prediction)#np_utils.categorical_probas_to_classes(prediction)

print(np.argmax(prediction))
