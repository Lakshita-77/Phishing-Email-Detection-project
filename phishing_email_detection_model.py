# Phishing Email Detection Model (Without Libraries)

def detect_phishing(email_text):
    phishing_score = 0

    # Common phishing keywords
    phishing_keywords = [
        "urgent", "verify", "click here", "login",
        "bank", "password", "limited time",
        "winner", "free", "account suspended",
        "update", "confirm", "security alert"
    ]

    # Check suspicious keywords
    for word in phishing_keywords:
        if word.lower() in email_text.lower():
            phishing_score += 1

    # Check for URLs
    if "http://" in email_text or "https://" in email_text:
        phishing_score += 2

    # Check for @ symbol misuse
    if "@" in email_text and ".com" not in email_text:
        phishing_score += 1

    # Capital letters check
    if email_text.isupper():
        phishing_score += 2

    # Final result
    if phishing_score >= 5:
        return "PHISHING EMAIL"
    elif phishing_score >= 3:
        return "SUSPICIOUS EMAIL"
    else:
        return "SAFE EMAIL"


# Main Program
print("===== Phishing Email Detection =====")

email = input("Paste the email content:\n")

result = detect_phishing(email)

print("\nResult:", result)