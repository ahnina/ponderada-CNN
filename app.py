from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
model = load_model('pesos.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return "No file"

    img = Image.open(io.BytesIO(file.read())).convert('L')
    img = img.resize((28, 28))
    img = np.array(img)
    img = img.reshape(1, 28, 28, 1).astype('float32') / 255

    prediction = model.predict(img)
    digit = np.argmax(prediction)

    return jsonify({'digit': int(digit)})

if __name__ == '__main__':
    app.run(debug=True)
