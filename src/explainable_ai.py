
from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = (
    PROJECT_ROOT / "models" /
    "heart_disease_logistic_regression.joblib"
)


def explain_model():
    model = joblib.load(MODEL_PATH)

    # Get the fitted preprocessing component
    preprocessor = model.named_steps["preprocessor"]

    # Get feature names after encoding and scaling
    feature_names = preprocessor.get_feature_names_out()

    # Get Logistic Regression coefficients
    coefficients = model.named_steps["classifier"].coef_[0]

    results = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": coefficients
    })

    results["Absolute_Importance"] = (
        results["Coefficient"].abs()
    )

    results = results.sort_values(
        by="Absolute_Importance",
        ascending=False
    )

    print("\n--- TOP 10 INFLUENTIAL FEATURES ---")
    print(
        results[[
            "Feature",
            "Coefficient"
        ]].head(10).to_string(index=False)
    )

    print("\n--- MODEL INTERPRETATION ---")
    print("Positive coefficient: associated with higher predicted odds.")
    print("Negative coefficient: associated with lower predicted odds.")
    print("Coefficient magnitude indicates strength on the model's scale.")


if __name__ == "__main__":
    explain_model()
