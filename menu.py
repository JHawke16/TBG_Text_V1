from player import Player
from battle import Battle
from monster import Monster


# noinspection PyMethodMayBeStatic
class Menu:
    def char_creation(self):
        print('\nWelcome to TBG!')
        print('\n------------------------------\n')
        player_name = input('Please enter a name for your character: ')
        player = Player(player_name, 1, 0, 90)
        player.player_stats()
        print('\n------------------------------')
        print('\nTutorial Battle!')
        print('\n------------------------------')
        monster = Monster('Goblin', 2)
        battle = Battle()
        battle.battle(player, monster)
        print('\n------------------------------\n')
        print('Tutorial Completed!')
        print('\n------------------------------\n')
        self.main_menu()

    def main_menu(self):
        # Add main menu options
        print('Welcome to the Main Menu!')
