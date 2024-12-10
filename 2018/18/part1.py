#!/usr/bin/python3

import time

#fn = "test.txt"
fn = "input.txt"

iterations = 10

start_time = time.time()

with open(fn, 'r') as f:
	grid = [list(line.strip()) for line in f]
len_x = len(grid[0])
len_y = len(grid)

change_trees = set()
change_lumber = set()
change_open = set()

for _ in range(iterations):
	change_trees.clear()
	change_lumber.clear()
	change_open.clear()

	for x in range(len_x):
		for y in range(len_y):
			count_open = 0
			count_lumber = 0
			count_trees = 0
			for nx in range(x-1, x+2):
				for ny in range(y-1, y+2):
					if (not (x == nx and y == ny)) and (0 <= nx < len_x) and (0 <= ny < len_y):
						loc = grid[ny][nx]
						if loc == '.':
							count_open += 1
						elif loc == '#':
							count_lumber += 1
						else:
							count_trees += 1

			
			loc = grid[y][x]
			if loc == '.' and count_trees >= 3:
				change_trees.add((x, y))
			elif loc == '|' and count_lumber >= 3:
				change_lumber.add((x, y))
			elif loc == '#' and (count_lumber == 0 or count_trees == 0):
				change_open.add((x, y))

	# Make all the changes after we've figured out what they all are
	for x, y in change_trees:
		grid[y][x] = '|'
	for x, y in change_lumber:
		grid[y][x] = '#'
	for x, y in change_open:
		grid[y][x] = '.'

total_trees = sum(1 for x in range(len_x) for y in range(len_y) if grid[y][x] == '|')
total_lumber = sum(1 for x in range(len_x) for y in range(len_y) if grid[y][x] == '#')

print("Total resource value: %d" % (total_trees * total_lumber))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
