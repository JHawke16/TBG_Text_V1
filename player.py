import random


class Player:

    health = 0
    damage = 0
    speed = 0

    def __init__(self, name, level, gold, exp):
        self.name = name
        self.level = level
        self.gold = gold
        self.exp = exp

        # Base stats for level 1 player
        self.base_health = 50
        self.base_damage = 10
        self.base_speed = 5

        # Initialize stats based on level
        self.calculate_stats()

    def calculate_stats(self):
        # Stat increase per level
        health_increase = self.level * 15
        damage_increase = self.level * 1.5
        speed_increase = 5

        # Scale stats based on level
        self.health = self.base_health + (self.level - 1) * health_increase
        self.damage = self.base_damage + (self.level - 1) * damage_increase
        self.speed = self.base_speed + (self.level - 1) * speed_increase

    def player_stats(self):
        required_exp_for_next_level = self.calculate_required_exp()
        exp_to_next_level = required_exp_for_next_level - self.exp

        print(f'\nPlayer Name: {self.name}\n'
              f'Player Health: {self.health}\n'
              f'Player Gold: {self.gold}\n'
              f'Player Level: {self.level}\n'
              f'Player Exp: {self.exp}\n'
              f'Exp to Next Level: {exp_to_next_level}')

    def player_attack(self, monster):
        attack_damage = random.randint(self.base_damage, self.base_damage + 10)
        print(f'\n{self.name} attacks!')
        print(f'{self.name} did {attack_damage} damage to the {monster.name}')
        monster.damage_taken(attack_damage)

    def gain_exp(self, amount):
        self.exp += amount
        print(f'{self.name} has gained {amount} exp and has {self.exp} exp total!')

    def gain_gold(self, amount):
        self.gold += amount
        print(f'{self.name} has gained {amount} gold and has {self.gold} gold total!')

    def check_alive(self):
        return self.health > 0

    def damage_taken(self, damage):
        self.health -= damage
        print(f'{self.name} Health: {self.health}')
        if not self.check_alive():
            print(f'{self.name} has been defeated!')

    def calculate_required_exp(self):
        base_exp = 100
        growth_rate = 1.5
        return base_exp * (growth_rate ** (self.level - 1))

    def check_level_up(self):
        required_exp = self.calculate_required_exp()
        if self.exp >= required_exp:
            self.level_up()

    def level_up(self):
        required_exp = self.calculate_required_exp()
        self.level += 1
        self.exp -= required_exp
        self.calculate_stats()
        print(f'\n{self.name} has leveled up to level {self.level}!')
        self.player_stats()
        self.check_level_up()
