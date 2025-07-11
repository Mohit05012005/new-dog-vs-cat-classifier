# 🐶 Cat vs Dog Image Classifier API (Flask + TensorFlow)

This project is a Flask-based REST API that classifies images as either a **cat** or a **dog** using a pre-trained deep learning model (`model.h5`), downloaded dynamically from Google Drive.

Hosted on: **Render.com**

---

## 🚀 Features

- Accepts image uploads via `/predict` route
- Returns JSON with predicted class and confidence score
- Automatically downloads `model.h5` from Google Drive on first run
- Uses TensorFlow, Flask, and Gunicorn

---

## 🧠 Model Details

- CNN trained on the [Dogs vs Cats dataset](https://www.kaggle.com/datasets/salader/dogs-vs-cats)
- Input image size: `256x256`
- Output: Binary classification — **Dog** or **Cat**
- Saved model size: ~100MB+

---

## 📁 Folder Structure



## 🔗 Large File Download

This project uses a file that exceeds GitHub's 100MB limit.

You can download the required file from Google Drive:

[📥 Click here to download the file](https://drive.google.com/uc?export=download&id=1kIDT8hr8N62gGveHhA8ch_GuxVZT-Nww)
