# Handles everything about enemies

# enemy.py - Phase 4: Enemy as a Class + Boss inherits from Enemy
#
# NEW CONCEPT: INHERITANCE
#   Boss is a special Enemy. Instead of rewriting everything,
#   Boss INHERITS all of Enemy's methods and only overrides what's different.
#   This is the "is-a" relationship: a Boss IS-A Enemy.

import random

# Templates stay as data — the class uses them to build instances
ENEMY_TYPE = [
    {"name": "Goblin",      "hp": 30,   "attack": 8,    "gold": 5,  "xp": 1},
    {"name": "Orc",         "hp": 50,   "attack": 10,   "gold": 10, "xp": 2},
    {"name": "Skeleton",    "hp": 40,   "attack": 12,   "gold": 7,  "xp": 1},
    {"name": "Troll",       "hp": 80,   "attack": 18,   "gold": 20, "xp": 3},
    {"name": "Dark Mage",   "hp": 35,   "attack": 20,   "gold": 25, "xp": 3}
]


class Enemy:

    def __init__(self, name, hp, attack, gold, xp):
        self.name   = name
        self.hp     = hp
        self.attack = attack
        self.gold   = gold
        self.xp     = xp
        

    def is_dead(self):
        return self.hp <= 0
    
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def roll_attack(self):
        return random.randint(max(1, self.attack - 3 ), self.attack + 3)
    
    def show_stats(self):
        print(f"  👿  Enemy: {self.name}  |   HP : {self.hp}  | ATTACK:{self.attack}")
    
    def __str__(self):
        return f"Enemy({self.name}, HP {self.hp})"
    



#  INHERITANCE: Boss(Enemy) means Boss gets ALL of Enemy's methods
#  for free. We only override what's different.

class Boss(Enemy):
    # A powerfull boss appears and inherits from Enemy
    def __init__(self):
        # super().__init__() calls Enemy's __init__ so we don't repeat it
        super().__init__(
            name    = "Dungeon Boss",
            hp      = 150,
            attack  = 25,
            gold    = 100,
            xp      = 10
        )
        self.phase = 1  # Bosses have 2 phases — unique to Boss!

    def roll_attack(self):
        
        if self.phase == 1 and self.hp < 75:
            self.phase = 2
            print("boss phase 2 begins!")

        multiplier = 1.5 if self.phase == 2 else 1.0
        base = random.randint(max(1, self.attack - 3 ), self.attack + 3)
        return int(base * multiplier)

    def show_stats(self):
        print(f"  👑  Enemy: {self.name}  |   HP : {self.hp}  | ATTACK:{self.attack} |   PHASE:{self.phase}")




#  Factory function — creates the right type of enemy automatically   #
def spawn_enemy(player_level= 1, is_boss= False):

    # Returns an Enemy or Boss instance.
    # player_level controls which enemies can appear.

    if is_boss:
        return Boss()
    # as level increases the difficulty of the enemy also increases
    max_index = min(player_level + 1, len(ENEMY_TYPE))
    template = random.choice(ENEMY_TYPE[:max_index])
    return Enemy(**template) # ** unpacks the dict as keyword arguments 
    
