#!/usr/bin/python

import sys

fh = open('instructions')
floor = sum([-1 if c == ')' else 1 for c in list(fh.read().strip())], 0)
fh.close()

print "FLOOR: {0}".format(floor)
