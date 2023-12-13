
import sys
import numpy as np

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

universe = []
with open(sys.argv[1]) as f:
    universe = np.array([list(x.strip()) for x in f.readlines()])

row_expansions = [0 for _ in range(len(universe))]
col_expansions = [0 for _ in range(len(universe[0]))]

for i in range(universe.shape[0]):
    if np.all(universe[i] == '.'):
        row_expansions[i] = 1

for j in range(universe.shape[1]):
    if np.all(universe[:,j] == '.'):
        col_expansions[j] = 1

cum_rows = np.cumsum(row_expansions)
cum_cols = np.cumsum(col_expansions)

def cum_dist(a, b, part_2=False):
    return abs(a[1] - b[1]) + abs(a[0] - b[0]) \
        + (cum_cols[max(a[1], b[1])] - cum_cols[min(a[1], b[1])]) * (999999 if part_2 else 1) \
        + (cum_rows[max(a[0], b[0])] - cum_rows[min(a[0], b[0])]) * (999999 if part_2 else 1)

galaxies = []
for i in range(len(universe)):
    for j in range(len(universe[0])):
        if universe[i][j] == '#':
            galaxies.append((i, j))

ans_part_1 = 0
ans_part_2 = 0

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        ans_part_1 += cum_dist(galaxies[i], galaxies[j])
        ans_part_2 += cum_dist(galaxies[i], galaxies[j], part_2=True)

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')
