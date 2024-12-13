#!/usr/bin/python3

import time
from itertools import product
from priorityq import PriorityQueue

# Test input
#cave_depth = 510
#target = (10, 10)

# Puzzle input
cave_depth = 4080
target = (14, 785)

map_char = ['.', '=', '|']

def erosion_level(gi):
	return (gi + cave_depth) % 20183

def region_type(el):
	return el % 3

def add_row(grid):
	row_prev = grid[-1]
	width = len(row_prev)
	row = [0] * width
	y = len(grid)

	for x in range(width):
		if x == 0:
			row[x] = erosion_level(48271 * y)
		elif x == target[0] and y == target[1]:
			# Special case for the target
			row[x] = 0
		else:
			row[x] = erosion_level(row_prev[x] * row[x-1])

	grid.append(row)

def add_column(grid):
	x = len(grid[0])
	for y in range(len(grid)):
		if y == 0:
			grid[y].append(erosion_level(x * 16807))
		else:
			grid[y].append(erosion_level(grid[y-1][-1] * grid[y][-1]))

# This list tells you what the cost is, and what tool you will switch to in
# order to move from one region type to another. You will get None if the
# combination is invalid
# Mapping is move_cost_tool[type_from][type_to][tool]
move_cost_tool = [
		#  N      T       C
	[                                  # In rocky
		[None, (1, 1), (1, 2)],    # To rocky
		[None, (8, 2), (1, 2)],    # To wet
		[None, (1, 1), (8, 1)]     # To narrow
	],
	[                                  # In wet
		[(8, 2), None, (1, 2)],    # To rocky
		[(1, 0), None, (1, 2)],    # To wet
		[(1, 0), None, (8, 0)]     # To narrow
	],
	[                                  # In narrow
		[(8, 1), (1, 1), None],    # To rocky
		[(1, 0), (8, 0), None],    # To wet
		[(1, 0), (1, 1), None]     # To narrow
	]
]

start_time = time.time()

# Start with just the map to the target. We will add rows and columns as need later
len_x = target[0] + 1
len_y = target[1] + 1

# Build a map to work with
grid = [[erosion_level(x * 16807) for x in range(len_x)]]
for y in range(1, len_y):
	add_row(grid)

# Tools => neither=0, torch=1, climbing=2
starting_tool = 1
start_entry = (0, 0, starting_tool)
end_entry = (target[0], target[1], starting_tool)

# Initialize our priority queue, costs, and a set for marking nodes visited
pq = PriorityQueue()
pq.add(start_entry, 0)
costs = { start_entry: 0 }
visited = set()

end_visited = False
while pq:
	curr_cost, entry = pq.pop()
	visited.add(entry)

	curr_x = entry[0]
	curr_y = entry[1]
	curr_tool = entry[2]
	if (curr_x, curr_y) == target:
		# We have to visit the target location twice - once with each possible tool
		if end_visited:
			break
		else:
			end_visited = True
			continue

	curr_type = region_type(grid[curr_y][curr_x])
	for cx, cy in ((curr_x-1, curr_y), (curr_x+1, curr_y), (curr_x, curr_y-1), (curr_x, curr_y+1)):
		# The map extends infinitely to the right and down. Add rows and columns as needed
		if cx < 0 or cy < 0:
			continue
		for _ in range(len_x, cx+1):
			add_column(grid)
			len_x += 1
		for _ in range(len_y, cy+1):
			add_row(grid)

		# Build the entry for the neighbor node, and skip if we have visited it
		to_type = region_type(grid[cy][cx])
		to_cost, to_tool  = move_cost_tool[curr_type][to_type][curr_tool]
		new_entry = (cx, cy, to_tool)
		if new_entry in visited:
			continue

		# Calculate and check costs
		to_cost += curr_cost
		if new_entry not in costs:
			pq.add(new_entry, to_cost)
			costs[new_entry] = to_cost
		else:
			old_cost = costs[new_entry]
			if to_cost < old_cost:
				pq.add(new_entry, to_cost)
				costs[new_entry] = to_cost

best_cost = min(costs[end_entry], costs[(target[0], target[1], 2)] + 7)
print("Time to get to target: %d" % (best_cost))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
