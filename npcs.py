# content/npcs.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# NPC INTERACTIONS

from security.security import audit_log
from systems.inventory import add_item


def interact_guard(state):
    audit_log("NPC_INTERACTION", "SUCCESS", "NPC=FacilityGuard")
    print("Guard: 'Check the manager terminal. It may show where the keycard is hidden.'")
    state["flags"]["guard_clue"] = True


def interact_manager_log(state):
    audit_log("NPC_INTERACTION", "SUCCESS", "NPC=FormerManagerLog")
    print("Manager Log: 'The blue keycard is hidden in my desk drawer. The map shows the loading bay route.'")
    add_item(state, "Facility Map")


def interact_ai_voice(state):
    audit_log("NPC_INTERACTION", "SUCCESS", "NPC=SecurityAI")
    print("Security AI: 'Terminal password reminder: facility opening year.'")
    add_item(state, "Terminal Password Clue")


def interact_scientist(state):
    audit_log("NPC_INTERACTION", "SUCCESS", "NPC=TrappedScientist")
    print("Scientist: 'Thank you. Take this code and injector. The tunnel is behind the medical wing.'")
    add_item(state, "Tunnel Access Code")
    add_item(state, "Energy Injector")
    state["flags"]["scientist_saved"] = True


def interact_drone(state):
    audit_log("NPC_INTERACTION", "SUCCESS", "NPC=SecurityDrone")
    print("Drone: 'Target detected. Identify yourself immediately.'")


NPC_HANDLERS = {
    "guard": interact_guard,
    "manager_log": interact_manager_log,
    "ai_voice": interact_ai_voice,
    "scientist": interact_scientist,
    "drone": interact_drone,
}
