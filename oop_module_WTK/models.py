import settings
from exceptions import EnemyDown, GameOver
import random


class Enemy:
    def __init__(self, level=settings.INITIAL_ENEMY_LEVEL):
        self.level = level
        self.health = level
        self.characters = ['Wizard', 'Thief', 'Knight']

    def decrease_health(self, player):
        self.health -= 1
        if self.health < 1:
            player.score += settings.SCORE_ENEMY_DOWN
            raise EnemyDown

    def select_character(self):
        return random.choice(self.characters)


class Player:
    def __init__(self, name):
        self.name = name
        self.health = settings.INITIAL_PLAYER_HEALTH
        self.score = 0
        self.characters = {'1': 'Wizard', '2': 'Thief', '3': 'Knight'}
        self.last_attack = True

    def attack(self, enemy):
        enemy_choice = enemy.select_character()
        player_choice = self.select_character()
        result = fight(player_choice, enemy_choice)
        if result == 'Draw':
            print('IT’S A DRAW!')
            self.last_attack = False
        elif result == 'Player':
            print('YOUR ATTACK IS SUCCESSFUL!')
            self.score += settings.SCORE_SUCCESS_ATTACK
            self.last_attack = True
            enemy.decrease_health(self)
        else:
            print('YOUR ATTACK IS FAILED!')
            self.last_attack = False

    def decrease_health(self):
        self.health -= 1
        if self.health < 1:
            raise GameOver

    def defense(self, enemy):
        enemy_choice = enemy.select_character()
        player_choice = self.select_character()
        result = fight(player_choice, enemy_choice)
        if result == 'Draw':
            print('IT’S A DRAW!')
        elif result == 'Enemy':
            print('YOUR DEFENCE IS FAILED!')
            self.decrease_health()
        else:
            print('YOUR DEFENCE IS SUCCESSFUL!')

    def select_character(self):
        while True:
            choice = input('MAKE A FIGHT CHOICE FROM (WIZARD - 1, THIEF - 2, KNIGHT - 3): ')
            if choice == '1' or choice == '2' or choice == '3':
                return self.characters[choice]


def fight(player_choice, enemy_choice):
    if enemy_choice == player_choice:
        return 'Draw'
    elif enemy_choice == 'Wizard' and player_choice == 'Knight' or enemy_choice == 'Thief' and \
            player_choice == 'Wizard' or enemy_choice == 'Knight' and player_choice == 'Thief':
        return 'Enemy'
    else:
        return 'Player'
