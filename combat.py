
import random



def run_combat(player, enemy):
    
    # this function will handle the combat between player and enemy

    print(f"\n A wild enemy {enemy.name} appears!")
    enemy.show_stats()
    
    while player.is_alive() and not enemy.is_dead():
        print("\n --------------------------------------")
        print(f" Your HP : {player.hp} / {player.max_hp}")
        print(f" Enemy {enemy.name} HP : {enemy.hp}")
        print(" \nWhat is your plan? ")
        print("     [1] Attack the enemy.")
        print("     [2] Run away.")

        choice = input(" Enter your choice(1/2) :").strip()

        if  choice == "1":
            # player attacks the enemy

            dmg = player.roll_attack()
            enemy.take_damage(dmg)
            print(f"\n ⚔️ You have dealt {dmg} damage to the enemy {enemy.name}!")

            if enemy.is_dead():
                print(f"\n 🎉 congratulations! You have defeated the enemy {enemy.name}")
                # player gets rewarded

                player.gold += enemy.gold
                player.kills += 1

                print(f" You have found {enemy.gold} gold! (Total gold : {player.gold})")

                if player.kills % 3 == 0:
                    player.level_up()

                return "win"
        
            #  enemy fights back if it is still alive
            enemy_dmg = enemy.roll_attack()
            player.take_damage(enemy_dmg)
            print(f"\n 😈 {enemy.name} hits you for a damage {enemy_dmg}!")

            if not player.is_alive():
                print("\n 💀 You have been defeated by the enemy...")
                return "dead"
            


        elif choice == "2":
            # player tries to run away
            print("\n You  attempt to run away...")
            # 50% chance to successfully run away
            if random.random() < 0.5:
                print("\n You have successfully escaped from the enemy!")
                return "flee"
            else:
                print("\n You have failed to escape!")
                enemy_dmg = enemy.enemy_attack()
                player.take_damage(enemy_dmg)
                print(f"\n 😈 {enemy.name} hits you for a damage {enemy_dmg}! while fleeing")


                if not player.is_alive():
                    print("\n 💀 You have been defeated by the enemy while trying to flee...")
                    return "dead"


        else:
            print("\n Invalid choice. Please choose 1 or 2.")