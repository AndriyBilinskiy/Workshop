"""
Print
"""


field = [['_' for _ in range(10)] for __ in range(10)]

def print_array(lst):
    alp = 'ABCDEFGHIJ'
    print('  1 2 3 4 5 6 7 8 9 10')
    for i, line in enumerate(lst):
        print(f'{alp[i]} ', end='')
        print(*line)
print_array(field)



ship1 = [1,1,1,1]