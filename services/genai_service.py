def classify_issue(issue_text):
    issue = issue_text.lower()

    if "light" in issue or "fan" in issue or "switch" in issue:
        return "Electrical", "Medium"

    elif "wifi" in issue or "internet" in issue or "network" in issue:
        return "Network", "High"

    elif "ac" in issue or "tv" in issue or "device" in issue:
        return "Device", "Medium"

    elif "app" in issue or "software" in issue:
        return "Software", "Low"

    else:
        return "Other", "Low"
