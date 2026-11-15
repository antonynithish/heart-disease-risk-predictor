
import numpy as np

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from preprocessing import load_data, build_preprocessor


def evaluate_model():
    X, y = load_data()

    # Reproduce the original train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Complete pipeline prevents preprocessing data leakage
    model = Pipeline([
        ("preprocessor", build_preprocessor()),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    # Five-fold stratified cross-validation
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    scoring = [
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc"
    ]

    results = cross_validate(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring
    )

    print("\n--- 5-FOLD CROSS-VALIDATION RESULTS ---")

    for metric in scoring:
        scores = results[f"test_{metric}"]

        print(
            f"{metric.upper():10s}: "
            f"{np.mean(scores):.4f} "
            f"+/- {np.std(scores):.4f}"
        )


if __name__ == "__main__":
    evaluate_model()
