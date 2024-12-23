#!/usr/bin/python3

import time
from itertools import combinations
from math import isclose

def cross(a, b):
	return [a[1]*b[2] - a[2]*b[1],
		a[2]*b[0] - a[0]*b[2],
		a[0]*b[1] - a[1]*b[0]]

class Hailstone:
	def __init__(self, line):
		self._line = line
		parts = line.split(' @ ')

		self.point = [int(n) for n in parts[0].split(', ')]
		self.velocity = [int(n) for n in parts[1].split(', ')]

		# We'll want a second point. Might as well make it now
		self.point2 = [
			self.point[0] + self.velocity[0],
			self.point[1] + self.velocity[1],
			self.point[2] + self.velocity[2]
		]

		self.line = cross(self.point, self.point2)

	def intersects_with(self, other):
		point = cross(self.line, other.line)
		if point[2] == 0:
			return None
		return (point[0] / point[2], point[1] / point[2], point[2] / point[2])

	# Return the time we are at a given point
	def time_at(self, point):
		tx = (point[0] - self.point[0]) / self.velocity[0]
		ty = (point[1] - self.point[1]) / self.velocity[1]
		tz = (point[2] - self.point[2]) / self.velocity[2]
		if (not isclose(tx, ty)) or (not isclose(tx, tz)):
			raise ValueError("x, y, and z coordinates indicate different times (%f != %f != %f)" % (tx, ty, tz))
		return tx

	def __repr__(self):
		return "(%s)" % (self._line)

timer1 = time.process_time()

# Real Input
#filename = "input.txt"

# Test Input
filename = "test.txt"

with open(filename) as f:
	hailstones = [Hailstone(line[0:-1]) for line in f]

for hailstone in hailstones:
	print(hailstone.line)

timer2 = time.process_time()

print("Time: %f" % (timer2 - timer1))
