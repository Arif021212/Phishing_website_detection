def calculate_brand_risk(brand_result):

    score = 0
    reasons = []

    # =================================
    # Brand impersonation
    # =================================

    if brand_result["brand_impersonation"] == 1:

        score += 80

        brand = brand_result["brand"]

        reasons.append(
            f"Possible {brand} brand impersonation detected"
        )

    # =================================
    # Known brand detected
    # =================================

    elif brand_result["brand_detected"] == 1:

        reasons.append(
            f"Known brand detected: "
            f"{brand_result['brand']}"
        )

    # =================================
    # Risk Level
    # =================================

    if score >= 60:

        risk_level = "HIGH"

    elif score >= 30:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    return score, risk_level, reasons


# =================================
# Test
# =================================

if __name__ == "__main__":

    test_result = {
        "brand_detected": 1,
        "brand": "google",
        "official_domain": "google.com",
        "brand_impersonation": 1
    }

    score, level, reasons = (
        calculate_brand_risk(
            test_result
        )
    )

    print(
        "Brand Risk Score:",
        score,
        "%"
    )

    print(
        "Brand Risk Level:",
        level
    )

    print(
        "\nBrand Risk Reasons:"
    )

    if reasons:

        for reason in reasons:

            print(
                "-",
                reason
            )

    else:

        print(
            "- No brand impersonation detected"
        )