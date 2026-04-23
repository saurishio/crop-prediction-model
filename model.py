import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# ✅ Load dataset (use local path)
data = pd.read_csv("Crop_recommendation.csv")  # make sure file is in the same folder

# Display first few rows
print(data.head())

# Check shape and null values
print("Shape of dataset:", data.shape)
print("Missing values:\n", data.isnull().sum())

# Split features and labels
X = data.iloc[   :    ,    :-1]  # features
y = data.iloc[  :  , -1]   # target/label

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training feature shape:", X_train.shape)
print("Training label shape:", y_train.shape)

# Build model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# ✅ Save model correctly
pickle.dump(model, open("model.pkl", "wb"))


