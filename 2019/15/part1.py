#!/usr/bin/env python

import time
from collections import deque

from aoc.utils.intcode import Intcode, read_intcode_from_file

vectors = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
reverse = {1: 2, 2: 1, 3: 4, 4: 3}

class Stumble:
	def __init__(self, computer):
		self.computer = computer
		self._walls = set()
		self.target = None
		self.steps_to_target = None
		self._start = (0, 0)
		self._visited = set()
		self._x_range = [0, 0]
		self._y_range = [0, 0]

	def _update_ranges(self, x, y):
		if x < self._x_range[0]:
			self._x_range[0] = x
		if x > self._x_range[1]:
			self._x_range[1] = x
		if y < self._y_range[0]:
			self._y_range[0] = y
		if y > self._y_range[1]:
			self._y_range[1] = y

	def wander(self, x=None, y=None, steps=0):
		if x is None:
			x = self._start[0]
			y = self._start[1]
		self._visited.add((x, y))

		for direction in range(1, 5):
			nx, ny = x + vectors[direction][0], y + vectors[direction][1]
			self._update_ranges(nx, ny)
			if (nx, ny) in self._walls:
				continue
			if (nx, ny) in self._visited:
				# We're going to consider crossing our own path to be like a wall
				continue

			# Tell the robot to move in this direction, check the output
			self.computer.add_input(direction)
			self.computer.run()
			output = self.computer.get_output()[0]
			if output == 0:
				self._walls.add((nx, ny))
				continue
			if output == 2:
				self.target = (nx, ny)
				if self.steps_to_target is None:
					self.steps_to_target = steps + 1

			# Keep wandering
			self.wander(nx, ny, steps=steps+1)

			# Return to the original location. Discard the output because we know it's 1 or 2
			self.computer.add_input(reverse[direction])
			self.computer.run()
			self.computer.get_output()

	def spread_oxygen(self):
		queue = deque([(self.target, 0)])
		visited = set()
		max_minutes = 0

		while queue:
			coord, minutes = queue.popleft()
			x, y = coord
			visited.add(coord)

			if minutes > max_minutes:
				max_minutes = minutes
			for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
				if (nx, ny) in self._walls or (nx, ny) in visited:
					continue
				queue.append(((nx, ny), minutes + 1))
		return max_minutes

	def print(self):
		for y in range(self._y_range[0], self._y_range[1]+1):
			for x in range(self._x_range[0], self._x_range[1]+1):
				coord = (x, y)
				c = '.'
				if coord in self._walls:
					c = '#'
				elif coord == self._start:
					c = 'S'
				elif coord == self.target:
					c = 'E'
				print(c, end='')
			print()


start_time = time.time()

computer = Intcode(read_intcode_from_file("input.txt"), pause_for_input=True)
stumbler = Stumble(computer)
stumbler.wander()
print(f'Shortest path to oxygen system: {stumbler.steps_to_target}')

p1_time = time.time()
print("Part 1 Elapsed time: %f\n" % (p1_time - start_time))

total_time = stumbler.spread_oxygen()
print(f'Total time for oxygen to spread: {total_time}')
print("Part 2 Elapsed time: %f" % (time.time() - p1_time))
