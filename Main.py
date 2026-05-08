from player import Player
from enemy import spawn_enemy
from rooms import build_dungeon
from combat import run_combat
from inventory import pick_up_item, show_inventory, use_item
import random
import save_load as sl


def show_banner():
    print("""
╔══════════════════════════════════════╗
║                                      ║
║      ⚔️   DUNGEON OF SHADOWS  ⚔️    ║
║      Text Adventure RPG  v4.0        ║
║                                      ║
╚══════════════════════════════════════╝
    """)

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


def game_loop(player, dungeon, start_room = "entrance"):

    # Main game loop with room navigation
    current_room_key = start_room
    last_room_key = None
    
    print(f"\n welcome {player.name}! your adventure awaits You. Find the Throne room to win.")
    print("Or die trying!!")
    print(" Type [sv] to save anytime.\n")

    while True:
        room = dungeon[current_room_key]

        just_entered = (current_room_key != last_room_key)      #only run entry logic when we moved into a new room

        if just_entered:
            last_room_key = current_room_key
            room.show()

            if random.random() < room.enemy_chance:
                foe = spawn_enemy(player.level, is_boss=room.is_boss_room)

                if room.is_boss_room:
                    print("\n 👑 The Dungeon Boss blocks your path!")

                result = run_combat(player, foe)

                if result == "dead":
                    print("\n =================================================")
                    print("                ☠️  Game Over  ☠️                    ")
                    print(f" Level reached: {player.level} | Total kills: {player.kills} | Gold collected: {player.gold}")
                    print(" =================================================")
                    sl.delete_save()
                    return
                
                if room.is_boss_room and result == "win":
                    print("\n =================================================")
                    print("                🎉 You Win! 🎉                    ")
                    print(f" Level reached: {player.level} | Total kills: {player.kills} | Gold collected: {player.gold}")
                    print(" =================================================")
                    sl.delete_save()
                    return
                
                if result in ("win", "flee"):
                    print("\n ⚔️ The dust settles. You are still in the dungeon.")

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
        print("     [q]         Quit to menu")
        print("----------------------------------------")
        

        choice = input("\n Enter your choice :").strip().lower()

        if choice in ("n","s","e","w"):
            directions = {"n": "north", "s": "south", "e": "east", "w": "west"}
            new_key = room.get_exit(directions[choice])

            if new_key:
                current_room_key = new_key
            else:
                print(f"\n No exit in the mentioned direction")
            
        
        elif choice == "p":
            pick_up_item(player, room)
        
        elif choice == "i":
            show_inventory(player)

        elif choice == "u":
            use_item(player)

        elif choice == "m":
            show_map()

        elif choice == "t":
            player.show_stats()

        elif choice == "sv":
            sl.save_game(player, current_room_key, dungeon)

        elif choice == "q":
            print("\n Returning to main menu... \n")
            return

        else:
            print("\n Invalid choice")


def main():
    # game entry point
    
    show_banner()

    # build dungeon once
    dungeon =  build_dungeon()

    while True:

        # show save file info if it exists

        if sl.save_exists():
            sl.show_save_info()

        print("\n     [1]     New Game")
        print("     [2]     Continue (load save) " if sl.save_exists() else 
              "     [2]     Continue (no save found)")
        if sl.save_exists():
            print("     [3]     Delete Save")
        print("     [4]     Quit")

        choice = input("\n Enter your choice    :").strip()

        if choice == "1":
            name = input("Enter the player's name :").strip() or "Hero"
            player = Player(name)
            dungeon = build_dungeon()
            game_loop(player, dungeon)


        elif choice == "2":

            dungeon = build_dungeon()
            player, room_key = sl.load_game(dungeon)

            if player:
                game_loop(player, dungeon, start_room = room_key)
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