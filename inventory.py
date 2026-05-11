# systems/inventory.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# INVENTORY SYSTEM

from security.security import audit_log

ITEM_DESCRIPTIONS = {
    "Blue Keycard": "Unlocks the loading bay exit.",
    "Facility Map": "Reveals safe routes and hidden areas.",
    "Terminal Password Clue": "Helps solve the server terminal puzzle.",
    "Tunnel Access Code": "Unlocks the maintenance tunnel door.",
    "Energy Injector": "Heals you during danger.",
    "Encrypted USB": "Can override security checkpoint systems.",
}


def add_item(state, item):
    if item not in state["inventory"]:
        state["inventory"].append(item)
        print(f"Item collected: {item}")
        audit_log("ITEM_COLLECTED", "SUCCESS", f"Item={item}")


def has_item(state, item):
    return item in state["inventory"]


def remove_item(state, item):
    if item in state["inventory"]:
        state["inventory"].remove(item)
        return True
    return False


def view_inventory(state):
    print("\n=== INVENTORY ===")
    if not state["inventory"]:
        print("Your inventory is empty.")
    else:
        for item in state["inventory"]:
            print(f"- {item}: {ITEM_DESCRIPTIONS.get(item, 'Useful story item.')}")
    print(f"Health: {state['health']}")
    print("=================\n")


def use_item(state, item):
    if not has_item(state, item):
        print(f"You do not have {item}.")
        audit_log("ITEM_USED", "FAIL", f"Item={item}")
        return False
    if item == "Energy Injector":
        state["health"] = min(100, state["health"] + 25)
        remove_item(state, item)
        print("You use the Energy Injector and recover 25 health.")
        audit_log("ITEM_USED", "SUCCESS", f"Item={item}")
        return True
    print(f"{item} cannot be used manually right now. It works during the correct story event.")
    audit_log("ITEM_USED", "FAIL", f"Item={item} Reason=WrongTime")
    return False
