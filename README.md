# 🌾 Crop Recommendation System

A machine learning web app that recommends the most suitable crop to grow based on soil and climate conditions.

## 📋 Input Features
| Feature | Description | Unit |
|---|---|---|
| Nitrogen | Nitrogen content in soil | kg/ha |
| Phosphorus | Phosphorus content in soil | kg/ha |
| Potassium | Potassium content in soil | kg/ha |
| Temperature | Ambient temperature | °C |
| Humidity | Relative humidity | % |
| pH | Soil pH level | 0–14 |
| Rainfall | Annual rainfall | mm |

## 🛠️ Tech Stack
- **Model** — Random Forest Classifier (scikit-learn)
- **Backend** — Flask
- **Frontend** — HTML, CSS

## 🚀 How to Run
1. Clone the repo and install dependencies
```bash
   pip install -r requirements.txt
```
2. Train the model
```bash
   python model.py
```
3. Start the Flask app
```bash
   python app.py
```
4. Open `http://localhost:5000` in your browser

## 📁 Project Structure

├── app.py                    # Flask application
├── model.py                  # Model training script
├── model.pkl                 # Saved trained model
├── feature_names.json        # Feature order for inference
├── Crop_recommendation.csv   # Dataset
├── templates/
│   └── index.html            # Frontend UI
└── static/
└── style.css             # Stylesheet
