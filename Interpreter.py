import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import pickle
import sys
from PyQt5.QtCore import *
#from ui import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Interpreter:
    def __init__(self):
        self.class_names = ['planes', 'tanks'] 
        self.img_height = 180
        self.img_width = 180
        
    def int_load(self, fn='model'): 
        
        name = fn + '.pickle'   
        with open(name, 'rb') as f:
            self.model = pickle.load(f)

    def insert_image(self, file_name, fn='model') :
        self.int_load(fn)
        test_path = file_name
        img = tf.keras.utils.load_img(test_path, target_size=(self.img_height, self.img_width))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        message = (
            "This image is most likely a {} with a {:.2f} percent confidence."
            .format(self.class_names[np.argmax(score)], 100 * np.max(score))
        )
        return message