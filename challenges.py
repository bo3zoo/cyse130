# systems/challenges.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# CHALLENGES

from security.security import audit_log, get_valid_choice
from systems.inventory import add_item, has_item, use_item


def terminal_login_challenge(state):
    print("\n=== CHALLENGE: TERMINAL LOGIN ===")
    print("The terminal asks for the facility opening year.")
    print("Hint: The answer is shown in the AI clue.")
    attempts = 0
    while attempts < 3:
        attempts += 1
        answer = input("Enter password: ").strip()
        if answer == "2024":
            audit_log("CHALLENGE_ATTEMPT", "SUCCESS", f"Puzzle=TerminalLogin Attempts={attempts}")
            print("Access granted. Security cameras disabled.")
            add_item(state, "Encrypted USB")
            state["flags"]["terminal_hacked"] = True
            return "terminal_success"
        audit_log("CHALLENGE_ATTEMPT", "FAIL", f"Puzzle=TerminalLogin Attempts={attempts}")
        print("Incorrect password.")
    return "alarm_ending"


def drone_stealth_challenge(state):
    print("\n=== CHALLENGE: SECURITY DRONE ===")
    print("A drone scans the hallway. You must react fast.")
    print("1. Hide behind the server racks")
    print("2. Run into the open hallway")
    print("3. Use Energy Injector and sprint")
    choice = get_valid_choice("Choose 1-3: ", ["1", "2", "3"], scene="DroneChallenge")
    if choice == "1":
        audit_log("CHALLENGE_ATTEMPT", "SUCCESS", "Puzzle=DroneStealth Method=Hide")
        print("The drone loses your signal.")
        return "server_room"
    if choice == "3" and has_item(state, "Energy Injector"):
        use_item(state, "Energy Injector")
        audit_log("CHALLENGE_ATTEMPT", "SUCCESS", "Puzzle=DroneStealth Method=Injector")
        print("You sprint past the drone and reach the server room.")
        return "server_room"
    audit_log("CHALLENGE_ATTEMPT", "FAIL", "Puzzle=DroneStealth")
    return "alarm_ending"


CHALLENGE_HANDLERS = {
    "terminal_login": terminal_login_challenge,
    "drone_stealth": drone_stealth_challenge,
}
