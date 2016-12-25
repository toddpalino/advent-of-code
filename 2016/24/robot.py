#!/usr/bin/python

import itertools

positions = {}
node_cache = {}
max_depth = 99999999

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.neighbors = []
        node_cache[(self.x, self.y)] = self


def bfs(start_pos, finish_pos):
    start_state = node_cache[start_pos]
    for coord in node_cache:
        node_cache[coord].depth = max_depth
    start_state.depth = 0

    state_stack = [start_state]
    while len(state_stack) > 0:
        state = state_stack.pop(0)
        for child in state.neighbors:
            if child.depth < max_depth:
                continue
            child.depth = state.depth + 1
            if child.pos == finish_pos:
                return child.depth
            state_stack.append(child)
    return -1

with open('map') as f:
    y = 0
    for line in f:
        row = list(line.strip())
        for x, space in enumerate(row):
            if space == '#':
                continue
            if space.isdigit():
                positions[int(space)] = {
                    'pos': (x, y),
                    'distances': {}
                }
            spot = Node(x, y)
            if (x-1, y) in node_cache:
                spot.neighbors.append(node_cache[(x-1, y)])
                node_cache[(x-1, y)].neighbors.append(spot)
            if (x, y-1) in node_cache:
                spot.neighbors.append(node_cache[(x, y-1)])
                node_cache[(x, y-1)].neighbors.append(spot)
        y += 1

for start in positions:
    for finish in positions:
        if start == finish:
            continue
        positions[start]['distances'][finish] = bfs(positions[start]['pos'], positions[finish]['pos'])

min_path = None
min_path_len = 0
min_path_zero = None
min_path_zero_len = 0
for path in itertools.permutations(range(1, 8)):
    last_pos = 0
    path_len = 0
    for pos in path:
        path_len += positions[last_pos]['distances'][pos]
        last_pos = pos
    if min_path is None or min_path_len > path_len:
        min_path_len = path_len
        min_path = path

    path_len += positions[last_pos]['distances'][0]
    if min_path_zero is None or min_path_zero_len > path_len:
        min_path_zero_len = path_len
        min_path_zero = path

print "SHORTEST: {0} - {1}".format(min_path_len, min_path)
print "SHORTEST (to zero): {0} - {1}".format(min_path_zero_len, min_path_zero)
