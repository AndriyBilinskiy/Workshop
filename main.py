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

    # for 2-sized
    for _ in range(3):
        while True:
            # getting rotation:
            # if 1 then up, if 2 then down, if 3 then left, if 4 then right
            rotation = random.randint(1, 4)
            i, j = random.randint(0,9), random.randint(0,9)
            if rotation == 1:
                try:
                    if field[i][j] != "▢" and field[i+1][j] != "▢":
                        field[i][j] = "▢"
                        field[i+ 1][j] = "▢"
                        break
                except IndexError:
                    pass

            elif rotation == 2:
                try:
                    if field[i][j] != "▢" and field[i - 1][j] != "▢":
                        field[i][j] = "▢"
                        field[i - 1][j] = "▢"
                        break
                except IndexError:
                    pass
            elif rotation == 3:
                try:
                    if field[i][j] != "▢" and field[i][j + 1] != "▢":
                        field[i][j] = "▢"
                        field[i][j + 1] = "▢"
                        break
                except IndexError:
                    pass
            elif rotation == 4:
                try:
                    if field[i][j] != "▢" and field[i][j - 1] != "▢":
                        field[i][j] = "▢"
                        field[i][j - 1] = "▢"
                        break
                except IndexError:
                    pass
    """
    # for 3-sized
    for _ in range(2):
        while True:
            # getting rotation:
            # if 1 then up, if 2 then down, if 3 then left, if 4 then right
            rotation = random.randint(1, 4)
            i, j = random.randint(0,9), random.randint(0,9)
            if rotation == 1:
                try:
                    if field[i][j] != "▢" and field[i+1][j] != "▢" and field[i + 2][j] != "▢":
                        field[i][j] = "▢"
                        field[i + 1][j] = "▢"
                        field[i + 2][j] = "▢"
                        break
                except IndexError:
                    pass

            elif rotation == 2:
                try:
                    if field[i][j] != "▢" and field[i - 1][j] != "▢" and :
                        field[i][j] = "▢"
                        field[i - 1][j] = "▢"
                        break
                except IndexError:
                    pass
            elif rotation == 3:
                try:
                    if field[i][j] != "▢" and field[i][j + 1] != "▢":
                        field[i][j] = "▢"
                        field[i][j + 1] = "▢"
                        break
                except IndexError:
                    pass
            elif rotation == 4:
                try:
                    if field[i][j] != "▢" and field[i][j - 1] != "▢":
                        field[i][j] = "▢"
                        field[i][j - 1] = "▢"
                        break
                except IndexError:
                    pass
    """


    return field


def check_borders(field, i,j,size, rotation):
    pass



def display_field(field):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')

    for i, line in enumerate(field):
        print(f'{alp[i]} ', end='')
        print(*line)


if __name__ == "__main__":
    field  = create_field()
    display_field(field)