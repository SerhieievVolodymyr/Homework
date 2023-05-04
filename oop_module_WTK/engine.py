import models
from settings import INITIAL_ENEMY_LEVEL
import exceptions


def get_player_name():
    return input('ENTER YOUR NAME: ').strip()


def play():
    player = models.Player(get_player_name())
    enemy = models.Enemy()
    enemy_level = INITIAL_ENEMY_LEVEL
    try:
        while True:
            print(f'Player hp   -  {player.health}', end='   ')
            print(f'Enemy hp   -  {enemy.health}')
            print(f'Player score - {player.score}', end='   ')
            print(f'Enemy level - {enemy_level}')
            while True:
                print('ATTACK')
                try:
                    player.attack(enemy)
                except exceptions.EnemyDown:
                    print(f'ENEMY LEVEL {enemy_level} IS DEFEATED')
                    enemy_level += 1
                    enemy = models.Enemy(enemy_level)
                    print(f'NEW ENEMY LEVEL {enemy.level}')
                if not player.last_attack:
                    break
                else:
                    print(f'Enemy hp - {enemy.health}')
                    print(f'Player score - {player.score}')
            print('DEFENSE')
            try:
                player.defense(enemy)
            except exceptions.GameOver:
                print(f'{player.name} is defeated')
                print(f'SCORE POINTS: {player.score}')
                break
    except KeyboardInterrupt:
        print('\nGame over')
        print(f'{player.name} hp   -  {player.health}', end='   ')
        print(f'Enemy hp   -  {enemy.health}')
        print(f'{player.name} score - {player.score}', end='   ')
        print(f'Enemy level - {enemy_level}')


if __name__ == '__main__':
    play()
