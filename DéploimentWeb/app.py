from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
import base64
import io

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load the model
model = load_model('models/model.h5')

def predict_label(img_path):
    dic = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
    
    img = image.load_img(img_path, target_size=(32, 32))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict(img)
    prediction = np.argmax(prediction, axis=1)[0]
    
    return dic[prediction]

@app.route("/", methods=['GET'])
def main():
    return render_template("start.html")

@app.route("/predict", methods=['GET'])
def choose_plant():
    return render_template("predict.html")

@app.route("/predict/submit", methods=['POST'])
def get_output_tomato():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)
        
        prediction = predict_label(img_path)
        return render_template("predict.html", prediction=prediction, img_path=img_path)
    
    return redirect(request.url)

# New route for REST API
@app.route("/api/predict", methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    img_data = base64.b64decode(data['image'])
    img = image.load_img(io.BytesIO(img_data), target_size=(32, 32))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict(img)
    prediction = np.argmax(prediction, axis=1)[0]
    dic = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}
    
    return jsonify({'prediction': dic[prediction]})

if __name__ == '__main__':
    app.run(debug=True)
