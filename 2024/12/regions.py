#!/usr/bin/python3

from collections import deque
from itertools import product

def make_regions(grid):
	regions = []

	# Put all the coords into a set which we'll use to figure out what we haven't looked at
	coords = set(product(range(len(grid[0])), range(len(grid))))

	while coords:
		# Pull any coord from the set to start a region
		c = coords.pop()
		r = set([c])
		l = grid[c[1]][c[0]]

		# Look at neighbors to build this region
		queue = deque([c])
		while queue:
			x, y = queue.popleft()
			for n in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
				if n not in coords:
					continue
				if grid[n[1]][n[0]] == l:
					# This adjacent plot is in the same region
					coords.remove(n)
					r.add(n)
					queue.append(n)

		regions.append(r)

	return regions
