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

		# For part1, we are ignoring z. Just set it to 1 with no velocity
		self.point[2] = 1
		self.velocity[2] = 0

		# We'll want a second point. Might as well make it now
		self.point2 = self.point.copy()
		self.point2[0] += self.velocity[0]
		self.point2[1] += self.velocity[1]

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
		if not isclose(tx, ty):
			raise ValueError("x and y coordinates indicate different times (%f != %f)" % (tx, ty))
		return tx

	def __repr__(self):
		return "(%s)" % (self._line)

timer1 = time.process_time()

# Real Input
filename = "input.txt"
bounds = (200000000000000, 400000000000000)

# Test Input
#filename = "test.txt"
#bounds = (7, 27)

with open(filename) as f:
	hailstones = [Hailstone(line[0:-1]) for line in f]

intersections = 0
for pair in combinations(range(len(hailstones)), 2):
	h1 = hailstones[pair[0]]
	h2 = hailstones[pair[1]]
	coord = h1.intersects_with(h2)
	if coord is None:
		continue

	# Make sure the intersection is inside the test bounds
	if not ((bounds[0] <= coord[0] <= bounds[1]) and (bounds[0] <= coord[1] <= bounds[1])):
		continue

	# Check what time each line reaches this point, making sure it's not in the past
	t1 = h1.time_at(coord)
	t2 = h2.time_at(coord)
	if t1 < 0 or t2 < 0:
		continue

	intersections += 1

timer2 = time.process_time()

print("Intersections: %d" % (intersections))
print("Time: %f" % (timer2 - timer1))
