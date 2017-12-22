#!/usr/bin/python

import sys
from collections import deque

grid = {}
class Loc(object):
	def __init__(self, x, y, clean=True):
		self.x = x
		self.y = y
		self.clean = clean

	def move(self, diff):
		x = self.x + diff[0]
		y = self.y + diff[1]
		if (x, y) not in grid:
			grid[(x,y)] = Loc(x, y)
		return grid[(x, y)]


starting_grid = []
with open("input", "r") as f:
	for line in f:
		starting_grid.append(list(line.strip()))

# Test input
test_starting_grid = [
	['.', '.', '#'],
	['#', '.', '.'],
	['.', '.', '.']
]
#starting_grid = test_starting_grid

# We want to give the grid coordinates with the middle being (0, 0). Figure out the max on the starting grid
max_x = len(starting_grid[0]) / 2
max_y = len(starting_grid) / 2

for y in range(max_y, -max_y - 1, -1):
	for x in range(-max_x, max_x + 1):
		grid[(x, y)] = Loc(x, y, clean=starting_grid[max_y-y][x+max_x] == '.')

# This is the coordinate difference for the next move. Starting order is "up, left, down, right"
# Turning left is rotate(-1), right is rotate()
move_diff = deque([(0, 1), (-1, 0), (0, -1), (1, 0)])

location = grid[(0, 0)]
infected = 0
for i in range(10000):
	if location.clean:
		move_diff.rotate(-1)
		infected += 1
	else:
		move_diff.rotate()
	location.clean = not location.clean
	location = location.move(move_diff[0])

print("INFECTED: {0}".format(infected))
