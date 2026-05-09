# game/__init__.py
#
# WHAT IS THIS FILE?
#   This empty-looking file is what makes the 'game' folder a Python PACKAGE.
#   Without it, Python treats the folder as just a folder — not importable.
#   With it, you can do:  from game.player import Player
#
# WHAT CAN GO HERE?
#   You can leave it empty (Python still recognises the package).
#   OR you can use it to define exactly what the package "exports" publicly
#   using __all__. We do both below.
#
# __all__ controls what gets imported when someone does:  from game import *
# It's also great documentation — it tells any reader exactly what this
# package is meant to provide.

__all__ = [
    "Player",
    "Enemy",
    "Boss",
    "spawn_enemy",
    "Room",
    "build_dungeon",
    "run_combat",
    "pick_up_item",
    "show_inventory",
    "use_item",
    "save_game",
    "load_game",
    "save_exists",
    "delete_save",
    "show_save_info",
]

# Version info — good habit for any package
__version__ = "4.0.0"
__author__  = "Tejesh"