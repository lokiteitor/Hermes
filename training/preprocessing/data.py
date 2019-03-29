import pathlib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
import random
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split


#tf.enable_eager_execution()
#AUTOTUNE = tf.data.experimental.AUTOTUNE



class DataSet(object):
    def __init__(self,path):
        # self.dataset = None
        # self.label_OneHot = None
        # self.label_ds = None
        self.image_ds = []
        self.label_ds = []

        self.train_X = []
        self.train_Y = []
        self.test_X = []
        self.test_Y = []
        
        
        data_root = pathlib.Path(path)
        # obtener las rutas a las imagenes
        self.all_images = list(data_root.glob('*/*'))
        self.all_images = [str(path) for path in self.all_images]
        random.shuffle(self.all_images)
        self.countImg = len(self.all_images)
        # obtener las etiquetas para cada imagen en base al dir
        self.label_names = sorted(item.name for item in data_root.glob('*/') if item.is_dir())
        self.label_index = dict((name,index) for index,name in enumerate(self.label_names))

        # crear una lista con los index de label por cada imagen
        self.all_images_labels = [self.label_index[pathlib.Path(path).parent.name] for path in self.all_images]

        self.processesImage()
        #self.imagesToArray()
        self.labelsToOneHot()   
        self.splitDataSet() 

        print(self.label_names)
        print(self.label_index)

    def processesImage(self):
        images = []
        

        for i in self.all_images:
            # convertir las imagenes al formato requerido
            raw = tf.read_file(i)
            # TODO:  leemos en grayscale, mejorar modelo para leer rgb
            i = tf.image.decode_image(raw,channels=1)
            i = tf.image.resize_images(i,[28,28])
            
            images.append(i.numpy())
        
        images = np.array(images)
        self.image_ds = images.reshape(-1,28,28,1)
        self.image_ds = self.image_ds.astype('float32')
        self.image_ds /= 255

    def splitDataSet(self,proportion=0.3):
        self.train_X,self.test_X,self.train_Y,self.test_Y = train_test_split(self.image_ds, self.label_ds, test_size=proportion,shuffle=False)        

    def imagesToArray(self):
        print("Convirtiendo imagenes en matriz numpy")
        for image in self.all_images:
            imageP = Image.open(image)
            npImage = np.array(imageP)
            self.image_ds.append(npImage)
    
    def labelsToOneHot(self):
        self.label_ds =  to_categorical(self.all_images_labels)        
            

class PreProcessing(object):
    def __init__(self,train_images,train_labels):
        # convertir imagenes a matriz para alimentar la red
        self.train_X = train_images
        self.train_Y = train_labels
        self.train_Y_OneHot = None

        self.reshape()
        self.convertType()    
    
    def reshape(self):
        self.train_X = self.train_X.reshape(-1,28,28,1)
    
    def convertType(self):
        # convertir a float32
        self.train_X = self.train_X.astype('float32')
        # valores del grayscale 0 a 255 -> 0 a 1
        self.train_X /= 255

        

            

