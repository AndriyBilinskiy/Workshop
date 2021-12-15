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

    # for 1-sized
    for _ in range(4):
        i, j = random.randint(0,9), random.randint(0,9)
        if field[i][j] != "▢":
            field[i][j] = "▢"

    return field



def display_field(field):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')

    for i, line in enumerate(field):
        print(f'{alp[i]} ', end='')
        print(*line)


def checkHit(map, hit):
    length = len(hit)
    if length == 3:
        hit[0] = hit[0] + hit[1]
        hit.pop(1)
    for i in range(len(hit)):
        if hit[i].isnumeric():
            hit[i] = int(hit[i])
        else:
            hit[i] = ord(hit[i]) - 65
    if len(hit) > 0 and hit[0] <= 10 and hit[0] >= 1 and hit[1] <= 9 and hit[1] >= 0:
        for i in range(len(map)):
            for j in range(len(map)):
                if i == hit[1] and j == hit[0] - 1:
                    if map[i][j] == '▢':
                        return True
                    else:
                        return False
    else:
        print('Invalid input!')


if __name__ == "__main__":
    field  = create_field()
    while True:
        display_field(field)
        hit = list(input())
        hitted = checkHit(field, hit)
        if hitted:
            for i in range(len(field)):
                for j in range(len(field)):
                    if i == hit[1] and j == hit[0] - 1:
                        if field[i][j] == '▢':
                            field[i][j] = 'X'
            print('Good shot!')
        elif not hitted:
            for i in range(len(field)):
                for j in range(len(field)):
                    if i == hit[1] and j == hit[0] - 1:
                        field[i][j] = '*'
                        continue
            print('You missed')          


    