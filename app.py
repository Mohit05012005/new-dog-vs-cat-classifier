from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf
import gdown
import os

app = Flask(__name__)

MODEL_PATH = "model.h5"
DRIVE_FILE_ID = "1kIDT8hr8N62gGveHhA8ch_GuxVZT-Nww"  # 👈 Replace this with your actual Google Drive File ID

# Step 1: Download model if not already downloaded
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

# Step 2: Load model
print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded.")

# Step 3: Predict route
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    image = Image.open(file).resize((256, 256))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    prob = model.predict(img_array)[0][0]
    label = "Dog" if prob > 0.5 else "Cat"

    return jsonify({"prediction": label, "confidence": float(prob)})

@app.route('/')
def home():
    return "Cat vs Dog Classifier (model.h5)"

if __name__ == '__main__':
    app.run(debug=True)
