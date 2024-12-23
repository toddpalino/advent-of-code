#!/usr/bin/python3

import time

# Real Input
filename = "input.txt"
steps = 64

# Test Input
# filename = "test.txt"
# steps = 6

t1 = time.process_time()

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
for _ in range(steps + 1):
	current_step = next_step
	next_step = set([])
	num_plots = len(current_step)

	while current_step:
		plot = current_step.pop()
		for neighbor in ((plot[0]-1, plot[1]), (plot[0]+1, plot[1]), (plot[0], plot[1]-1), (plot[0], plot[1]+1)):
			if (0 <= neighbor[0] < max_x) and (0 <= neighbor[1] < max_y):
				is_plot = grid[neighbor[1]][neighbor[0]]
				if is_plot and neighbor not in next_step:
					next_step.add(neighbor)

t2 = time.process_time()

print("Can reach: %d" % (num_plots))
print("Time: %f" % (t2 - t1))
