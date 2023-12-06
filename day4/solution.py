
import sys, re

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]

cards = []

with open(input_file_name) as f:
    cards = f.read().splitlines()

def get_matching_nums(card: str) -> int:
    card = re.sub(r'Card\s+\d+: ', '', card)

    winning_nums, my_nums = [
        [int(num) for num in card_half.split()] for card_half in card.split('|')
    ]

    winning_nums = frozenset(winning_nums)
    matches = 0

    for num in my_nums:
        if num in winning_nums:
            matches += 1

    return matches

def get_score(matches: int) -> int:
    return 2 **(matches - 1) if matches > 0 else 0

ans_part_1 = 0
ans_part_2 = 0

copy_counts = [1] * len(cards)

for i, card in enumerate(cards):
    matching_nums = get_matching_nums(card)
    score = get_score(matching_nums)

    for j in range(i+1, min(i+matching_nums+1, len(cards))):
        copy_counts[j] += copy_counts[i]

    ans_part_1 += score
    ans_part_2 += copy_counts[i]

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')
