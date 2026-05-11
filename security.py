# security/security.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# CYBER PACK: AUDIT LOGGING + INPUT VALIDATION

from datetime import datetime

LOG_FILE = "audit_log.txt"


def audit_log(event_type, result=None, details=""):
    # This function writes important game/security events into audit_log.txt.
    # Each log line includes the time, event type, result, and extra details.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    parts = [timestamp, event_type]

    # Add the result only if one is provided.
    if result:
        parts.append(result)

    # Add details only if there are extra details to record.
    if details:
        parts.append(details)

    # Join everything into one clean log line.
    line = " - ".join(parts)

    # Open the log file in append mode so old logs are not deleted.
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(line + "\n")


def get_valid_choice(prompt, valid_choices, scene="Menu"):
    # This function keeps asking the player for input until they enter a valid choice.
    # It helps stop the game from crashing or accepting wrong menu options.

    # Convert all valid choices to lowercase strings so input checking is consistent.
    valid_choices = [str(choice).lower() for choice in valid_choices]

    while True:
        try:
            # Ask the player for input and clean extra spaces.
            choice = input(prompt).strip().lower()

            # If the input is valid, return it to the game.
            if choice in valid_choices:
                return choice

            # If the input is not valid, log it and show a friendly message.
            audit_log("INPUT_INVALID", "FAIL", f'Scene={scene} Input="{choice}"')
            print(f"Invalid choice. Please enter one of these options: {', '.join(valid_choices)}.")

        except (KeyboardInterrupt, EOFError):
            # This handles cases where input is interrupted, like Ctrl+C or EOF.
            # Instead of crashing, the game logs the problem and asks again.
            audit_log("INPUT_INTERRUPTED", "FAIL", f"Scene={scene}")
            print("\nInput interrupted. Please choose again.")
