import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import os
import pickle

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class CreateModel:
  def __init__(self): 
    self.data_dir = pathlib.Path("C:/Users/Owner/Desktop/TWP/twpgit/TWP/merged").with_suffix('')
    self.batch_size = 32
    self.img_height = 180
    self.img_width = 180
    self.model = None

  def create_model(self, nClass=2, epoks=3, fn='model'):
    train_ds = tf.keras.utils.image_dataset_from_directory(
      self.data_dir,
      validation_split=0.2,
      subset="training",
      seed=123,
      image_size=(self.img_height, self.img_width),
      batch_size=self.batch_size)

    val_ds = tf.keras.utils.image_dataset_from_directory(
      self.data_dir,
      validation_split=0.2,
      subset="validation",
      seed=123,
      image_size=(self.img_height, self.img_width),
      batch_size=self.batch_size)

    class_names = train_ds.class_names
    plt.figure(figsize=(10, 10))
    for images, labels in train_ds.take(1):
      for i in range(nClass):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
    #plt.show(block=True)
    for image_batch, labels_batch in train_ds:
      print(image_batch.shape)
      print(labels_batch.shape)
      break
  
    

    normalization_layer = tf.keras.layers.Rescaling(1./255)

    normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_ds))
    first_image = image_batch[0]
    print(np.min(first_image), np.max(first_image))

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    num_classes = nClass

    model = tf.keras.Sequential([
      tf.keras.layers.Rescaling(1./255),
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dense(num_classes)
    ])

    model.compile(
      optimizer='adam',
      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
      metrics=['accuracy'])

    model.fit(
      train_ds,
      validation_data=val_ds,
      epochs=epoks
    )
    
    file_name = fn + '.pickle'
    with open(file_name, 'wb') as f:
      pickle.dump(model, f)
      
    self.model = model
      