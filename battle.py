import random


# noinspection PyMethodMayBeStatic
class Battle:
    def battle(self, player, monster):
        monster.monster_intro()

        while player.check_alive() and monster.check_alive():
            player_action = self.player_choice()
            if player_action == "attack":
                if self.player_turn(player, monster):
                    self.player_victory(player, monster)
                    break
            elif player_action == "run":
                print(f"{player.name} tries to runs away!")
                run_away = random.randint(1, 3)
                if run_away == 1:
                    print(f'{player.name} runs away successfully!')
                    break
                else:
                    print(f'{player.name} failed to run away!')

            # Add more options here
            if monster.check_alive():
                if self.monster_turn(monster, player):
                    break

    def player_turn(self, player, monster):
        player.player_attack(monster)
        return not monster.check_alive()

    def monster_turn(self, monster, player):
        monster.monster_attack(player)
        return not player.check_alive()

    def player_victory(self, player, monster):
        print(f'\n{player.name} has defeated the monster\n')
        monster.drop_exp(player)
        monster.drop_gold(player)
        player.check_level_up()

    def player_choice(self):
        print("\nChoose an action:\n1. Attack\n2. Run")
        choice = input("Enter your choice: ")
        if choice == "1" or choice.lower() == "attack":
            return "attack"
        elif choice == "2" or choice.lower() == "run":
            return "run"
        else:
            print("Invalid choice. Defaulting to attack.")
            return "attack"

