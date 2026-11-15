
import joblib
import pandas as pd
from pathlib import Path


# Load the trained Cleveland model
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR / "models" /
    "heart_disease_logistic_regression.joblib"
)

model = joblib.load(MODEL_PATH)


# Expected feature order
FEATURE_ORDER = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]


def predict_heart_disease(input_data):

    # Arrange input values in the correct feature order
    input_df = pd.DataFrame(
        [input_data],
        columns=FEATURE_ORDER
    )

    # Predict binary classification
    prediction = int(model.predict(input_df)[0])

    # Get model probability for the positive class
    probability = model.predict_proba(input_df)[0][1]

    return prediction, round(float(probability) * 100, 2)
