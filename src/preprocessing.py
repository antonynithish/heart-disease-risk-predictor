
import pandas as pd
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "processed.cleveland.data"
)

COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "num"
]

# Features that represent continuous measurements
NUMERIC_FEATURES = [
    "age", "trestbps", "chol", "thalach", "oldpeak"
]

# Features that represent categories or binary values
CATEGORICAL_FEATURES = [
    "sex", "cp", "fbs", "restecg", "exang",
    "slope", "ca", "thal"
]


def load_data():
    df = pd.read_csv(
        DATA_PATH,
        header=None,
        names=COLUMNS,
        na_values="?"
    )

    for column in COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="raise")

    X = df.drop(columns=["num"])
    y = (df["num"] > 0).astype(int)

    return X, y


def build_preprocessor():
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, NUMERIC_FEATURES),
        ("categorical", categorical_pipeline, CATEGORICAL_FEATURES)
    ])

    return preprocessor


if __name__ == "__main__":
    X, y = load_data()

    print("Features shape:", X.shape)
    print("Target shape:", y.shape)
    print("\nBinary target distribution:")
    print(y.value_counts().sort_index())

    print("\nMissing values:")
    print(X.isnull().sum()[X.isnull().sum() > 0])

    print("\nPreprocessor created successfully.")
