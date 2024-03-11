import pandas as pd
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
 
dataset_path = '/Users/Owner/Desktop/TWP/TandP.csv'
image_size=(48,48) #add 3 if RGB image
 
def load():
    data = pd.read_csv(dataset_path)
    pixels = data['Pixels'].tolist()
    width, height= 48, 48 ,# add depth 3 if RGB image
    vehicles = []
    for pixel_sequence in pixels:
        vehicle = [int(pixel) for pixel in pixel_sequence.split(' ')]
        vehicle = np.asarray(vehicle).reshape(width, height,) #add depth if RGB image
        a = vehicle
        vehicle = np.resize(vehicle.astype('uint8'),image_size)
        vehicles.append(vehicle.astype('float32'))

    vehicles = np.asarray(vehicles)
    A = vehicles
    vehicles = np.expand_dims(vehicles, -1)
    return vehicles, A
 
vehicle,A = load()