#!/usr/bin/python

import sys

count = 0

batch = [[], [], []]
for line in sys.stdin.readlines():
    sides = [int(x) for x in line.split()]
    for i, side in enumerate(sides):
        batch[i].append(side)

    if len(batch[0]) == 3:
        for triangle in batch:
            print triangle
            all_sides = sum(triangle, 0)
            largest_side = max(triangle)
            if (all_sides > 2 * largest_side):
                count += 1
        batch = [[], [], []]

print count
