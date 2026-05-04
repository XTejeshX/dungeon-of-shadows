# This file will save the current game progress upto a point, it will handle saving and loading the game progress usnig JSON

import json
import os
from player import Player

SAVE_FILE = "savegame.json"

def save_game(player, current_room_key, dungeon):
    # saves the player object + dungeon room states to JSON.
    # dungeon is the {key : Room} dict so we capture visited/item state.

    room_states = {key: room.to_dict() for key, room in dungeon.items()} 
        
    save_data = {
        "player"        : player.to_dict(),
        "current_room"  : current_room_key,
        "room_states"   : room_states,
    }

    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(save_data, f, indent= 4)
            print(f"\n GAME SAVED! ({SAVE_FILE})")
    except IOError as e:
        print(f"\n could not save game :{e}")

def load_game(dungeon):
    #loads game state from the JSON save file, returns (player object, room_key) or (None, None) if no save exists.
    #also returns visited/items state for each room in the dungeon
    if not os.path.exists(SAVE_FILE):
        print("\n No Save file found")
        return None, None
    
    try:
        with open(SAVE_FILE,"r") as f:
            save_data = json.load(f)

            # rebuild Player from saved dict using the @classmethod
            player = Player.from_dict(save_data["Player"])
            current_room = save_data["current_room"]


            for key, state in save_data.get("room_states", {}).items():
                if key in dungeon:
                    dungeon[key].visited = state.get("visited", False)
                    dungeon[key].item    = state.get("item", dungeon[key].item)

            print(f"\n Game Loaded! Welcome back {player['name']}!")
            return player, current_room
        
    except (json.JSONDecodeError, KeyError) as e:
        print(f" Save file is corrupted: {e}")
        return None, None

def delete_save():
    # Deletes the save file, it is used afther a game is completed or upon request/call
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("\n Save file deleted! ")

def save_exists():
    # returns whether or not a save file exists
    return os.path.exists(SAVE_FILE)

def show_save_info():
    # peeks into the save file and give basic info without fully loading
    if not save_exists():
        return
    
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

            p = data["player"]
            room = data["current_room"].replace("_"," ").title()
            print(f"\n save found: {p['name']}  |   Level {p['level']}  |   Room: {room}")

    except Exception:
        print("\n Save found and could not be previewed")