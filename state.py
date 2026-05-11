# engine/state.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# GAME STATE

def new_game_state():
    return {
        "current_scene": "start",
        "inventory": [],
        "health": 75,
        "flags": {
            "guard_clue": False,
            "terminal_hacked": False,
            "scientist_saved": False,
        },
    }
