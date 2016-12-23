#!/usr/bin/python

import re
import sys

max_depth = 999999
node_cache = {}
class Node:
    def __init__(self, x, y, total, used):
        self.x = x
        self.y = y
        self.total = total
        self.used = used
        self.neighbors = []
        self.depth = max_depth
        node_cache[(self.x, self.y)] = self

    def available(self):
        return self.total - self.used


def bfs(start_state, finish_x, finish_y):
    state_stack = [start_state]
    max_used = start_state.available()

    while len(state_stack) > 0:
        state = state_stack.pop(0)
        for child in state.neighbors:
            if child.depth < max_depth:
                continue
            if child.used > max_used:
                continue
            child.depth = state.depth + 1
            if child.x == finish_x and child.y == finish_y:
                return child.depth
            state_stack.append(child)
    return -1

df_re = re.compile(r'/dev/grid/node-x([0-9]+)-y([0-9]+)\s+([0-9]+)T\s+([0-9]+)T')

max_x = 0
max_y = 0
with open('df.output') as f:
    for line in f:
        m = df_re.match(line)
        if m is None:
            continue
        x = int(m.group(1))
        y = int(m.group(2))
        node = Node(x, y, int(m.group(3)), int(m.group(4)))
        for coord in ((node.x-1, node.y), (node.x+1, node.y), (node.x, node.y-1), (node.x, node.y+1)):
            if coord in node_cache:
                node.neighbors.append(node_cache[coord])
                node_cache[coord].neighbors.append(node)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

by_used = sorted(node_cache.keys(), key=lambda x: node_cache[x].used)
by_avail = sorted(node_cache.keys(), key=lambda x: node_cache[x].available(), reverse=True)

pairs = 0
for node_a in by_used:
    if node_cache[node_a].used == 0:
        continue
    for node_b in by_avail:
        if node_cache[node_b].available() < node_cache[node_a].used:
            break
        pairs += 1

print "VIABLE PAIRS: {0}".format(pairs)

# BFS to get the empty node to (max_x-1, 0)
node_cache[by_used[0]].depth = 0
moves = bfs(node_cache[by_used[0]], max_x-1, 0)

# Empty node is now in "front" of the goal node. Every step of moving the goal mode takes 5 moves:
# . _ G -> . G _ -> . G . -> . G . -> . G . -> _ G .
# . . .    . . .    . . _    . _ .    _ . .    . . .
#
# We do this distance-1 times, then one extra move to move the goal node to our node
moves += ((max_x - 1) * 5) + 1
print "MOVES: {0}".format(moves)

# goal_node = (max_x, 0)
# my_node = (0, 0)
# for y in range(max_y+1):
#     for x in range(max_x+1):
#         node_str = '.'
#         if (x, y) == goal_node:
#             node_str = 'G'
#         elif (x, y) == my_node:
#             node_str = 'M'
#         elif node_cache[(x, y)].used == 0:
#             node_str = '_'
#         elif node_cache[(x, y)].used > 100:
#             node_str = '#'
#         sys.stdout.write(node_str)
#     sys.stdout.write("\n")
