# security/security.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# CYBER PACK: AUDIT LOGGING + INPUT VALIDATION

from datetime import datetime
# Main audit log file used for security-related events
LOG_FILE = "audit_log.txt"


def audit_log(event_type, result=None, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [timestamp, event_type]
    if result:
        parts.append(result)
    if details:
        parts.append(details)
    line = " - ".join(parts)
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(line + "\n")


def get_valid_choice(prompt, valid_choices, scene="Menu"):
    valid_choices = [str(choice).lower() for choice in valid_choices]
    while True:
        try:
            choice = input(prompt).strip().lower()
            if choice in valid_choices:
                return choice
            audit_log("INPUT_INVALID", "FAIL", f'Scene={scene} Input="{choice}"')
            print("Invalid choice. Please try again.")
        except (KeyboardInterrupt, EOFError):
            audit_log("INPUT_INTERRUPTED", "FAIL", f"Scene={scene}")
            print("\nInput interrupted. Please choose again.")
