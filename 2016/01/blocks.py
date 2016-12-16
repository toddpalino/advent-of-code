#!/usr/bin/python

import re
import sys

axis = [0, 0, 0, 0]
input_string = sys.stdin.read()

current_dir = None

for step in re.split(",\s+", input_string):
    if step[0] in ('r', 'R'):
        current_dir = 0 if current_dir is None else (current_dir + 1) % 4
    elif step[0] in ('l', 'L'):
        current_dir = 3 if current_dir is None else (current_dir - 1) % 4

    axis[current_dir] += int(step[1:])
    print "{0} = {1}".format(step, axis)

print abs(axis[0] - axis[2]) + abs(axis[1] - axis[3])
