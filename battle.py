from monster import Monster


class Battle:
    def battle(self, player):
        monster = Monster('Goblin', 2)
        monster.monster_intro()

        while player.check_alive() and monster.check_alive():
            # Future implementation of player's choice goes here

            if player.speed >= monster.speed:
                if self.player_turn(player, monster):
                    self.player_victory(player, monster)
                    break
                if self.monster_turn(monster, player):
                    break
            else:
                if self.monster_turn(monster, player):
                    break
                if self.player_turn(player, monster):
                    self.player_victory(player, monster)
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
