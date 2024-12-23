#!/usr/bin/python3

import time

# Real Input
#filename = "input.txt"
#steps = 26501365

# Test Input
filename = "test.txt"
#steps = 16733044
steps = 50

t1 = time.process_time()

def get_neighbors(plot):
	return (
		(plot[0]-1, plot[1]),
		(plot[0]+1, plot[1]),
		(plot[0], plot[1]-1)),
		(plot[0], plot[1]+1))
	)

grid = []
start = None
with open(filename) as f:
	for line in f:
		grid.append([(x == '.' or x == 'S') for x in line[0:-1]])
		try:
			start_x = line.index('S')
			start = (start_x, len(grid) - 1)
		except ValueError:
			pass

max_x = len(grid[0])
max_y = len(grid)

num_plots = 1
next_step = set([start])
for i in range(steps + 1):
	current_step = next_step
	next_step = set([])
	num_plots = len(current_step)
	print("s=%d p=%d" % (i, num_plots))

	while current_step:
		plot = current_step.pop()
		for neighbor in get_neighbors(plot):
			if grid[neighbor[1]][neighbor[0]]:
				next_step.add(neighbor)

t2 = time.process_time()

print("Can reach: %d" % (num_plots))
print("Time: %f" % (t2 - t1))
