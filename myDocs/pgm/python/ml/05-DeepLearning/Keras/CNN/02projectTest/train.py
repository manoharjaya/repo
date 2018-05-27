from keras.preprocessing.image import *
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from glob import glob
from model import CNN_model
# %matplotlib inline
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

batch_size = 4

# data augmentation
train_datagen = ImageDataGenerator(
        rescale=1./255,    
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
        'dataset',  # this is the target data directory
        target_size=(124, 124),  # all images will be resized to 124 x 124
        batch_size=batch_size,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels


x, y = next(train_generator)
x.shape, y.shape

#print 'x next=',x,'\t',x.shape
#print 'y next=',y,'\t',y.shape


model = CNN_model()



model.fit_generator(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=5)
model.save_weights('weights.h5')  # save weights after training



x, y = next(train_generator)
#print 'x=',x
#print 'y=',y

y = y.reshape(len(y), 1)

#print 'after reshape y=',y

y_pred = model.predict(x)
y_pred = (y_pred > 0.5) * 1

y == y_pred

#print 'equal-',y

img_path = random.choice(glob('dataset/Qnotes/*'))
img = load_img(img_path, target_size=(124, 124, 3)) # this is a PIL image
x = img_to_array(img) / 255.0
y = model.predict(np.expand_dims(x, axis=0))
print(np.squeeze(y) > 0.5)
img
