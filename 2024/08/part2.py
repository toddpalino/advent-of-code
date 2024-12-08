#!/usr/bin/python3

import time
from itertools import permutations

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [ln.strip() for ln in f]

len_y = len(grid)
len_x = len(grid[0])

# Find the locations of the antennas
antennas = {}
for y in range(len_y):
	for x in range(len_x):
		loc = grid[y][x]
		if loc == '.':
			continue
		if loc not in antennas:
			antennas[loc] = []
		antennas[loc].append((x, y))

antinodes = set()
for freq, locs in antennas.items():
	for p1, p2 in permutations(locs, 2):
		x_off = p1[0] - p2[0]
		y_off = p1[1] - p2[1]
		i = 0
		while True:
			x = p1[0] + (i * x_off)
			y = p1[1] + (i * y_off)
			if (0 <= x < len_x) and (0 <= y < len_y):
				antinodes.add((x, y))
				i += 1
			else:
				break

print("Unique antinodes: %d" % (len(antinodes)))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
