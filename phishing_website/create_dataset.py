import csv
from feature_extractor import extract_features


# Test URLs
data = [
    ("https://www.google.com", 0),
    ("https://www.youtube.com", 0),
    ("https://www.facebook.com", 0),

    ("http://paypal-login-example.com/account/login", 1),
    ("http://secure-bank-login-example.com/verify", 1),
    ("http://free-prize-example.com/winner", 1)
]


# CSV file
output_file = "url_dataset_15_features.csv"


# Feature names
feature_names = [
    "url_length",
    "domain_length",
    "dots",
    "hyphens",
    "digits",
    "slashes",
    "at_symbol",
    "question_mark",
    "equal_symbol",
    "https",
    "has_ip",
    "subdomain_count",
    "path_length",
    "suspicious_word",
    "double_slash"
]


# Create CSV
with open(output_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["url"] + feature_names + ["label"])

    # Process each URL
    for url, label in data:

        features = extract_features(url)

        row = [url]

        for feature in feature_names:
            row.append(features[feature])

        row.append(label)

        writer.writerow(row)


print("Dataset created successfully!")
print("File:", output_file)