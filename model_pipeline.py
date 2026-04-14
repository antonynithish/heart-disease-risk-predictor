import joblib
import pandas as pd
import os

# -------- Load model & scaler --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model", "heart_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "model", "scaler.pkl"))

# -------- Feature order --------
FEATURE_ORDER = [
    "age",
    "gender",
    "systolic_bp",
    "diastolic_bp",
    "cholesterol",
    "diabetes",
    "smoker",
    "physical_activity",
    "family_history"
]

# -------- Prediction Function --------
def predict_heart_risk(input_data):
    try:
        # Convert input → DataFrame
        input_df = pd.DataFrame([input_data])[FEATURE_ORDER]

        # Scale input
        input_scaled = scaler.transform(input_df)

        # Get probability (disease class)
        probability = model.predict_proba(input_scaled)[0][1]

        # Convert to %
        risk_percentage = round(probability * 100, 2)

        # 🔥 FINAL THRESHOLDS (TUNED FOR YOUR MODEL)
        if risk_percentage < 30:
            risk_level = "Low"
        elif risk_percentage < 80:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return risk_percentage, risk_level

    except Exception as e:
        print("Prediction Error:", e)
        return None, None