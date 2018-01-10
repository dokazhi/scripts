import config
import os
import telebot
import requests
from telebot import types
import image_utils
import numpy as np
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing import image
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import scipy.misc

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['photo'])
def recognize(message):
	try:
		file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		path = file_info.file_path.split('/')[1]
		with open('recog/'+path,'wb') as f:
			f.write(downloaded_file)
		print(message.chat.id)


		json_file = open('model/cifar10_arch.json','r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights('model/cifar10_weights.h5')
		optim = SGD()
		
		loaded_model.compile(loss='categorical_crossentropy', optimizer=optim, metrics=['accuracy'])

		classes = ['Самолет','Автомобиль','Птица','Кот','Олень','Собакен','Лягушка','Лошадь','Корабль','Грузовик']

		img_path = 'recog/'+path
		img = image.load_img(img_path, target_size=(32,32))

		
		x = image.img_to_array(img)
		x /= 255
		x = np.expand_dims(x, axis=0)
		# img = np.transpose(scipy.misc.imresize(scipy.misc.imread(img_path),(32,32)),(1,0,2)).astype('float32')
		# img /= 255
		# img = image_utils.dim_ordering_fix(img.reshape((-1,1,28,28)))
		prediction = loaded_model.predict(img)
		#prediction = np_utils.categorical_probas_to_classes(prediction)
		# bot.send_message(message.chat.id,)
		bot.reply_to(message,classes[np.argmax(prediction[0])])
		os.remove('recog/'+path)
		# print(prediction[0])
		# print(classes[np.argmax(prediction[0])])


	except Exception as e:
		bot.reply_to(message,e )
if __name__ == '__main__':
	bot.polling(none_stop=True)