# content/story.py
# ESCAPE PROTOCOL - CYSE 130 Final Project
# STORY DATA

story_data = {
    "start": {
        "title": "Research Facility - Awakening",
        "text": """
You wake up inside a locked research facility.
Red emergency lights flash across the metal walls.
A robotic voice repeats: 'Security breach detected. Containment mode active.'
The exit doors are sealed. You need to escape.
""",
        "choices": {
            "1": ("Search nearby offices for access cards", "office_hall"),
            "2": ("Run to the server room terminal", "ai_voice"),
            "3": ("Follow a faint cry for help", "scientist_lab"),
        },
    },
    "office_hall": {
        "title": "Office Hallway",
        "text": """Dusty office doors line the hallway. You hear footsteps nearby.""",
        "choices": {
            "1": ("Enter the open office", "manager_log"),
            "2": ("Approach the hallway guard", "guard_npc"),
            "3": ("Hide and wait", "caught_ending"),
        },
    },
    "guard_npc": {
        "title": "Facility Guard",
        "text": """A guard points his flashlight at you and asks for clearance.""",
        "npc": "guard",
        "choices": {
            "1": ("Bluff and say you are emergency staff", "manager_log"),
            "2": ("Run away", "caught_ending"),
        },
    },
    "manager_log": {
        "title": "Manager Terminal Log",
        "text": """A dusty terminal contains an old emergency note from the former manager.""",
        "npc": "manager_log",
        "choices": {
            "1": ("Search the desk drawer", "manager_office"),
            "2": ("Ignore the clue and wait", "caught_ending"),
        },
    },
    "manager_office": {
        "title": "Manager Office",
        "text": """Inside the drawer you find a Blue Keycard. The loading bay route is marked on the map.""",
        "items": ["Blue Keycard"],
        "choices": {
            "1": ("Use the Blue Keycard at the loading bay", "escape_loading_bay"),
        },
    },
    "ai_voice": {
        "title": "Security AI Voice",
        "text": """The speakers crackle. The AI warns you that the password is linked to the facility opening year. A nearby monitor flashes: 'FACILITY OPENED: 2024'.""",
        "npc": "ai_voice",
        "choices": {
            "1": ("Use the clue and go to the server room", "server_room"),
            "2": ("Ignore the warning and rush forward", "drone_npc"),
        },
    },
    "server_room": {
        "title": "Server Room",
        "text": """Rows of machines hum loudly. A terminal blocks Checkpoint Gate C.""",
        "challenge": "terminal_login",
    },
    "terminal_success": {
        "title": "Terminal Access Granted",
        "text": """Security cameras shut down. Checkpoint Gate C unlocks.""",
        "choices": {
            "1": ("Escape through Checkpoint Gate C", "checkpoint_escape"),
        },
    },
    "drone_npc": {
        "title": "Security Drone",
        "text": """A drone drops from the ceiling and scans the hallway with a red laser.""",
        "npc": "drone",
        "challenge": "drone_stealth",
    },
    "scientist_lab": {
        "title": "Medical Wing",
        "text": """A trapped scientist is pinned under fallen equipment and begs for help.""",
        "choices": {
            "1": ("Help the scientist", "scientist_saved"),
            "2": ("Ignore her and enter the dark tunnel", "dark_tunnel"),
        },
    },
    "scientist_saved": {
        "title": "Scientist Rescue",
        "text": """You free the scientist from the equipment.""",
        "npc": "scientist",
        "choices": {
            "1": ("Ask about the tunnel", "scientist_warning"),
            "2": ("Leave quickly through the tunnel", "hero_escape"),
        },
    },
    "scientist_warning": {
        "title": "Scientist Warning",
        "text": """Scientist: 'Use the tunnel code at the locked door and do not turn back.'""",
        "choices": {
            "1": ("Use the tunnel access code", "hero_escape"),
        },
    },
    "dark_tunnel": {
        "title": "Dark Tunnel",
        "text": """Without the tunnel code, the tunnel door locks forever.""",
        "choices": {
            "1": ("Continue into the darkness", "trapped_ending"),
        },
    },
}


endings = {
    "escape_loading_bay": """
ENDING: Loading Bay Escape
Using the Blue Keycard, you unlock the cargo bay and escape into the night.
You survived through stealth.
""",
    "checkpoint_escape": """
ENDING: Checkpoint Override
You hacked the terminal, disabled security, and escaped through Gate C.
You survived through intelligence.
""",
    "hero_escape": """
ENDING: Hero's Escape
You saved the scientist and escaped together through the maintenance tunnel.
You survived through compassion.
""",
    "alarm_ending": """
ENDING: Security Failure
Wrong choices triggered full lockdown. Security drones surround you.
Mission failed.
""",
    "caught_ending": """
ENDING: Captured
You waited too long. Facility guards discovered your location.
Mission failed.
""",
    "trapped_ending": """
ENDING: Lost Underground
The tunnel sealed behind you. No signal. No light. No exit.
Mission failed.
""",
}


def get_scene(scene_name):
    return story_data.get(scene_name)


def get_ending(ending_name):
    return endings.get(ending_name)
