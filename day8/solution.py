import sys, re
import numpy as np

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]
map_input = []

with open(input_file_name) as f:
    instruction = list(f.readline().strip())
    f.readline()
    map_input = [
        re.sub('( = \()|(, )|(\))', ' ', x).split() for x in f.readlines()
    ]

move_map = {}
starting_nodes = []

for move in map_input:
    move_map[move[0]] = { 'L': move[1], 'R': move[2] }

    if move[0][-1] == 'A':
        starting_nodes.append(move[0])

def dist_to_end(node):
    dist = 0
    instruction_idx = 0

    while node[-1] != 'Z':
        node = move_map[node][instruction[instruction_idx]]
        instruction_idx = (instruction_idx + 1) % len(instruction)
        dist += 1

    return dist

part_1_ans = dist_to_end(starting_nodes[0])
part_2_ans = np.lcm.reduce([dist_to_end(node) for node in starting_nodes])

print(f'The answer\n\tpart 1: {part_1_ans}\n\tpart 2: {part_2_ans}')