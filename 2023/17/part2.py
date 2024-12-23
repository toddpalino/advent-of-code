#!/usr/bin/python3

import heapq
import itertools
import time
from collections import deque

def manhattan_cost(node, goal):
	return abs(goal[0] - node[0]) + abs(goal[1] - node[1])

def path_cost(node):
	x = node[0]
	y = node[1]
	direction = node[2]
	distance = node[3]
	if direction == 1:
		return sum(row[x] for row in grid[y-distance:y])
	if direction == 2:
		return sum(row[x] for row in grid[y+1:y+distance+1])
	if direction == 3:
		return sum(grid[y][x+1:x+distance+1])
	if direction == 4:
		return sum(grid[y][x-distance:x])
	return 0

def neighbors(node, len_x, len_y):
	x = node[0]
	y = node[1]
	direction = node[2]
	distance = node[3]
	if direction == 1:
		y -= distance
	elif direction == 2:
		y += distance
	elif direction == 3:
		x += distance
	elif direction == 4:
		x -= distance

	potentials = []
	if direction in (1, 2, 0):
		# Add E/W paths
		for dist in range(4, 11):
			if 0 <= x + dist < len_x:
				potentials.append((x, y, 3, dist))
			if 0 <= x - dist < len_x:
				potentials.append((x, y, 4, dist))
	if direction in (3, 4, 0):
		# Add N/S paths
		for dist in range(4, 11):
			if 0 <= y + dist < len_y:
				potentials.append((x, y, 2, dist))
			if 0 <= y - dist < len_y:
				potentials.append((x, y, 1, dist))

	return potentials

t1 = time.process_time()

with open("input.txt") as f:
	grid = [[int(x) for x in line[0:-1]] for line in f]

len_x = len(grid[0])
len_y = len(grid)

# Nodes are (start_x, start_y, direction, distance)
# Direction is 1 (N), 2 (S), 3 (E), 4 (W)
start = (0, 0, 0, 0)
goal = (len_x-1, len_y-1)

# Path tracking
came_from = {}

# Cheapest cost to get to a given node
cheapest = {start: 0}

# Priority queue (based on the cheapest cost to get to the node, plus the guessed cost to the goal)
queue = []
entry_finder = {}
entry_count = itertools.count()

def add_entry(node, priority):
	# Update or add entry
	if node in entry_finder:
		remove_entry(node)
	count = next(entry_count)
	entry = [priority, count, node]
	entry_finder[node] = entry
	heapq.heappush(queue, entry)

def remove_entry(node):
	entry = entry_finder.pop(node)
	entry[-1] = None

def pop_task():
	while queue:
		priority, count, node = heapq.heappop(queue)
		if node is not None:
			del entry_finder[node]
			return node
	return None

add_entry(start, manhattan_cost(start, goal))
while True:
	current = pop_task()
	if current is None:
		break

	if current[0:2] == goal:
		goal = came_from[current]
		break

	for neighbor in neighbors(current, len_x, len_y):
		next_cost = cheapest[current] + path_cost(neighbor)
		if neighbor not in cheapest or (next_cost < cheapest[neighbor]):
			came_from[neighbor] = current
			cheapest[neighbor] = next_cost
			add_entry(neighbor, next_cost + manhattan_cost(neighbor, goal))

t2 = time.process_time()

path = deque([goal])
while path[0] in came_from:
	path.appendleft(came_from[path[0]])

cost = 0
for i in range(1, len(path)):
	c = path_cost(path[i])
	print(path[i], ' => ', c)
	cost += c
print("Path Cost: %d" % (cost))
print("Time: %f" % (t2 - t1))
