import pandas as pd

# Read the CSV file
df = pd.read_csv("url_features.csv")

# Show the dataset
print(df)

# Show number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Show column names
print("\nColumns:")
print(df.columns.tolist())

# Count each label
print("\nLabel Counts:")
print(df["label"].value_counts())