# engine/game_engine.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# GAME ENGINE

from content.story import get_scene, get_ending
from content.npcs import NPC_HANDLERS
from systems.challenges import CHALLENGE_HANDLERS
from systems.inventory import add_item, view_inventory, use_item
from security.security import audit_log, get_valid_choice
from security.save_load import save_game


def show_help():
    print("\nCommands: choose a number, i = inventory, s = save, u = use item, q = quit")


def run_game(state):
    audit_log("GAME_START", "SUCCESS", f"Scene={state['current_scene']}")
    print("\nWelcome to ESCAPE PROTOCOL")
    show_help()

    while True:
        scene_name = state["current_scene"]

        ending_text = get_ending(scene_name)
        if ending_text:
            print("\n" + ending_text)
            audit_log("GAME_END", "SUCCESS", f"Ending={scene_name}")
            return

        scene = get_scene(scene_name)
        if not scene:
            print("Scene missing. Returning to start.")
            audit_log("SCENE_ERROR", "FAIL", f"Scene={scene_name}")
            state["current_scene"] = "start"
            continue

        print(f"\n=== {scene['title']} ===")
        print(scene["text"])

        for item in scene.get("items", []):
            add_item(state, item)

        npc_key = scene.get("npc")
        if npc_key in NPC_HANDLERS:
            NPC_HANDLERS[npc_key](state)

        challenge_key = scene.get("challenge")
        if challenge_key in CHALLENGE_HANDLERS:
            state["current_scene"] = CHALLENGE_HANDLERS[challenge_key](state)
            continue

        choices = scene.get("choices", {})
        for key, (label, _) in choices.items():
            print(f"{key}. {label}")
        print("i. View inventory")
        print("s. Save game")
        print("u. Use item")
        print("q. Quit")

        valid = list(choices.keys()) + ["i", "s", "u", "q"]
        choice = get_valid_choice("Enter choice: ", valid, scene=scene_name)

        if choice == "i":
            view_inventory(state)
        elif choice == "s":
            save_game(state)
        elif choice == "u":
            item_name = input("Enter exact item name to use: ").strip()
            use_item(state, item_name)
        elif choice == "q":
            audit_log("GAME_END", "SUCCESS", "Player quit")
            print("Game ended.")
            return
        else:
            next_scene = choices[choice][1]
            audit_log("CHOICE_MADE", "SUCCESS", f"Scene={scene_name} Choice={choice} Next={next_scene}")
            state["current_scene"] = next_scene
