
import sys

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

pipes = []
with open(sys.argv[1]) as f:
    pipes = [list(x.strip()) for x in f.readlines()]

width = len(pipes[0])
height = len(pipes)

left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)

opposites = { left:right, right:left, up:down, down:up }

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def in_bounds(a):
    return 0 <= a[0] < height and 0 <= a[1] < width

moves = {
    '|': [up, down],
    '-': [left, right],
    'L': [right, up],
    'F': [right, down],
    'J': [left, up],
    '7': [left, down],
    '.': [],
    'S': [],
}

source = None
for i in range(height):
    for j in range(width):
        if pipes[i][j] == 'S':
            source = (i, j)

queue = []
visited = {source}

# Get starting points 
for offset in [left, right, up, down]:
    dest = add(source, offset)

    if not in_bounds(dest):
        continue

    if opposites[offset] in moves[pipes[dest[0]][dest[1]]]:
        queue.append(dest)

dist = [[0 for _ in range(width)] for _ in range(height)]
while len(queue) > 0:
    v = queue.pop(0)

    for offset in moves[pipes[v[0]][v[1]]]:
        to = add(offset, v)

        if to in visited or not in_bounds(to):
            continue
        
        dist[to[0]][to[1]] = dist[v[0]][v[1]] + 1
        visited.add(to)
        queue.append(to)

ans_part_1 = max(max(l) for l in dist) + 1

# https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
ans_part_2 = 0
for i in range(height):
    for j in range(width):
        b = (i, j)

        if b in visited:
            continue

        inside = False

        while in_bounds(b):
            if b in visited and pipes[b[0]][b[1]] not in {'F', 'J'}:
                inside = not inside

            b = add(b, (1, -1))
        
        if inside:
            ans_part_2 += 1

print(f'The answer\n\tpart 1: {ans_part_1}\n\tpart 2: {ans_part_2}')