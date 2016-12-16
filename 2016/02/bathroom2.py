#!/usr/bin/python

import re
import sys

buttons = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]
pos = [2, 0]

for line in sys.stdin.readlines():
    directions = list(line)
    for direction in directions:
        proposed = list(pos)
        if direction in ('u', 'U'):
            proposed[0] = max(0, proposed[0] - 1)
        elif direction in ('d', 'D'):
            proposed[0] = min(4, proposed[0] + 1)
        elif direction in ('l', 'L'):
            proposed[1] = max(0, proposed[1] - 1)
        elif direction in ('r', 'R'):
            proposed[1] = min(4, proposed[1] + 1)
        else:
            continue
        # print "{0} -> {1} -> {2} ({3})".format(pos, direction, proposed, buttons[proposed[0]][proposed[1]])
        if buttons[proposed[0]][proposed[1]] is not None:
            pos = proposed
    print buttons[pos[0]][pos[1]]
