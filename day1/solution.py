import re

calibration_document = []

with open("input.txt", "r") as f:
    calibration_document = f.read().splitlines()
    f.close()

def calibration_value(s: str) -> int:
    nums = re.sub(r'[A-Za-z]+', '', s)
    return int(nums[0] + nums[-1])

answer = sum(calibration_value(line) for line in calibration_document)

print(f'The answer is: {answer}')
