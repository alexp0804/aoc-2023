import re

calibration_document = []

with open("input.txt", "r") as f:
    calibration_document = f.read().splitlines()
    f.close()

def calibration_value(s: str) -> int:
    nums = re.sub(r'[A-Za-z]+', '', s)
    return int(nums[0] + nums[-1])

def calibration_value_part2(s: str) -> int:
    # sub 'one' as 'o1e', 'two' as 't2o', and so on...
    # replacing the word with the number with the starting and ending letter surrounding it
    mappings = [
            ('one', 'o1e'),
            ('two', 't2o'),
            ('three', 't3e'),
            ('four', 'f4r'),
            ('five', 'f5e'),
            ('six', 's6e'),
            ('seven', 's7n'),
            ('eight', 'e8t'),
            ('nine', 'n9e')
    ]

    for mapping in mappings:
        s = re.sub(mapping[0], mapping[1], s)

    return calibration_value(s)

answer_part_1 = sum(calibration_value(line) for line in calibration_document)
answer_part_2 = sum(calibration_value_part2(line) for line in calibration_document)

print(f'The answer\n\tpart 1: {answer_part_1}\n\tpart 2: {answer_part_2}')

