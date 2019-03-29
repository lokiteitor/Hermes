import tensorflow as tf
import os
import numpy as np
import tensorflow.keras as keras
tf.enable_eager_execution()
tf.executing_eagerly() 

class Model(object):
    def __init__(self):
        # cargar el modelo
        self.model = None
        archivo = open('../training/model/history.txt','r')
        model = archivo.readline()
        print("cargando:" + model)
        if os.path.exists(model):
            self.model = keras.models.load_model(model)
            self.model.summary()
        else:
            print("El modelo no existe")

    def predict(self,image):
        prediction = self.model.predict(image.image)
        prediction = np.argmax(prediction)
        prediction = {
            "index":prediction
        }

        return prediction


class ImageP(object):
    def __init__(self,path):
        self.path = path
        self.image = None
        #cargar imagen
        if os.path.exists(self.path):
            raw = tf.read_file(self.path)
            is_jpg = tf.image.is_jpeg(raw)
            if(is_jpg):
                self.preProccess(raw)
    
    def preProccess(self,raw):
        self.image = tf.image.decode_image(raw,channels=1)
        self.image = tf.image.resize_images(self.image,[28,28])
        self.image = np.array(self.image)
        self.image = self.image.reshape(-1,28,28,1)
        self.image = self.image.astype('float32')
        self.image /= 255

if __name__ == "__main__":
    model = Model()