import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv("data/heart.csv")

# Separate features and target
X = df.drop("heart_disease", axis=1)
y = df["heart_disease"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Feature scaling (important for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler for later use (prediction & explainability)
joblib.dump(scaler, "scaler.pkl")

# Optional: Save processed datasets (good practice)
pd.DataFrame(X_train_scaled, columns=X.columns).to_csv(
    "data/X_train_processed.csv", index=False
)
pd.DataFrame(X_test_scaled, columns=X.columns).to_csv(
    "data/X_test_processed.csv", index=False
)
y_train.to_csv("data/y_train.csv", index=False)
y_test.to_csv("data/y_test.csv", index=False)

# Display shapes
print("Training data shape:", X_train_scaled.shape)
print("Testing data shape:", X_test_scaled.shape)
