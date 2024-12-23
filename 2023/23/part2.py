#!/usr/bin/python3

import time
from collections import deque

class Node:
	def __init__(self, coord, grid):
		self.x = coord[0]
		self.y = coord[1]
		self._grid = grid

		# node => path length
		self.neighbors = {}

	def find_next_node(self, first_step):
		distance = 1
		current = first_step
		last_step = (self.x, self.y)

		while True:
			neighbors = get_neighbors(current, self._grid)
			if len(neighbors) != 2:
				return (current, distance)
			next_step = neighbors[neighbors.index(last_step) - 1]
			last_step = current
			current = next_step
			distance += 1

	def find_neighbors(self):
		neighbors = {}
		for neighbor in get_neighbors((self.x, self.y), self._grid):
			rv = self.find_next_node(neighbor)
			neighbors[rv[0]] = rv[1]
		return neighbors

	def __repr__(self):
		return "(Node %d, %d)" % (self.x, self.y)


def get_neighbors(coord, grid):
	return [n for n in ((coord[0], coord[1]-1), (coord[0], coord[1]+1), (coord[0]-1, coord[1]), (coord[0]+1, coord[1])) if (0 <= n[0] < len(grid[0])) and (0 <= n[1] < len(grid)) and grid[n[1]][n[0]] in '.<>^v']

def path_distance(path):
	distance = 0
	for i in range(1, len(path)):
		distance += path[i-1].neighbors[path[i]]
	return distance

t1 = time.process_time()

with open("input.txt") as f:
	grid = f.readlines()
last_line = len(grid) - 1

start = Node((grid[0].index('.'), 0), grid)
goal = Node((grid[last_line].index('.'), last_line), grid)

# We need to parse the grid out to vertices and edges or we're going to be looping forever
nodes = {(start.x, start.y): start, (goal.x, goal.y): goal}
queue = deque([start])
while queue:
	current = queue.popleft()
	neighbors = current.find_neighbors()
	for neighbor, distance in neighbors.items():
		if neighbor not in nodes:
			nodes[neighbor] = Node(neighbor, grid)
			queue.append(nodes[neighbor])
		current.neighbors[nodes[neighbor]] = distance

# Now we're going to find the longest path from start to goal
paths = deque([[start]])
longest = 0
while paths:
	path = paths.popleft()
	current = path[-1]
	for neighbor in current.neighbors:
		if neighbor == goal:
			longest = max(longest, path_distance(path) + current.neighbors[goal])
		elif neighbor not in path:
			paths.append((*path, neighbor))

t2 = time.process_time()

print(longest)
print("Time: %f" % (t2 - t1))
