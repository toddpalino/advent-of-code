#!/usr/bin/env python

import time
from itertools import product

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

grid = []
moves = []
with open(fn, 'r') as f:
	reading_grid = True
	for line in f:
		ln = line.strip()
		if len(ln) == 0:
			reading_grid = False
			continue
		if reading_grid:
			grid.append(list(ln))
			continue

		moves.extend(list(ln))

len_x = len(grid[0])
len_y = len(grid)

r = None
for x, y in product(range(len_x), range(len_y)):
	if grid[y][x] == '@':
		r = [x, y]
		grid[y][x] = '.'

dir = {
	'^': (0, -1),
	'v': (0, 1),
	'<': (-1, 0),
	'>': (1, 0)
}

for move in moves:
	v = dir[move]

	# Figure out how many things need to move in that direction, and if we can do it
	n = 0
	next_x, next_y = r
	while True:
		next_x, next_y = next_x+v[0], next_y+v[1]
		c = grid[next_y][next_x]
		if c == 'O':
			n += 1
		elif c == '#':
			n = None
			break
		elif c == '.':
			break

	if n is None:
		# Can't move, blocked by a wall
		continue

	# Move robot
	grid[r[1]][r[0]] = '.'
	r = [r[0]+v[0], r[1]+v[1]]

	# Move boxes
	for i in range(1, n+1):
		grid[r[1]+(i*v[1])][r[0]+(i*v[0])] = 'O'

# for row in grid:
#	print(''.join(row))

gps_sum = 0
for x, y in product(range(len_x), range(len_y)):
	if grid[y][x] == 'O':
		gps_sum += (100 * y) + x

print("GPS Sum: %d" % (gps_sum))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
