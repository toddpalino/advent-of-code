#!/usr/bin/python

import re
import sys
from collections import deque

def display(scr):
    for row in scr:
        print ''.join(row)

def count(scr):
    total = 0
    for row in scr:
        for pixel in row:
            if pixel == '#':
                total += 1
    return total

width = int(sys.argv[1])
height = int(sys.argv[2])

rect_re = re.compile("rect ([0-9]+)x([0-9]+)")
rotate_re = re.compile("rotate (column x|row y)=([0-9]+) by ([0-9]+)")

scr = [deque(['.' for x in range(width)]) for y in range(height)]

for ln in sys.stdin.readlines():
    m = rect_re.match(ln)
    if m:
        for i in range(int(m.group(2))):
            for j in range(int(m.group(1))):
                scr[i][j] = '#'
        continue

    m = rotate_re.match(ln)
    if m:
        if m.group(1) == "row y":
            scr[int(m.group(2))].rotate(int(m.group(3)))
        else:
            idx = int(m.group(2))
            col = deque([scr[y][idx] for y in range(len(scr))])
            col.rotate(int(m.group(3)))
            for y, val in enumerate(col):
                scr[y][idx] = val

display(scr)
print count(scr)
