import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    # Get form values and convert to float
    float_features = [float(x) for x in request.form.values()]
    
    # Convert to numpy array and reshape for model
    features = np.array([float_features])
    
    # Make prediction
    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"The Predicted Crop is {prediction[0]}"
    )

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
