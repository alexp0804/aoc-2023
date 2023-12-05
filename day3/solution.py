
import sys
import numpy as np

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]

engine = []
symbols = frozenset(['&', '/', '+', '#', '@', '%', '-', '$', '*', '='])

with open(input_file_name) as f:
    engine = [list(line) for line in f.read().splitlines()]
    f.close()

def in_bounds(i, j):
    return i >= 0 and i < len(engine) and j >= 0 and j < len(engine[0])

def surrounding_symbols(i, j):
    offsets = [(-1, -1), (-1, 0),
               (-1, 1), (0, -1),
               (0, 1), (1, -1),
               (1, 0), (1, 1)]

    for offset in offsets:
        coord = np.array((i, j)) + np.array(offset)

        if not in_bounds(*coord):
            continue
        
        if engine[coord[0]][coord[1]] in symbols:
            return True

    return False

ans_part_1 = 0
ans_part_2 = 0

for i in range(len(engine)):
    number_start = 0
    in_number = False
    use_number = False

    for j in range(len(engine[0])):
        symbol = surrounding_symbols(i, j)
        char = engine[i][j]

        if char.isnumeric():
            if not in_number:
                number_start = j

            in_number = True

            if symbol:
                use_number = True

        else:
            if in_number and use_number:
                ans_part_1 += int(''.join(engine[i][number_start:j]))
            
            in_number = False
            use_number = False
    
    if in_number and use_number:
        ans_part_1 += int(''.join(engine[i][number_start:]))

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')