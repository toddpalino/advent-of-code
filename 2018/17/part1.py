#!/usr/bin/python3

import time
from collections import deque

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

clay = []

with open(fn, 'r') as f:
	# We'll use this while reading in
	coords = [{'x': 0, 'y': 0}, {'x': 0, 'y': 0}]

	for line in f:
		# x=495, y=2..7
		parts = line.strip().split(', ')
		a = parts[0]
		b = parts[1]

		axis = a[0]
		val = int(a[2:])
		coords[0][axis] = val
		coords[1][axis] = val

		axis = b[0]
		r = b[2:].split('..')
		coords[0][axis] = int(r[0])
		coords[1][axis] = int(r[1])

		clay.append(((coords[0]['x'], coords[0]['y']), (coords[1]['x'], coords[1]['y'])))

# Figure out the bounds - first coordinate in the pair will always be lower than the second
# We need 1 additional in all directions to account for overflow
x_vals = [c[0][0] for c in clay]
y_vals = [c[0][1] for c in clay]
min_x = min(x_vals) - 1
max_x = max(x_vals) + 1
min_y = min(y_vals) - 1
max_y = max(y_vals) + 1

input_x = 500 - min_x

# Create a grid to use - the min_* values become our offsets
len_x = max_x - min_x + 1
len_y = max_y - min_y + 1
grid = [['.'] * len_x for _ in range(len_y)]

# Draw the clay onto the grid
for c1, c2 in clay:
	for x in range(c1[0] - min_x, c2[0] - min_x + 1):
		for y in range(c1[1] - min_y, c2[1] - min_y + 1):
			grid[y][x] = '#'

iter = 0
queue = deque([(input_x, 0)])
while queue:
	iter += 1
	src_x, src_y = queue.popleft()

	# Draw unsettled water (|) going down to clay or settled water (~)
	surface_y = None
	overlapping = False
	for y in range(src_y, len_y-1):
		grid[y][src_x] = '|'
		if grid[y+1][src_x] == '|':
			# We can skip this flow because we've already covered it
			overlapping = True
			break
		if grid[y+1][src_x] in ('#', '~'):
			surface_y = y + 1
			break

	if overlapping:
		continue

	if surface_y is not None:
		# Find the left and right bounds of the surface we hit
		s_left = src_x
		s_right = src_x
		while grid[surface_y][s_left-1] in ('#', '~'):
			s_left -= 1
		while grid[surface_y][s_right+1] in ('#', '~'):
			s_right += 1

		# Find bounds (if exist) on the row above the surface (1 past on each side)
		fill_y = surface_y - 1
		f_left = None
		f_right = None
		for x in range(src_x, s_left - 2, -1):
			if grid[fill_y][x] == '#':
				f_left = x + 1
				break
		for x in range(src_x, s_right + 2):
			if grid[fill_y][x] == '#':
				f_right = x - 1
				break

		if f_left is None and f_right is None:
			# No bounds on either side - unsettled water and 2 new sources
			for x in range(s_left - 1, s_right + 2):
				grid[fill_y][x] = '|'
			queue.append((s_left - 1, fill_y))
			queue.append((s_right + 1, fill_y))
		elif f_left is None:
			# No bound on the left - unsettled water and 1 new source on left
			for x in range(s_left - 1, f_right + 1):
				grid[fill_y][x] = '|'
			queue.append((s_left - 1, fill_y))
		elif f_right is None:
			# No bound on the right - unsettled water and 1 new source on right
			for x in range(f_left, s_right + 2):
				grid[fill_y][x] = '|'
			queue.append((s_right + 1, fill_y))
		else:
			# Bounds on both side - settled water and 1 new source above
			for x in range(f_left, f_right + 1):
				grid[fill_y][x] = '~'
			queue.append((src_x, fill_y - 1))

# for ln in grid:
#	print(''.join(ln))

# Count the water in our grid
total_water = sum(1 for y in range(1, len_y) for x in range(0, len_x) if grid[y][x] in ('|', '~'))
settled_water = sum(1 for y in range(1, len_y) for x in range(0, len_x) if grid[y][x] == '~')

print("Total water: %d" % (total_water))
print("Settled water: %d" % (settled_water))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
