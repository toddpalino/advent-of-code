#!/usr/bin/python

def get_line(x, start_y, size, grid):
	return '/'.join([grid[y][x:x+size] for y in range(start_y, start_y+size)])


mappings = {
	2: {},
	3: {}
}
with open("input", "r") as f:
	for line in f:
		parts = line.strip().split(' => ')
		src_rows = parts[0].split('/')
		size = len(src_rows)

		# All 4 rotations and 4 flipped rotations
		for iter1 in range(2):
			for iter2 in range(4):
				mappings[size]['/'.join(src_rows)] = parts[1]
				src_rows = [''.join([src_rows[j][i] for j in range(len(src_rows)-1,-1,-1)]) for i in range(len(src_rows))]
			src_rows = [src_rows[r] for r in range(len(src_rows)-1,-1,-1)]

grid = [
	'.#.',
	'..#',
	'###'
]

for iteration in range(18):
	if len(grid) % 2 == 0:
		size = 2
	else:
		size = 3

	newgrid = []
	for y in range(0, len(grid), size):
		newrows = [''] * (size + 1)
		for x in range(0, len(grid), size):
			rows = mappings[size][get_line(x, y, size, grid)].split('/')
			for i in range(len(rows)):
				newrows[i] = newrows[i] + rows[i]
		newgrid.extend(newrows)
	grid = newgrid

	print("ON ({0}): {1}".format(iteration, sum([s.count('#') for s in grid])))
