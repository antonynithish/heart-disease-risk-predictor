import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model", "heart_model.pkl")
scaler_path = os.path.join(BASE_DIR, "model", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

FEATURE_NAMES = [
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

def explain_prediction(input_data):
    try:
        input_df = pd.DataFrame([input_data])[FEATURE_NAMES]

        input_scaled = scaler.transform(input_df)

        coefficients = model.coef_[0]

        explanation = {}

        for i, feature in enumerate(FEATURE_NAMES):
            contribution = input_scaled[0][i] * coefficients[i]
            explanation[feature] = round(contribution, 4)

        return explanation

    except Exception as e:
        print("Explanation Error:", e)
        return None