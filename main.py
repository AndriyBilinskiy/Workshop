"""this is our main"""
import random


def create_field():
    """10x10"""

    ships_unplaced = 10
    ships = {4: 1, 3 : 2, 2: 3, 1: 4 }

    while ships_unplaced != 0:
        print(f"You have {ships_unplaced} ships unplaced. Ships left: ")
        for key in ships.keys():
            print(f"{key} size : {ships[key]} ship(s) left.")
        break

    field = [['_' for _ in range(10)] for __ in range(10)]





def display_field(field):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')

    for i, line in enumerate(field):
        print(f'{alp[i]} ', end='')
        print(*line)


if __name__ == "__main__":
    create_field()