import preprocessing.data as data
import tensorflow as tf
import neuron.model as model
tf.enable_eager_execution()
AUTOTUNE = tf.data.experimental.AUTOTUNE

# Este script pone en marcha el entrenamiento y solo el entranamiento 
# de la red neuronal
BATCH_SIZE = 32

if __name__ == "__main__":
    dataset = data.DataSet('./data')
    network = model.NeuralNetwork('./logdir')

    
    
    if not network.isAlive:
        network.trainModel(dataset)
    else:
        network.saveModel()
    
    # probar
    test_loss, test_acc = network.model.evaluate(dataset.image_ds,dataset.label_ds)
    print('Test accuracy: ',test_acc)
    print('Test loss',test_loss)    
    

    
