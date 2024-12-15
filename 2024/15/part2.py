#!/usr/bin/env python

import time
from bot import move_lateral, move_vertical
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

# Transform the map for part 2
new_grid = [['.'] * (len_x * 2) for _ in range(len_y)]
for x, y in product(range(len_x), range(len_y)):
	c = grid[y][x]
	if c == '#':
		new_grid[y][x*2] = '#'
		new_grid[y][x*2+1] = '#'
	elif c == 'O':
		new_grid[y][x*2] = '['
		new_grid[y][x*2+1] = ']'
	elif c == '@':
		new_grid[y][x*2] = '@'
grid = new_grid
len_x = len(grid[0])
len_y = len(grid)

r = None
for x, y in product(range(len_x), range(len_y)):
	if grid[y][x] == '@':
		r = [x, y]
		#grid[y][x] = '.'

dir = {
	'^': (0, -1),
	'v': (0, 1),
	'<': (-1, 0),
	'>': (1, 0)
}

for move in moves:
	# Lateral moves are easy
	if move in ('<', '>'):
		move_lateral(r, grid, dir[move])
	else:
		move_vertical(r, grid, dir[move])

for row in grid:
	print(''.join(row))

gps_sum = 0
for x, y in product(range(len_x), range(len_y)):
	if grid[y][x] == '[':
		gps_sum += (100 * y) + x

print("GPS Sum: %d" % (gps_sum))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
