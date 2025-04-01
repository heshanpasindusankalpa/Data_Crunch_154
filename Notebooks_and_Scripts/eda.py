import pandas as pd

# Load dataset (update filename accordingly)
df = pd.read_csv("train.csv")

# Display basic info
print("Dataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
