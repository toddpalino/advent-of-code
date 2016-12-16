#!/usr/bin/python

import re
import sys

buttons = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pos = [1, 1]

for line in sys.stdin.readlines():
    directions = list(line)
    for direction in directions:
        if direction in ('u', 'U'):
            pos[0] = max(0, pos[0] - 1)
        elif direction in ('d', 'D'):
            pos[0] = min(2, pos[0] + 1)
        elif direction in ('l', 'L'):
            pos[1] = max(0, pos[1] - 1)
        elif direction in ('r', 'R'):
            pos[1] = min(2, pos[1] + 1)
        else:
            continue
    print buttons[pos[0]][pos[1]]
