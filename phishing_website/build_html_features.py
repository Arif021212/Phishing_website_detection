import pandas as pd
from html_analyzer import analyze_html

# Real dataset load
df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# URL এবং original label নেওয়া
df = df[["URL", "label"]].dropna()

# Project label:
# Original UCI: 1 = Legitimate, 0 = Phishing
# Project: 0 = Legitimate, 1 = Phishing
df["project_label"] = df["label"].map({
    1: 0,
    0: 1
})

print("Dataset loaded!")
print("Total URLs:", len(df))

print("\nIMPORTANT:")
print("We will NOT download/analyze all 235,795 websites now.")
print("First we will test the HTML analysis on a small sample.")

# প্রথমে শুধু 10টি URL
sample = df.head(10).copy()

results = []

for index, row in sample.iterrows():

    url = row["URL"]

    print("\nAnalyzing:", url)

    html_features = analyze_html(url)

    result = {
        "url": url,
        "label": row["project_label"]
    }

    result.update(html_features)

    results.append(result)


html_df = pd.DataFrame(results)

html_df.to_csv(
    "html_test_features.csv",
    index=False
)

print("\n==============================")
print("HTML test dataset created!")
print("==============================")

print("\nShape:")
print(html_df.shape)

print("\nColumns:")
print(html_df.columns.tolist())

print("\nFirst rows:")
print(html_df.head())