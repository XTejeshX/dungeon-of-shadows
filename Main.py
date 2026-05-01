from player import Player
from enemy import spawn_enemy
from rooms import build_dungeon
import combat as c
import rooms as r
import inventory as inv
import save_load as sl
import random

def show_banner():
    
    print(" This is a RPG Game, WELCOME TO THIS TEXT ADVENTURE RPG! ")

def show_map():
    # Prints a simple ASCII map showing visited rooms.
    print("""
  ┌─────────────────────────────────┐
  │          DUNGEON MAP            │
  │                                 │
  │         [THRONE ROOM]           │
  │             │                   │
  │ [PRISON]─[HALLWAY]─[ARMORY]     │
  │              │          │       │
  │          [ENTRANCE]─[GUARD RM]  │
  │                                 │
  └─────────────────────────────────┘
    """)


def game_loop(player, start_room = "entrance"):

    # Main game loop with room navigation
    current_room_key = start_room
    
    print(f"\n welcome {player['name']}! your adventure awaits You. Find the Throne room to win.")
    print("Or die trying!!")
    print(" Type [sv] to save anytime.\n")

    while True:
        room = r.get_room(current_room_key)
        r.show_room(room)

        # random  boss encounter chance
        if random.random() < room["enemy_chance"]:
            print("near enemy room")
            foe = e.spawn_enemy(player["level"])
        
            # Boss room: stronger enemy
            if room.get("is_boss_room"):
                foe = {"name" : "Dungeon Boss", "hp": 150, "attack": 25, "gold": 100, "xp": 50}
                print("\n 👑 The Dungeon Boss blocks your path!")

            result = c.run_combat(player, foe)


            if result == "dead":
                print("\n =================================================")
                print("                ☠️  Game Over  ☠️                    ")
                print(f" Level reached: {player['level']} | Total kills: {player['kills']} | Gold collected: {player["gold"]}")
                print(" =================================================")
                return
        
            # Win condition: beating the boss
            if room.get("is_boss_room") and result == "win":
                print("\n =================================================")
                print("                🎉 You Win! 🎉                    ")
                print(f" Level reached: {player['level']} | Total kills: {player['kills']} | Gold collected: {player['gold']}")
                print(" =================================================")
                return




        # player action menu
        print("\n----------------------------------------")
        print("You are in a dungeon, What will you do?")
        print("     [n/s/e/w]   Move in a direction(north/south/east/west)")
        print("     [p]         Pick up item")
        print("     [u]         Use item")
        print("     [i]         Show inventory")
        print("     [m]         Show map")
        print("     [t]         Show stats")
        print("     [sv]        Save game")
        print("     [q]         Quit")
        print("----------------------------------------")
        

        choice = input("\n Enter your choice :").strip().lower()

        if choice in ("n","s","e","w"):
            direction_map = {"n": "north", "s": "south", "e": "east", "w": "west"}
            direction = direction_map[choice]
            new_room_key = r.move(current_room_key, direction)

            if new_room_key:
                current_room_key = new_room_key
            else:
                print(f"\n You can't go {direction} from here.")
        
        elif choice == "p":
            inv.pick_up_item(player, room)
        
        elif choice == "i":
            inv.show_inventory(player)

        elif choice == "u":
            inv.use_item(player)

        elif choice == "m":
            show_map()

        elif choice == "t":
            p.show_stats(player)

        elif choice == "sv":
            sl.save_game(player, current_room_key)

        elif choice == "q":
            print("\n Returning to main menu... \n")
            return

        else:
            print("\n Invalid choice")


def main():
    # game entry point
    
    show_banner()

    while True:

        # show save file info if it exists

        if sl.save_exists:
            sl.show_save_info()

        print("\n     [1]     New Game")
        print("     [2]     Continue (load save) " if sl.save_exists() else 
              "     [2]     Continue (no save found)")
        if sl.save_exists:
            print("     [3]     Delete Save")
        print("     [4]     Quit")

        choice = input("\n Enter your choice    :")

        if choice == "1":
            name = input("Enter the player's name :")

            if not name:
                name = "Hero"
            
            hero = p.create_player(name)

            hero["inventory"] = []      # Bag of consumables
            hero["weapon"] = "Fists"    # Equipped weapon
            hero["weapon_bonus"] = 0    # Bonus attack from weapon
            game_loop(hero)

        elif choice == "2":
            player, room_key = sl.load_game()

            if player:
                game_loop(player, start_room = room_key)
            else:
                print("\n There is no save file please start a new game!")

        elif choice == "3":
            sl.delete_save()
        
        elif choice == "4":
            print("\n Thanks for playing adventurer!! Visit again! \n")
            break

        else:
            print("\ninvlaid choice! please enter a valid choice.\n")


if __name__ == "__main__":
    main()