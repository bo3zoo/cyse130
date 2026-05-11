# security/save_load.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# CYBER PACK: SAVE / LOAD WITH TAMPER CHECK

import hashlib
import json
import os
from security.security import audit_log

SAVE_FILE = "savegame.json"


def hash_state(state):
    # Turn the game state into JSON text in a consistent order.
    # This makes sure the same state always produces the same hash.
    # We use SHA-256 to create a unique fingerprint of the save data.
    clean_json = json.dumps(state, sort_keys=True)
    return hashlib.sha256(clean_json.encode("utf-8")).hexdigest()


def save_game(state, filename=SAVE_FILE):
    # Save the current game state to a file.
    # Before saving, we create a hash and store it with the data.
    # This hash will be used later to check if the file was modified.
    try:
        data = {"state": state, "hash": hash_state(state)}

        # Write the state and hash into a JSON file.
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        # Record that the save was successful.
        audit_log("SAVE_ATTEMPT", "SUCCESS", f"File={filename}")

        print(f"Game saved to {filename}.")
        return True

    except Exception as error:
        # If anything goes wrong, log the error and inform the player.
        audit_log("SAVE_ATTEMPT", "FAIL", f"Reason={error}")
        print("Save failed. Please try again.")
        return False


def load_game(filename=SAVE_FILE):
    # Load a saved game and verify that it has not been changed.

    # First, make sure the save file actually exists.
    if not os.path.exists(filename):
        audit_log("LOAD_ATTEMPT", "FAIL", "Reason=NO_SAVE_FILE")
        print("No save file found.")
        return None

    try:
        # Read the JSON data from the save file.
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Get the saved game state and the stored hash.
        state = data.get("state")
        saved_hash = data.get("hash")

        # If either value is missing, the file format is invalid.
        if state is None or saved_hash is None:
            audit_log("LOAD_ATTEMPT", "FAIL", "Reason=BAD_SAVE_FORMAT")
            print("Save file is not valid.")
            return None

        # Recalculate the hash from the loaded state.
        current_hash = hash_state(state)

        # Compare the new hash with the saved hash.
        # If they do not match, the file was edited or corrupted.
        if current_hash != saved_hash:
            audit_log("LOAD_ATTEMPT", "FAIL", "Reason=SAVE_TAMPERED")
            print("WARNING: Save file was changed or tampered with. Load rejected.")
            return None

        # If the hashes match, the save file is safe to use.
        audit_log("LOAD_ATTEMPT", "SUCCESS", f"File={filename}")
        print("Save loaded successfully.")
        return state

    except Exception as error:
        # Handle damaged or unreadable save files.
        audit_log("LOAD_ATTEMPT", "FAIL", f"Reason={error}")
        print("Load failed. The save file may be damaged.")
        return None
