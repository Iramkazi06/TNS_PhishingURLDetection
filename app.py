# run with: python app.py   (after python train_model.py)
import json
import os

import joblib
import pandas as pd
from flask import Flask, jsonify, request

from backend.features import get_features, columns

base = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder="frontend", static_url_path="")

try:
    model = joblib.load(os.path.join(base, "artifacts", "model.pkl"))
except FileNotFoundError:
    print("Model not found. Run  python train_model.py  first.")
    raise SystemExit


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    url = str(data.get("url", "")).strip()
    if url == "":
        return jsonify({"error": "Please enter a URL"}), 400

    feats = get_features(url)
    prob = model.predict_proba(pd.DataFrame([feats], columns=columns))[0][1]
    return jsonify({
        "label": "Suspicious" if prob >= 0.5 else "Looks OK",
        "probability": round(float(prob) * 100, 1),
        "features": dict(zip(columns, feats)),
    })


@app.route("/metrics")
def metrics():
    with open(os.path.join(base, "artifacts", "metrics.json")) as f:
        return jsonify(json.load(f))


if __name__ == "__main__":
    app.run(debug=True)
