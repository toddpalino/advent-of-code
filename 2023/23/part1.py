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
			del neighbors[last_step]
			last_step = current
			current = neighbors.popitem()[0]
			distance += 1

	def find_neighbors(self):
		neighbors = {}
		possibles = get_neighbors((self.x, self.y), self._grid)
		for neighbor in possibles:
			if possibles[neighbor]:
				rv = self.find_next_node(neighbor)
				neighbors[rv[0]] = rv[1]
		return neighbors

	def __repr__(self):
		return "(Node %d, %d)" % (self.x, self.y)


def get_neighbors(coord, grid):
	max_x = len(grid[0]) - 1
	max_y = len(grid)
	neighbors = {}
	for i, n in enumerate(((coord[0], coord[1]-1), (coord[0], coord[1]+1), (coord[0]-1, coord[1]), (coord[0]+1, coord[1]))):
		if (0 <= n[0] < max_x) and (0 <= n[1] < max_y):
			c = grid[n[1]][n[0]]
			if c in '.<>^v':
				neighbors[n] = not ((i == 0 and c == 'v') or (i == 1 and c == '^') or (i == 2 and c == '>') or (i == 3 and c == '<'))
	return neighbors

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
longest = {start: 0}
queue = deque([start])
while queue:
	current = queue.popleft()
	for neighbor in current.neighbors:
		if neighbor not in longest:
			longest[neighbor] = longest[current] + current.neighbors[neighbor]
		else:
			longest[neighbor] = max(longest[neighbor], longest[current] + current.neighbors[neighbor])
		queue.append(neighbor)

t2 = time.process_time()

print(longest[goal])
print("Time: %f" % (t2 - t1))
