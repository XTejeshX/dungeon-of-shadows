# this file will contain about the code of items pickup and usage etc
# Each item has an name description and effect.

ITEMS = {
    "torch": {
        "name": "Torch",
        "description": "Lights up dark room. No Combat use.",
        "effect": "none"
    },
    "health_potion": {
        "name": "Health Potion",
        "description": "Heals and restores 40 HP to player when used.",
        "effect": "heal",
        "value" : 40
    },
    "rusty_sword": {
        "name": "RUSTY SWORD",
        "description": "An old sword which fuctions. +5 Attack",
        "effect": "attack_boost",
        "value" : 5
    },
    "steel_sword": {
        "name": "Steel Sword",
        "description": "A sharp, well-balanced blade. +12 attack",
        "effect": "attack_boost",
        "value" : 40
    },
    "gold_pouch": {
        "name": "Gold Pouch",
        "description": "A pouch filled with 30 gold coins.",
        "effect": "gold",
        "value" : 30
    }
}


def pick_up_item(player, room):
    """
    Handles the logic for interacting with items in a room.
    Determines if an item exists, applies its effects, and updates the player state.
    """

    # 1. CHECK FOR ITEM PRESENCE

    if not room.item:
        print("There is nothing in this room to loot.")
        return

    # 2. RETRIEVE ITEM DATA
    # We use the key (like "iron_sword") to look up the full item details 
    # from a global ITEMS dictionary.
    item = ITEMS[room.item]
    

    # Provide immediate feedback to the player about what they found.
    print(f"You have picked up {item['name']}")
    print(f"    {item['description']}")


    # 3. HANDLE DIFFERENT ITEM EFFECTS
    effect = item["effect"]
    # CASE A: THE ITEM IS GOLD
    if effect == "gold":
        # Add the item's value directly to the player's currency balance.
        player.gold += item["value"]
        print(f"    💰+{item['value']} gold!, the player now has a total of {player.gold}")
    
    # CASE B: THE ITEM IS A WEAPON (ATTACK BOOST)
    elif effect == "attack_boost":
        if item["value"] > player.weapon_bonus:
            gain = item["value"] - player.weapon_bonus
            player.attack += gain          
            player.weapon_bonus = item["value"]  
            player.weapon = item["name"]         
            
            print(f" ⚔️  Equipped attack:  {player.attack}")
        else:
            # If the item is weaker, we don't change stats; the player just leaves it.
            print("You already have a better weapon")
    
    # CASE C: THE ITEM IS A CONSUMABLE (HEAL)
    elif effect == "heal":
        # Potions are not used immediately; they are added to the 'inventory' list.
        # This allows the player to use them later during combat or exploration.
        player.inventory.append(room.item)
        print(" Added the item into the bag. Use it from the inventory menu")
    
    # CASE D: THE ITEM IS A QUEST ITEM OR MISC (NONE)
    elif effect == "none":
        # Items with no direct stat effect are simply moved to the player's inventory.
        player.inventory.append(room.item)

    # 4. CLEANUP
    # After the player interacts with the item (picks it up or equips it), 
    # we set the room's item to None so they can't loot the same room twice.
    room.item = None



def show_inventory(player):
    # displays users inventory

    print("---------------PLAYER INVENTORY---------------------")
    print(f" Weapon  : {player.weapon}")
    print(f" Gold    : {player.gold}")
    
    #bag = player.inventory

    if not player.inventory:
        print("     BAG : (EMPTY)")
    else:
        print("     BAG:")
        for i, item_key in enumerate(player.inventory):
            item = ITEMS[item_key]
            print(f"     [{i+1}] {item['name']} - {item['description']}")
    


def use_item(player):
    # it lets the player use an item from the inventory if available, returns true if item was used, False otherwise.


    usable = [(i, k) for i, k in enumerate(player.inventory) if ITEMS[k]["effect"] == "heal"]

    if not usable:
        print("\n There is no usable item in your bag.")
        return False
    

    print("\n Which item would you like to use?")
    for i, key in usable:
        item = ITEMS[key]
        print(f"    [{i + 1}] {ITEMS[key]['name']}")

    choice = input(" Enter number (or 0 to cancel):").strip()

    if choice == 0:
        return False
    
    try:
        index = int(choice) - 1
        item_key = player.inventory[index]
        item = ITEMS[item_key]

        if item["effect"] == "heal":
            player.heal(item["value"])
            player.inventory.pop(index)
            return True

    except (ValueError, IndexError):
        print(" Invalid choice! Please enter a valid one.")
    
    return False