
import sys, re
import numpy as np

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]

times = []
distances = []

with open(input_file_name) as f:
    times_list = re.sub('.*:\s+', '', f.readline()).split()
    dist_list = re.sub('.*:\s+', '', f.readline()).split()

    times = [int(x) for x in times_list]
    distances = [int(x) for x in dist_list]
    jumbled_time = int(''.join(times_list))
    jumbled_dist = int(''.join(dist_list))

# use math
def solve(time, dist):
    no_ways = 0

    for i in range(1, time):
        if i * time - i ** 2 > dist:
            no_ways += 1
    
    return no_ways

ans_part_1 = 1
for time, dist in list(zip(times, distances)):
    ans_part_1 *= solve(time, dist)

ans_part_2 = solve(jumbled_time, jumbled_dist)

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')
