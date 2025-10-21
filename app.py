from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import datetime
import requests

from colorama import Fore, Style

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask backend runningsuccessfully with multiple libraries!"
    print(Fore.GREEN + "Deployment successful!" + Style.RESET_ALL)

@app.route("/data")
def data():
    # Create a small dataframe
    df = pd.DataFrame({
        "Name": ["Ali", "Taimoor", "Najam"],
        "Score": [90, 85, 88],
        "Date": [datetime.date.today()] * 3
    })
    return df.to_json(orient="records")

@app.route("/predict", methods=["POST"])
def predict():
    # Example: use numpy to simulate a prediction
    data = request.json.get("values", [])
    if not data:
        return jsonify({"error": "No values provided"}), 400
    
    arr = np.array(data)
    prediction = float(np.mean(arr) + np.random.randn() * 0.1)
    return jsonify({"prediction": prediction})

@app.route("/external")
def external():
    # Example: call an external API
    r = requests.get("https://api.github.com")
    return jsonify({"github_status": r.status_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
