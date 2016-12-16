#!/usr/bin/python

import re
import sys

axis = [0, 0, 0, 0]
locations = {(0,0): 1}
input_string = sys.stdin.read()

current_dir = None

for step in re.split(",\s+", input_string):
    if step[0] in ('r', 'R'):
        current_dir = 0 if current_dir is None else (current_dir + 1) % 4
    elif step[0] in ('l', 'L'):
        current_dir = 3 if current_dir is None else (current_dir - 1) % 4
    for block in range(int(step[1:])):
        axis[current_dir] += 1
        idx = (axis[0] - axis[2], axis[1] - axis[3])
        print "{0} = {1}".format(step, idx)
        if idx not in locations:
            locations[idx] = 1
        else:
            sys.exit(0)
