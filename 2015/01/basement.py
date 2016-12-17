#!/usr/bin/python

import sys

fh = open('instructions')
steps = list(fh.read().strip())
fh.close()

floor = 0
position = None
for step, direction in enumerate(steps):
    floor += 1 if direction == '(' else -1
    if floor < 0:
        position = step + 1
        break

print "FLOOR: {0} (position {1})".format(floor, position)
