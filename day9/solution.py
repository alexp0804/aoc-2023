import sys

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]

sequences = []
with open(input_file_name) as f:
    sequences = [[int(x) for x in line.split()] for line in f.readlines()]

def get_prediction(sequence):
    diffs = [sequence]

    while not all(num == 0 for num in diffs[-1]):
        diffs.append([diffs[-1][i] - diffs[-1][i-1] for i in range(1, len(diffs[-1]))])

    return sum(diff[-1] for diff in diffs)

ans_part_1 = sum(get_prediction(seq) for seq in sequences)
ans_part_2 = sum(get_prediction(seq[::-1]) for seq in sequences)

print(f'The answer:\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')