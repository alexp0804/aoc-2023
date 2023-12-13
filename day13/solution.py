
import sys
import numpy as np

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

with open(sys.argv[1]) as f:
    puzzles = [[list(y) for y in x.split('\n')] for x in f.read().split('\n\n')]

def find_score_part1(puzzle):

    def find_row_reflection(p):
        splits = []

        for split in range(1, len(p[0])):
            reflection = True

            for row in p:
                left, right = np.flip(row[:split]), row[split:]

                for l, r in zip(left, right):
                    if l != r: reflection = False
            
            if reflection: splits.append(split)

        return splits

    splits_a = find_row_reflection(puzzle)

    transposed_puzzle = np.transpose(np.array(puzzle))
    splits_b = find_row_reflection(transposed_puzzle)

    return splits_a + [100 * x for x in splits_b]

def find_score_part2(puzzle, og_answer):
    swap = {'.':'#', '#':'.'}

    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):

            puzzle[i][j] = swap[puzzle[i][j]]

            new_answers = find_score_part1(puzzle)

            for ans in new_answers:
                if ans != og_answer:
                    return ans

            puzzle[i][j] = swap[puzzle[i][j]]

part_1_ans = 0
part_2_ans = 0

for puzzle in puzzles:
    part_1_split = max(find_score_part1(puzzle))

    part_1_ans += part_1_split
    part_2_ans += find_score_part2(puzzle, part_1_split)

print(f'The answer\n\tpart 1: {part_1_ans}\n\tpart 2: {part_2_ans}')
