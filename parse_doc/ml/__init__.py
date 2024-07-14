import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
import random
import os
import glob
import tensorflow as tf
import gdown
from tensorflow import keras # this allows  instead of 
from tensorflow.keras import layers # this allows  instead of 
tf.keras.utils.set_random_seed(111) # set random seed
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50, VGG16
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam, AdamW
import zipfile
# import cv2

# To supress any warnings during the flow
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({'font.size': 14})

   

class ModelConfig:
    test_size=0.2,
    image_size=(224,224)
    batch_size=16
    num_classes=3
    initial_epochs=10
    fine_tune_epochs=10
    lr=1e-5
    weight_decay=4e-3
    beta_1=0.9
    beta_2=0.999

class PreprocessingConfig:
    rescale=1./255
    rotation_range=20
    width_shift_range=0.2
    height_shift_range=0.2
    shear_range=0.2
    zoom_range=0.2
    horizontal_flip=True
    brightness_range=[0.8, 1.2]