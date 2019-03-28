#/usr/bin/python
from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
from tensorflow import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Flatten
from tensorflow.keras.layers import Conv2D,MaxPooling2D
from tensorflow.keras.layers import LeakyReLU
from tensorflow.train import AdamOptimizer

import numpy as np

import os
os.environ['KERAS_BACKEND'] = 'tensorflow'
os.environ['MKL_THREADING_LAYER'] = 'GNU'


def new_run_log_dir(base_dir):
    log_dir = os.path.join('./log',base_dir)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    run_id = len([name for name in os.listdir(log_dir)])
    run_log_dir = os.path.join(log_dir,str(run_id))
    return run_log_dir

class NeuralNetwork(object):
    def __init__(self,log_dir):
        #revisar si existen pesos creados anteriormente
        self.checkpoint_path = 'trainingCNN/cp-{epoch:04d}.ckpt'
        self.checkpoint_dir = os.path.dirname(self.checkpoint_path)
        self.tensorboard = TensorBoard(log_dir=log_dir,histogram_freq=50)
        self.model = None
        self.isAlive = False
        self.epochs_train = 50
        self.batch_size = 32        

        # si tenemos un modelo entrenado cargar los pesos
        if os.path.exists(self.checkpoint_dir) and len(os.listdir(self.checkpoint_dir)) > 0:
            self.loadWeights()
            self.isAlive = True

        
    
    def createModel(self):
        self.model = keras.Sequential()
        self.model.add(Conv2D(32,kernel_size=(3,3),activation='linear',input_shape=(28,28,1),padding='same'))
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(MaxPooling2D(2,2,padding='same'))
        self.model.add(Conv2D(64,kernel_size=(3,3),activation='linear',input_shape=(28,28,1),padding='same'))
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(MaxPooling2D(2,2,padding='same'))
        self.model.add(Conv2D(128,kernel_size=(3,3),activation='linear',input_shape=(28,28,1),padding='same'))
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(MaxPooling2D(2,2,padding='same')  ) 
        self.model.add(Flatten())             
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(Dropout(0.75))
        self.model.add(Dense(5,activation='softmax'))

        self.model.compile(optimizer=AdamOptimizer(learning_rate=0.003),
        loss='categorical_crossentropy',
        metrics=['accuracy'])        

        return self.model

    def trainModel(self,dataSet):
        # create checkpoint
        self.cp_callback = keras.callbacks.ModelCheckpoint(self.checkpoint_path,save_weights_only=True,verbose=1,period=10)

        self.createModel()
        self.model.save_weights(self.checkpoint_path.format(epoch=0))
        # TODO : dividir el dataset en conjunto entrenador y de prueba
        self.model.fit(dataSet.image_ds,dataSet.label_ds,
        batch_size=self.batch_size,epochs=self.epochs_train,verbose=1,
        validation_data=(dataSet.image_ds,dataSet.label_ds),
        callbacks=[self.cp_callback,self.tensorboard])

    def loadWeights(self):
        # TODO : esta rutina asume que el entrenamiento termino 
        # modificar para restablecer el entranamiento desde un punto x
        self.createModel()
        latest = tf.train.latest_checkpoint(self.checkpoint_dir)
        self.model.load_weights(latest)

