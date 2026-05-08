# This file will save the current game progress upto a point, it will handle saving and loading the game progress usnig JSON

import json
import os
from player import Player



_GAME_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(_GAME_DIR, "savegame.json")

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

def _extract_player_dict(data):
    """
    Tries to find the player dict from the loaded JSON.
    Handles multiple formats:
      - Phase 4:  {"player": {...}, "current_room": ..., "room_states": ...}
      - Phase 3:  {"player": {...}, "current_room": ...}  (no room_states)
      - Old/bad:  {"Player": {...}, ...}  (capital P)
      - Flat:     {"name": ..., "hp": ...}  (player IS the top level)
    """

    if "player" in data:
        return data["player"]
    
    if "Player" in data:
        return data["Player"]
    
    if "name" in data and "hp" in data and "level" in data:
        return data
    
    return None


def load_game(dungeon):
    if not os.path.exists(SAVE_FILE):
        print("\n No Save file found")
        return None, None
    
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"\n Save file not valid JSON: {e}")
        return None, None
    
    player_data = _extract_player_dict(data)

    if player_data is None:
        print("\n  ❌ Save file has an unexpected format.")
        return None, None
    
    # FIX: Use lowercase 'player_obj' to avoid overwriting the 'Player' class
    try:
        player_obj = Player.from_dict(player_data)
    except Exception as e:
        print(f"\n  ❌ Player data is incomplete: {e}")
        return None, None

    # --- Get current room ---
    current_room = data.get("current_room", "entrance")

    if current_room not in dungeon:
        print(f"\n  ⚠️  Saved room '{current_room}' not found — starting from entrance.")
        current_room = "entrance"
 
    # --- Restore room states ---
    for key, state in data.get("room_states", {}).items():
        if key in dungeon:
            dungeon[key].visited = state.get("visited", False)
            # Be careful here: if the player already picked up the item, 
            # ensure your room.to_dict() / from_dict handles None correctly.
            dungeon[key].item = state.get("item", dungeon[key].item)
 
    # FIX: Reference the correct variable 'player_obj'
    print(f"\n  ✅ Loaded! Welcome back, {player_obj.name}!")
    return player_obj, current_room



def delete_save():
    # Deletes the save file, it is used afther a game is completed or upon request/call
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("\n Save file deleted! ")

def save_exists():
    # returns whether or not a save file exists
    return os.path.exists(SAVE_FILE)

def show_save_info():
    if not save_exists():
        return
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        player_data = _extract_player_dict(data)
        if player_data:
            room = data.get("current_room", "?").replace("_", " ").title()
            print(f"\n  📂 Save: {player_data['name']}  |  "
                  f"Level {player_data['level']}  |  Room: {room}")
        else:
            print("\n  📂 Save found (unreadable format)")
    except Exception:
        print("\n  📂 Save found (could not preview)")