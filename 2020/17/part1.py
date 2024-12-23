#!/usr/bin/python3

from itertools import product

cycles = 6

#with open("test.txt") as f:
with open("input.txt") as f:
	actives = set((x, y, 0) for y, line in enumerate(f.readlines()) for x, c in enumerate(line) if c == '#')

for _ in range(cycles):
	check_ranges = [range(min(vals) - 1, max(vals) + 2) for vals in zip(*actives)]
	next_actives = set()

	# Check all cubes we know about and the ones just outside (+1 in any direction, including diagonals)
	for c in product(check_ranges[0], check_ranges[1], check_ranges[2]):
		# Generate a set of neighbors (don't include ourselves)
		neighbors = set(product(range(c[0]-1, c[0]+2), range(c[1]-1, c[1]+2), range(c[2]-1, c[2]+2)))
		neighbors.remove(c)

		# Count active neighbors and set next state
		active_neighbors = len(actives & neighbors)
		if active_neighbors == 3 or (c in actives and active_neighbors == 2):
			next_actives.add(c)

	# Update state
	actives = next_actives

print(len(actives))

