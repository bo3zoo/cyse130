# security/save_load.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# CYBER PACK: SAVE / LOAD WITH TAMPER CHECK

import hashlib
import json
import os
from security.security import audit_log

SAVE_FILE = "savegame.json"


def hash_state(state):
    clean_json = json.dumps(state, sort_keys=True)
    return hashlib.sha256(clean_json.encode("utf-8")).hexdigest()


def save_game(state, filename=SAVE_FILE):
    try:
        data = {"state": state, "hash": hash_state(state)}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        audit_log("SAVE_ATTEMPT", "SUCCESS", f"File={filename}")
        print(f"Game saved to {filename}.")
        return True
    except Exception as error:
        audit_log("SAVE_ATTEMPT", "FAIL", f"Reason={error}")
        print("Save failed. Please try again.")
        return False


def load_game(filename=SAVE_FILE):
    if not os.path.exists(filename):
        audit_log("LOAD_ATTEMPT", "FAIL", "Reason=NO_SAVE_FILE")
        print("No save file found.")
        return None
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        state = data.get("state")
        saved_hash = data.get("hash")
        if state is None or saved_hash is None:
            audit_log("LOAD_ATTEMPT", "FAIL", "Reason=BAD_SAVE_FORMAT")
            print("Save file is not valid.")
            return None
        current_hash = hash_state(state)
        if current_hash != saved_hash:
            audit_log("LOAD_ATTEMPT", "FAIL", "Reason=SAVE_TAMPERED")
            print("WARNING: Save file was changed or tampered with. Load rejected.")
            return None
        audit_log("LOAD_ATTEMPT", "SUCCESS", f"File={filename}")
        print("Save loaded successfully.")
        return state
    except Exception as error:
        audit_log("LOAD_ATTEMPT", "FAIL", f"Reason={error}")
        print("Load failed. The save file may be damaged.")
        return None
