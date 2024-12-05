#!/usr/bin/python3

#fn = "test.txt"
fn = "input.txt"

with open(fn, 'r') as f:
	grid = [line.strip() for line in f]

max_x = len(grid[0])
max_y = len(grid)
matches = 0

for y in range(1, max_y - 1):
	for x in range(1, max_x - 1):
		letter = grid[y][x]
		if grid[y][x] != 'A':
			continue

		nw = grid[y-1][x-1]
		ne = grid[y-1][x+1]
		sw = grid[y+1][x-1]
		se = grid[y+1][x+1]

		if ((nw == ne == 'M' and se == sw == 'S') or (nw == sw == 'M' and ne == se == 'S') or
		    (sw == se == 'M' and nw == ne == 'S') or (ne == se == 'M' and nw == sw == 'S')):
			matches += 1

print("Total matches: %d" % (matches))
