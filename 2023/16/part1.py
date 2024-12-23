#!/usr/bin/python3

import time
from collections import deque

# Directions
NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

class Node:
	def __init__(self, c, x, y):
		self.c = c
		self.x = x
		self.y = y
		self.energized = False

	# Returns a list of Beam objects
	def act_on_beam(self, beam):
		incoming_direction = beam.direction
		c = self.c
		self.energized = True

		if c == '-' and incoming_direction in [NORTH, SOUTH]:
			beam.direction = EAST
			return [beam, Beam(beam.x, beam.y, WEST)]
		elif c == '|' and incoming_direction in [EAST, WEST]:
			beam.direction = NORTH
			return [beam, Beam(beam.x, beam.y, SOUTH)]
		elif c in '/\\':
			if incoming_direction == EAST:
				beam.direction = NORTH if c == '/' else SOUTH
			if incoming_direction == WEST:
				beam.direction = SOUTH if c == '/' else NORTH
			if incoming_direction == NORTH:
				beam.direction = EAST if c == '/' else WEST
			if incoming_direction == SOUTH:
				beam.direction = WEST if c == '/' else EAST
		return [beam]

class Beam:
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction

	def __repr__(self):
		direction = "NORTH"
		if self.direction == 2:
			direction = "SOUTH"
		elif self.direction == 3:
			direction = "EAST"
		elif self.direction == 4:
			direction = "WEST"
		return "(Beam x=%d y=%d d=%s)" % (self.x, self.y, direction)

	def advance(self, max_x=-1, max_y=-1):
		next_x = self.x
		next_y = self.y

		if self.direction == NORTH:
			next_y -= 1
		if self.direction == SOUTH:
			next_y += 1
		if self.direction == EAST:
			next_x += 1
		if self.direction == WEST:
			next_x -= 1
		if (0 <= next_x <= max_x) and (0 <= next_y <= max_y):
			self.x = next_x
			self.y = next_y
			return True
		else:
			return False

def print_energized(grid):
	for row in grid:
		print(''.join(['#' if g.energized else '.' for g in row]))

grid = []
with open("input.txt") as f:
	y = 0
	for line in f:
		grid.append([Node(c, x, y) for x, c in enumerate(line[0:-1])])

max_x = len(grid[0]) - 1
max_y = len(grid) - 1

beam_path = []
beams = deque([Beam(0, 0, EAST)])
while beams:
	beam = beams.popleft()
	at = (beam.x, beam.y, beam.direction)
	if at in beam_path:
		# We've already had a beam pass through this node in this direction
		# We don't need to do it again
		continue

	beam_path.append(at)
	new_beams = grid[beam.y][beam.x].act_on_beam(beam)
	for new_beam in new_beams:
		if new_beam.advance(max_x, max_y):
			beams.append(new_beam)

count_energized = sum(sum(1 if g.energized else 0 for g in row) for row in grid)
print_energized(grid)
print(count_energized)
