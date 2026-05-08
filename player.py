# player.py - Phase 4: Player as a Class
#
# WHAT CHANGED FROM PHASE 3?
#   Before : player was a plain dict  → player["hp"], player["attack"]
#   Now    : player is an object      → player.hp,    player.attack
#
# WHY IS THIS BETTER?
#   - Data (hp, gold) and behaviour (heal, level_up) live TOGETHER in one place
#   - You can't accidentally pass the wrong thing — a Player is always a Player
#   - Easy to serialize to JSON and recreate from JSON (to_dict / from_dict)

import random

class Player:

    def __init__(self, name):

        self.name           = name
        self.hp             = 100
        self.max_hp         = 100
        self.attack         = 15
        self.gold           = 0
        self.level          = 1
        self.kills          = 0
        self.inventory      = []
        self.weapon         = "Bare Hands"
        self.weapon_bonus   = 0

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
        print(f" Nice!! You healed {amount} HP! (HP: {self.hp}/{self.max_hp})")

    def roll_attack(self):
        # returns a random attack value based on current attack value
        return random.randint(max(1, self.attack - 3), self.attack + 3)
    
    def level_up(self):
        # improve stats of player
        self.level      += 1
        self.max_hp     += 20
        self.attack     += 5
        self.hp         = self.max_hp
        print(f"player has leveled up {self.level}")
        print(f"  Max HP increased to: {self.max_hp}  |  Attack increased to: {self.attack}")

    def show_stats(self):
        # shows player stats
        print("===== CURRENT PLAYER STATS =====")
        print(f" Name    : {self.name}")
        print(f" Level   : {self.level}")
        print(f" HP      : {self.hp} / {self.max_hp}")
        print(f" Attack  : {self.attack} (weapon    :{self.weapon})")
        print(f" Gold    : {self.gold}")
        print(f" Kills   : {self.kills}")
        print("================================\n")


    #  Serialisation — convert to/from plain dict for JSON save files  #
    def to_dict(self):
        return{
            "name"          : self.name,
            "hp"            : self.hp,
            "max_hp"        : self.max_hp,
            "attack"        : self.attack,
            "gold"          : self.gold,
            "level"         : self.level,
            "kills"         : self.kills,
            "inventory"     : self.inventory,
            "weapon"        : self.weapon,
            "weapon_bonus"  : self.weapon_bonus            
        }


    #  @classmethod — called on the CLASS, not an instance.               #
    #  Used here as a second constructor:  Player.from_dict(data)         #

    @classmethod
    def from_dict(cls, data):
        # recreates a player object from a saved dict
        player              = cls(data["name"])
        player.hp           = data["hp"]
        player.max_hp       = data["max_hp"]
        player.attack       = data["attack"]
        player.gold         = data["gold"]
        player.level        = data["level"]
        player.kills        = data["kills"]
        player.inventory    = data.get("inventory", [])
        player.weapon       = data.get("weapon", "Bare Hands")
        player.weapon_bonus = data.get("weapon_bonus", 0)
        
        return player
    

    # __str__ — what Python prints when you do  print(player)  
    def __str__(self):
        return f"Player {self.name}, Level :{self.level},   HP: {self.hp}/{self.max_hp}"