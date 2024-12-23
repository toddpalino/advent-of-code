import re
from itertools import batched
from aoc.utils.priorityq import PriorityQueue

def add_bytes(grid, byte_list):
	for x, y in byte_list:
		grid[y][x] = '#'

def read_bytes(filename):
	with open(filename, 'r') as f:
		byte_list = list(batched([int(x) for x in re.findall(r'(\d+)', f.read())], 2))
	return byte_list

def create_grid(size):
	return [['.'] * size for _ in range(size)]

def find_shortest_path(grid, start, end):
	grid_len = len(grid)

	prev = {}
	score = { start: 0 }
	visited = set()
	queue = PriorityQueue()
	queue.add(start, 0)
	while queue:
		try:
			cost, item = queue.pop()
		except KeyError:
			# Empty queue
			break
		x, y = item
		visited.add(item)

		# Find blocks we can move to
		for ncoord in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
			nx, ny = ncoord
			if not ((0 <= nx < grid_len) and (0 <= ny < grid_len)):
				continue
			if grid[ny][nx] == '#' or ncoord in visited:
				continue

			ncost = cost + 1
			if ncoord not in score or ncost < score[ncoord]:
				score[ncoord] = ncost
				prev[ncoord] = item
			queue.add((nx, ny), ncost)
	return score[end] if end in score else None

