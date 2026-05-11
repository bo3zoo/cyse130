# main.py
# ESCAPE PROTOCOL - CYSE 130 Final Project

from engine.state import new_game_state
from engine.game_engine import run_game
from security.security import audit_log, get_valid_choice
from security.save_load import load_game


def main():
    print("=== ESCAPE PROTOCOL: CYSE 130 FINAL PROJECT ===")
    while True:
        print("\n1. New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = get_valid_choice("Enter a number (1-3): ", ["1", "2", "3"], scene="MainMenu")
        if choice == "1":
            run_game(new_game_state())
        elif choice == "2":
            state = load_game()
            if state:
                run_game(state)
        elif choice == "3":
            audit_log("GAME_END", "SUCCESS", "Quit from main menu")
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
