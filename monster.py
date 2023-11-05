import random


class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level

        # Base stats for level 1 monster
        base_health = 20
        self.base_damage = 5
        base_speed = 3
        base_gold = 10
        base_exp = 15

        # Stat increase per level
        health_increase = 10
        damage_increase = 2
        speed_increase = 1
        gold_increase = 5
        exp_increase = 10

        # Scale stats based on level
        self.health = base_health + (level - 1) * health_increase
        self.damage = self.base_damage + (level - 1) * damage_increase
        self.speed = base_speed + (level - 1) * speed_increase
        self.gold = base_gold + (level - 1) * gold_increase
        self.exp = base_exp + (level - 1) * exp_increase

    def monster_intro(self):
        print(f'\nA wild {self.name} approaches\n'
              f'Monster Level: {self.level}')

    def monster_attack(self, player):
        attack_damage = random.randint(self.base_damage, self.base_damage + 5)
        print('\nThe monster attacks')
        print(f'The monster did {attack_damage} to {player.name}')
        player.damage_taken(attack_damage)

    def drop_exp(self, player):
        print(f'The monster drops {self.exp} exp!')
        player.gain_exp(self.exp)

    def drop_gold(self, player):
        print(f'The monster drops {self.gold} gold!')
        player.gain_gold(self.gold)

    def set_name(self, new_name):
        self.name = new_name

    def check_alive(self):
        return self.health > 0

    def damage_taken(self, damage):
        self.health -= damage
        print(f'Monster Health: {self.health}')
        if not self.check_alive():
            print(f'{self.name} has been defeated!')
            return True
        return False
