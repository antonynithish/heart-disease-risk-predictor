
from pathlib import Path

import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from preprocessing import load_data, build_preprocessor


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = MODEL_DIR / "heart_disease_logistic_regression.joblib"


def train_model():
    # Load features and binary target
    X, y = load_data()

    # Split data before fitting any preprocessing steps
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Build complete machine learning pipeline
    model = Pipeline([
        ("preprocessor", build_preprocessor()),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    # Train the model
    model.fit(X_train, y_train)

    # Generate predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Evaluate model
    print("\n--- DATA SPLIT ---")
    print("Training records:", len(X_train))
    print("Testing records:", len(X_test))

    print("\n--- CLASS DISTRIBUTION IN TEST SET ---")
    print(y_test.value_counts().sort_index())

    print("\n--- MODEL PERFORMANCE ---")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1-score:  {f1_score(y_test, y_pred):.4f}")
    print(f"ROC-AUC:   {roc_auc_score(y_test, y_prob):.4f}")

    print("\n--- CONFUSION MATRIX ---")
    print(confusion_matrix(y_test, y_pred))

    print("\n--- CLASSIFICATION REPORT ---")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["No disease recorded", "Disease recorded"]
        )
    )

    # Save the complete pipeline, including preprocessing
    joblib.dump(model, MODEL_PATH)

    print("\nModel saved to:", MODEL_PATH)


if __name__ == "__main__":
    train_model()
