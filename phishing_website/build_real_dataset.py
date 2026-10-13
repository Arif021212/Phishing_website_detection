import pandas as pd
from feature_extractor import extract_features


# Read the real dataset
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

print("Original dataset shape:", df.shape)


# Keep only URL and label
df = df[["URL", "label"]].dropna()


# Convert labels
# Original dataset:
# 1 = Legitimate
# 0 = Phishing
#
# Our project:
# 0 = Legitimate
# 1 = Phishing

df["project_label"] = df["label"].map({
    1: 0,
    0: 1
})


# Extract URL features
feature_data = df["URL"].apply(extract_features).apply(pd.Series)


# Add URL
feature_data.insert(0, "url", df["URL"].values)


# Add project label
feature_data["label"] = df["project_label"].values


# Save new dataset
output_file = "real_url_features.csv"

feature_data.to_csv(output_file, index=False)


print("\nDataset created successfully!")
print("File:", output_file)
print("New dataset shape:", feature_data.shape)

print("\nLabel counts:")
print(feature_data["label"].value_counts())