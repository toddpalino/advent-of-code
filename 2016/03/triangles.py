#!/usr/bin/python

import sys

count = 0
for line in sys.stdin.readlines():
    sides = [int(x) for x in line.split()]
    all_sides = sum(sides, 0)
    largest_side = max(sides)
    if (all_sides > 2 * largest_side):
        count += 1

print count
