from urllib.parse import urlparse
import re


def extract_features(url):

    # Parse the URL
    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path

    # 1. URL length
    url_length = len(url)

    # 2. Domain length
    domain_length = len(domain)

    # 3. Number of dots
    dots = url.count(".")

    # 4. Number of hyphens
    hyphens = url.count("-")

    # 5. Number of digits
    digits = sum(c.isdigit() for c in url)

    # 6. Number of slashes
    slashes = url.count("/")

    # 7. @ symbol
    at_symbol = url.count("@")

    # 8. Question mark
    question_mark = url.count("?")

    # 9. Equal symbol
    equal_symbol = url.count("=")

    # 10. HTTPS
    https = 1 if parsed.scheme == "https" else 0

    # 11. Check if IP address is used
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    has_ip = 1 if re.match(ip_pattern, domain) else 0

    # 12. Number of subdomains
    domain_parts = domain.split(".")
    subdomain_count = max(len(domain_parts) - 2, 0)

    # 13. Path length
    path_length = len(path)

    # 14. Suspicious words
    suspicious_words = [
        "login",
        "signin",
        "verify",
        "verification",
        "secure",
        "account",
        "update",
        "bank",
        "password",
        "confirm"
    ]

    suspicious_word = 0

    for word in suspicious_words:
        if word in url.lower():
            suspicious_word = 1
            break

    # 15. Double slash after domain
    double_slash = 1 if "//" in path else 0

    # Return all features
    return {
        "url_length": url_length,
        "domain_length": domain_length,
        "dots": dots,
        "hyphens": hyphens,
        "digits": digits,
        "slashes": slashes,
        "at_symbol": at_symbol,
        "question_mark": question_mark,
        "equal_symbol": equal_symbol,
        "https": https,
        "has_ip": has_ip,
        "subdomain_count": subdomain_count,
        "path_length": path_length,
        "suspicious_word": suspicious_word,
        "double_slash": double_slash
    }


if __name__ == "__main__":
    # Test URL
    url = "https://www.google.com"

    features = extract_features(url)

    print("URL:", url)
    print("\nExtracted Features:")

    for name, value in features.items():
        print(name, ":", value)