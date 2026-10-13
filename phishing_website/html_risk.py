def calculate_html_risk(features):

    score = 0
    reasons = []

    # ==============================
    # Strong indicators
    # ==============================

    if features["has_external_form_submit"] == 1:
        score += 40
        reasons.append(
            "Form submits data to an external domain"
        )

    if features["has_password_field"] == 1:
        score += 20
        reasons.append(
            "Password field detected"
        )

    if features["has_login_form"] == 1:
        score += 20
        reasons.append(
            "Login form detected"
        )

    # ==============================
    # Supporting indicators
    # ==============================

    if features["has_hidden_fields"] == 1:
        score += 5
        reasons.append(
            "Hidden form fields detected"
        )

    if features["iframe_count"] > 0:
        score += 5
        reasons.append(
            f"{features['iframe_count']} iframe(s) detected"
        )

    if features["script_count"] >= 10:
        score += 5
        reasons.append(
            f"Many JavaScript elements detected: "
            f"{features['script_count']}"
        )

    if features["external_link_count"] >= 20:
        score += 5
        reasons.append(
            f"Many external links detected: "
            f"{features['external_link_count']}"
        )

    # ==============================
    # Maximum score = 100
    # ==============================

    score = min(score, 100)

    # ==============================
    # Risk level
    # ==============================

    if score >= 60:
        risk_level = "HIGH"

    elif score >= 30:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return score, risk_level, reasons


# ==============================
# Test
# ==============================

if __name__ == "__main__":

    test_features = {

        "has_password_field": 1,

        "has_login_form": 1,

        "has_external_form_submit": 1,

        "has_hidden_fields": 1,

        "iframe_count": 1,

        "script_count": 1,

        "external_link_count": 0
    }

    score, level, reasons = calculate_html_risk(
        test_features
    )

    print(
        "HTML Risk Score:",
        score,
        "%"
    )

    print(
        "HTML Risk Level:",
        level
    )

    print("\nReasons:")

    for reason in reasons:

        print("-", reason)