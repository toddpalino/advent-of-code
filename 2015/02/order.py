#!/usr/bin/python

footage = 0
ribbon = 0

fh = open('requirements')
for ln in fh.readlines():
    sides = sorted([int(val) for val in ln.strip().split('x')])
    sides_area = [sides[0]*sides[1], sides[1]*sides[2], sides[0]*sides[2]]

    footage += 2 * sum(sides_area, 0) + min(sides_area)
    ribbon += reduce(lambda x, y: x*y, sides) + 2 * (sides[0] + sides[1])

print "PAPER: {0}".format(footage)
print "RIBBON: {0}".format(ribbon)
