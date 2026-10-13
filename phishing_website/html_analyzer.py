import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def analyze_html(source):

    result = {
        "has_password_field": 0,
        "has_login_form": 0,
        "has_external_form_submit": 0,
        "has_hidden_fields": 0,
        "iframe_count": 0,
        "script_count": 0,
        "external_link_count": 0
    }

    try:

        # ==============================
        # Local HTML file
        # ==============================

        if source.startswith("file://"):

            file_path = source.replace("file:///", "")
            file_path = file_path.replace("%20", " ")

            with open(file_path, "r", encoding="utf-8") as file:
                html = file.read()

            page_domain = ""

        # ==============================
        # Online website
        # ==============================

        else:

            response = requests.get(
                source,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            html = response.text
            page_domain = urlparse(source).netloc

        # ==============================
        # Parse HTML
        # ==============================

        soup = BeautifulSoup(html, "html.parser")

        # ==============================
        # Password field
        # ==============================

        password_fields = soup.find_all(
            "input",
            {"type": "password"}
        )

        if password_fields:
            result["has_password_field"] = 1

        # ==============================
        # Forms
        # ==============================

        forms = soup.find_all("form")

        for form in forms:

            form_text = form.get_text(
                " ",
                strip=True
            ).lower()

            if "login" in form_text or "sign in" in form_text:
                result["has_login_form"] = 1

            action = form.get("action")

            if action and page_domain:

                action_domain = urlparse(action).netloc

                if action_domain and action_domain != page_domain:
                    result["has_external_form_submit"] = 1

        # ==============================
        # Hidden fields
        # ==============================

        hidden_fields = soup.find_all(
            "input",
            {"type": "hidden"}
        )

        if hidden_fields:
            result["has_hidden_fields"] = 1

        # ==============================
        # Iframes
        # ==============================

        result["iframe_count"] = len(
            soup.find_all("iframe")
        )

        # ==============================
        # JavaScript
        # ==============================

        result["script_count"] = len(
            soup.find_all("script")
        )

        # ==============================
        # External links
        # ==============================

        if page_domain:

            for link in soup.find_all(
                "a",
                href=True
            ):

                href = link["href"]

                link_domain = urlparse(
                    href
                ).netloc

                if (
                    link_domain
                    and link_domain != page_domain
                ):
                    result["external_link_count"] += 1

    except Exception as e:

        print("HTML analysis error:", e)

    return result


# ==============================
# Test local HTML file
# ==============================

if __name__ == "__main__":

    test_url = (
        "file:///C:/Users/rog%20zephyrus/"
        "Downloads/phishing_website/"
        "test_phishing.html"
    )

    print("Analyzing local test HTML...")

    features = analyze_html(test_url)

    print("\nHTML Features:")

    for name, value in features.items():
        print(name, ":", value)