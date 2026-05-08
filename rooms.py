# rooms.py - Defines the dungeon map and room navigation

class Room:
    #   shows one location in the dungeon
    def __init__(self, name, description, exits, item = None, enemy_chance = 0.0, is_boss_room = False):
        self.name           = name
        self.description    = description
        self.exits          = exits
        self.item           = item
        self.enemy_chance   = enemy_chance
        self.is_boss_room   = is_boss_room
        self.visited        = False
    
    def show(self):

        print(f"\n  {self.name}")
        # displays the room description, exits, and any items
        print(f"    {self.description}")
        # Show exits
        print(f"\n  Exits:  {', '.join(self.exits.keys())}")

        if self.item:
            item_name = self.item.replace("_", " ").title()
            print(f" You spot an {item_name} on the ground!")
        
        if not self.visited:
            print("\n This is your first time here.")
            self.visited = True

    def get_exit(self, direction):
        # returns the room key in the given direction or None will be returned
        return self.exits.get(direction)
    
    def to_dict(self):
        return{
            "item"      :   self.item,
            "visited"   :   self.visited
        }
    
    def __str__(self):
        return f"Room({self.name})"


def build_dungeon():
    # a dictionary of room objects keyed by a short string id
    return {
        "entrance": Room(
            name        ="Dungeon Entrance",
            description ="A dimly lit entrance with moss-covered walls. The air is damp and musty and smells of rot.",
            exits       = {"north": "hallway", "east": "guard_room"},
            item        = "torch",
            enemy_chance= 0.0,
        ),
        "hallway": Room(
            name        = "Dark Hallway",
            description = "A long corridor. Bones crunch underfoot. Shadows move at the far end.",
            exits       = {"south": "entrance", "north": "throne_room", "east": "armory", "west": "prison"},
            item        = "health_potion",
            enemy_chance= 0.4,
        ),
        "guard_room": Room(
            name        = "Guard Room",
            description = "An abandoned guard post. A rusty sword hangs ont the wall.",
            exits       = {"west": "entrance", "north": "armory"},
            item        = "rusty_sword",
            enemy_chance= 0.6,
        ),
        "armory": Room(
            name        = "Armory",
            description = " An old room filled with weapons racked along the walls. Most are broken, but a few are usable.",
            exits       = {"west": "hallway", "south": "guard_room"},
            item        =  "steel_sword",
            enemy_chance= 0.5,
        ),
        "prison": Room(
            name        = "Prison Cells",
            description = " Rows of empty cells. Chains dangle from the ceiling. Something growls nearby.",
            exits       = {"east": "hallway"},
            item        =  "gold_pouch",
            enemy_chance= 0.8,
        ),
        "throne_room": Room(
            name        = " 💀 THRONE ROOM (BOSS)",
            description = " A massive chamber. A rotting throne sits at the center. This is the final room",
            exits       = { "south": "hallway"},
            item        =  None,
            enemy_chance= 1.0,
            is_boss_room= True
        )
    }