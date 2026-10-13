
from urllib.parse import urlparse
from difflib import SequenceMatcher


BRANDS = {
    "google": "google.com",
    "microsoft": "microsoft.com",
    "apple": "apple.com",
    "facebook": "facebook.com",
    "instagram": "instagram.com",
    "amazon": "amazon.com",
    "paypal": "paypal.com",
    "netflix": "netflix.com",
    "youtube": "youtube.com",
    "linkedin": "linkedin.com",
    "samsung": "samsung.com",
    "naver": "naver.com"
}


def normalize_text(text):
    """Normalize common number substitutions in domain labels."""
    text = text.lower()

    substitutions = {
        "0": "o",
        "1": "l",
        "3": "e",
        "4": "a",
        "5": "s",
        "7": "t"
    }

    for number, letter in substitutions.items():
        text = text.replace(number, letter)

    return text


def detect_brand(url):

    parsed = urlparse(url)
    hostname = (parsed.hostname or "").lower().rstrip(".")

    if not hostname:
        return {
            "brand_detected": 0,
            "brand": None,
            "official_domain": None,
            "brand_impersonation": 0
        }

    # Official domains and their real subdomains are allowed.
    for brand, official in BRANDS.items():

        if hostname == official or hostname.endswith("." + official):

            return {
                "brand_detected": 1,
                "brand": brand,
                "official_domain": official,
                "brand_impersonation": 0
            }

    # Split hostname into labels, e.g. secure-google-login-example.
    labels = [
        label for label in hostname.split(".") if label
    ]

    normalized_labels = [
        normalize_text(label.replace("-", ""))
        for label in labels
    ]

    # Search for exact or similar brand names.
    for brand, official in BRANDS.items():

        for original_label, normalized_label in zip(
            labels, normalized_labels
        ):

            # Exact brand name or common number substitution.
            if normalized_label == brand:
                return {
                    "brand_detected": 1,
                    "brand": brand,
                    "official_domain": official,
                    "brand_impersonation": 1
                }

            # Similar spelling, e.g. gooogle instead of google.
            similarity = SequenceMatcher(
                None,
                normalized_label,
                brand
            ).ratio()

            if (
                len(normalized_label) >= 4
                and similarity >= 0.80
            ):
                return {
                    "brand_detected": 1,
                    "brand": brand,
                    "official_domain": official,
                    "brand_impersonation": 1
                }

        # Also detect a brand embedded in a longer domain label.
        compact_hostname = hostname.replace(".", "").replace("-", "")
        normalized_hostname = normalize_text(compact_hostname)

        if brand in normalized_hostname:
            return {
                "brand_detected": 1,
                "brand": brand,
                "official_domain": official,
                "brand_impersonation": 1
            }

    return {
        "brand_detected": 0,
        "brand": None,
        "official_domain": None,
        "brand_impersonation": 0
    }


if __name__ == "__main__":

    test_urls = [
        "https://www.google.com",
        "https://mail.google.com",
        "https://g00gle.com",
        "https://gooogle.com",
        "https://paypa1.com",
        "https://secure-google-login-example.com",
        "https://google.com.example.com",
        "https://example.com"
    ]

    for url in test_urls:
        result = detect_brand(url)

        print("\nURL:", url)
        print("Brand:", result["brand"])
        print(
            "Possible Impersonation:",
            result["brand_impersonation"]
        )
