import pandas as pd

# Load the dataset
df = pd.read_csv("data/heart.csv")

# Display sample records
print("Sample records from the dataset:")
print(df.head())

# Display dataset dimensions
print("\nDataset dimensions (rows, columns):")
print(df.shape)

# Display feature names
print("\nFeature names:")
print(list(df.columns))
