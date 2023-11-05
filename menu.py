from player import Player
from battle import Battle


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
        battle = Battle()
        battle.battle(player)
        print('\n------------------------------\n')
        print('Tutorial Completed!')
        print('\n------------------------------\n')
        self.main_menu()

    def main_menu(self):
        print('Welcome to the Main Menu!')
