"""this is our main"""
import random


def create_field():
    """10x10"""
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
                    if field[i][j] != "▢" and field[i - 1][j] != "▢" and field[i - 2][j] != "▢":
                        field[i][j] = "▢"
                        field[i - 1][j] = "▢"
                        field[i - 2][j] = "▢"
                        break
                except IndexError:
                    pass
            elif rotation == 3:
                try:
                    if field[i][j] != "▢" and field[i][j + 1] != "▢" and field[i][j + 2] != "▢":
                        field[i][j] = "▢"
                        field[i][j + 1] = "▢"
                        field[i][j + 2] = "▢"
                        break
                except IndexError:
                    pass
            elif rotation == 4:
                try:
                    if field[i][j] != "▢" and field[i][j - 1] != "▢" and field[i][j - 2] != "▢":
                        field[i][j] = "▢"
                        field[i][j - 1] = "▢"
                        field[i][j - 2] = "▢"
                        break
                except IndexError:
                    pass

    # for 4-sized
    while True:
        # getting rotation:
        # if 1 then up, if 2 then down, if 3 then left, if 4 then right
        rotation = random.randint(1, 4)
        i, j = random.randint(0,9), random.randint(0,9)
        if rotation == 1:
            try:
                if field[i][j] != "▢" and field[i+1][j] != "▢" and field[i + 2][j] != "▢" and field[i + 3][j] != "▢":
                    field[i][j] = "▢"
                    field[i + 1][j] = "▢"
                    field[i + 2][j] = "▢"
                    field[i + 3][j] = "▢"
                    break
            except IndexError:
                pass

        elif rotation == 2:
            try:
                if field[i][j] != "▢" and field[i - 1][j] != "▢" and field[i - 2][j] != "▢" and field[i - 3][j] != "▢":
                    field[i][j] = "▢"
                    field[i - 1][j] = "▢"
                    field[i - 2][j] = "▢"
                    field[i - 3][j] = "▢"
                    break
            except IndexError:
                pass
        elif rotation == 3:
            try:
                if field[i][j] != "▢" and field[i][j + 1] != "▢" and field[i][j + 2] != "▢" and field[i][j + 3] != "▢":
                    field[i][j] = "▢"
                    field[i][j + 1] = "▢"
                    field[i][j + 2] = "▢"
                    field[i][j + 3] = "▢"
                    break
            except IndexError:
                pass
        elif rotation == 4:
            try:
                if field[i][j] != "▢" and field[i][j - 1] != "▢" and field[i][j - 2] != "▢" and field[i][j - 3] != "▢":
                    field[i][j] = "▢"
                    field[i][j - 1] = "▢"
                    field[i][j - 2] = "▢"
                    field[i][j - 3] = "▢"
                    break
            except IndexError:
                pass
    return field

def display_field(field):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')

    for i, line in enumerate(field):
        print(f'{alp[i]} ', end='')
        print(*line)


def display_field(field):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')

    for i, line in enumerate(field):
        print(f'{alp[i]} ', end='')
        print(*line)


def checkHit(map, hit):
    if hit[0] == "Q":
        print("YOU SURRENDERED. EXITING GAME...")
        quit()
    length = len(hit)
    if length == 3:
        hit[0] = hit[0] + hit[1]
        hit.pop(1)
    if hit[0].isnumeric():
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
        print('Invalid input')
        return False


if __name__ == "__main__":
    print()
    print('Ship war game')
    field = create_field()
    field1 = [['_' for _ in range(10)] for __ in range(10)]
    counter = 0
    while True:


        display_field(field1)
        if counter == 20:
            print("____- GOOD GAME! -_____\n \tYOU WON")
            quit()
        print()
        print('Write coordinates: ')
        hit = list(input('>>> '))
        if hit[0] == "~":
            display_field(field)
            print("____---------______")
            continue
        print()
        print()
        hitted = checkHit(field, hit)
        if hitted:
            for i in range(len(field)):
                for j in range(len(field)):
                    if i == hit[1] and j == hit[0] - 1:
                        if field[i][j] == '▢':
                            field1[i][j] = 'X'
                            counter += 1
            print('Last hit: Good shot!')
            print()
        elif not hitted:
            for i in range(len(field)):
                for j in range(len(field)):
                    if i == hit[1] and j == hit[0] - 1:
                        field1[i][j] = '*'
                        continue
            print('Last hit: You missed')
            print()