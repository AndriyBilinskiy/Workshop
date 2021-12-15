"""
Print
"""


def print_array(lst):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')
    for i, line in enumerate(lst):
        print(f'{alp[i]} ', end='')
        print(*line)


def surrender(player):
    if player == 1:
        print(f'Player {player+1} won!')
    else:
        print('Player 1 won!')
    quit()

if __name__ == '__main__':
    field = [['▢' for _ in range(10)] for __ in range(10)]
    field[2][5] = '>'
    field[2][6] = '>'
    field[2][3] = '>'
    field[3][3] = '>'
    field[4][3] = '>'
    print_array(field)
