from flask import Flask
from flask import request
import numpy as np
import os
import time
import neuron 

app = Flask(__name__)

UPLOAD_FILES = '/temp'
ALLOWED_EXTENSION = '.jpg'
app.config['UPLOAD_FOLDER'] = os.environ['HOME']+UPLOAD_FILES


@app.route('/producto',methods=['POST'])
def obtenerProducto():
    # por defecto envia http 400 si no lo encuentra
    f = request.files['imagen']
    prediction = []
    # revisar que exista la carpeta si no crear
    if not os.path.exists('./var'):
        os.makedirs('var')
    #guardar
    if f and allowed_file(f.filename):
        path = './var/'+str(time.time())+'.jpg'
        f.save(path)

        image = neuron.ImageP(path)
        # load model
        model = neuron.Model()
        prediction = model.predict(image)

    return str(prediction)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

