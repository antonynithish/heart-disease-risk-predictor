
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "processed.cleveland.data"

columns = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "num"
]

df = pd.read_csv(DATA_PATH, header=None, names=columns)

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isin(["?"]).sum())

print("\n--- TARGET DISTRIBUTION ---")
print(df["num"].value_counts(dropna=False).sort_index())

print("\n--- UNIQUE TARGET VALUES ---")
print(df["num"].unique())
