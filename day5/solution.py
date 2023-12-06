import sys, re

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]

part_1_seeds = []
maps = []

with open(input_file_name) as f:
    part_1_seeds = [int(x) for x in re.sub(r'seeds: ', '', f.readline()).split()]
    f.readline()
    # This was left in as a joke
    [maps.append([[int(x) for x in s.split(' ')] for s in m.split('\n')]) for m in re.sub('.* map:\n','', f.read()).split('\n\n')]


def map_input(num, map_entries):
    entry_to_use = None

    for entry in map_entries:
        # range starts later than this num
        if entry[1] > num: continue

        # first viable range
        if entry_to_use is None:
            entry_to_use = entry

        # pick better range (one that starts closer to num)
        elif entry[1] > entry_to_use[1]:
            entry_to_use = entry
    
    # No ranges fit or range is too short
    if entry_to_use is None or entry_to_use[1] + entry_to_use[2] < num:
        return num

    return num - (entry_to_use[1] - entry_to_use[0])

def get_final_mapping(seed):
    val = seed

    for m in maps:
        val = map_input(val, m)

    return val

ans_part_1 = float('inf')
for seed in part_1_seeds:
    ans_part_1 = min(ans_part_1, get_final_mapping(seed))

# Prep for part 2
# 'seeds' is now ranges of seeds, not individual seeds
seeds = []
for i in range(0, len(part_1_seeds), 2):
    seeds.append([part_1_seeds[i], part_1_seeds[i] + part_1_seeds[i+1]])

for map_layer in maps:
    new_seeds = []

    while len(seeds) > 0:
        seed_start, seed_end = seeds.pop()
        mapped = False

        for mapping in map_layer:

            # Already mapped this seed range
            if mapped: continue

            map_dest, map_start, map_len = mapping
            map_end = map_start + map_len

            intersect_start = max(seed_start, map_start)
            intersect_end = min(seed_end, map_end)

            # No intersection
            if intersect_start >= intersect_end:
                continue

            # Map the intersecting portion
            new_seeds.append([
                intersect_start - map_start + map_dest,
                intersect_end - map_start + map_dest
            ])

            mapped = True

            # Put the non-intersecting portions back so we can check against different mappings
            if intersect_start > seed_start:
                seeds.append([seed_start, intersect_start])
            if intersect_end < seed_end:
                seeds.append([intersect_end, seed_end])

        # None of the maps intersected this seed range so it goes to the next layer unchanged
        if not mapped:
            new_seeds.append([seed_start, seed_end])

    seeds = new_seeds

ans_part_2 = float('inf')
for seed_range in seeds:
    ans_part_2 = min(seed_range[0], ans_part_2)

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')