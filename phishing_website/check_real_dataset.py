import pandas as pd


# Read our new dataset
df = pd.read_csv("real_url_features.csv")


print("Dataset Shape:")
print(df.shape)


print("\nColumns:")
print(df.columns.tolist())


print("\nFirst 5 rows:")
print(df.head())


print("\nLabel Counts:")
print(df["label"].value_counts())


print("\nMissing Values:")
print(df.isnull().sum())