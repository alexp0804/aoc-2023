import sys, re
import numpy as np

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1];

games = []

with open(input_file_name, "r") as f:
    games = f.read().splitlines()
    f.close()

games_valid = [True] * len(games)
games_powers = [0] * len(games)

def solve(index: int, game: str) -> bool:
    maxs = {'red': 12, 'green': 13, 'blue': 14}
    lower_bound = {'red': 0, 'green': 0, 'blue': 0}

    rounds = game.split('; ')

    for round in rounds:
        cubes = re.sub('Game \d+: ', '', round).split(', ')

        for cube in cubes:
            count, color = cube.split(' ')

            if int(count) > maxs[color]:
                games_valid[index] = False

            lower_bound[color] = max(lower_bound[color], int(count))

    games_powers[index] = np.prod(list(lower_bound.values()))

for i, game in enumerate(games):
    solve(i, game)

ans_part_1 = np.sum(np.nonzero(games_valid)) + np.count_nonzero(games_valid)
ans_part_2 = sum(games_powers)

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')