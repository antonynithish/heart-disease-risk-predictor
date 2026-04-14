import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset (IMPORTANT PATH)
df = pd.read_csv("data/heart.csv")

# Features & target
X = df.drop("heart_disease", axis=1)
y = df["heart_disease"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train (balanced FIX)
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_scaled, y_train)

# Save
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/heart_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Model trained successfully")