#!/usr/bin/env python

import re
import time
from collections import deque
from itertools import product
from aoc.utils.priorityq import PriorityQueue

clockwise = {(1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (-1, 0), (0, -1): (1, 0)}
counterclockwise = {(1, 0): (0, -1), (-1, 0): (0, 1), (0, 1): (1, 0), (0, -1): (-1, 0)}

def check_and_add(item, prev_item, new_score, queue, visited, scores, prev):
	if item not in scores:
		scores[item] = new_score
		prev[item] = set([prev_item])
	elif new_score == scores[item]:
		prev[item].add(prev_item)
		return
	elif new_score < scores[item]:
		scores[item] = new_score
		prev[item] = set([prev_item])
	if item not in visited:
		queue.add(item, new_score)


#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [list(ln.strip()) for ln in f]
len_x = len(grid[0])
len_y = len(grid)

# Find start and end
start = None
end = None
for x, y in product(range(len_x), range(len_y)):
	c = grid[y][x]
	if c == 'S':
		start = (x, y)
		grid[y][x] = '.'
	if c == 'E':
		end = (x, y)
		grid[y][x] = '.'

start_vec = (1, 0)
start_item = (start, start_vec)

prev = {}
scores = { start_item: 0 }
visited = set()
queue = PriorityQueue()
queue.add(start_item, 0)
while queue:
	try:
		score, item = queue.pop()
	except KeyError:
		# Empty queue
		break
	x, y = item[0]
	vec = item[1]
	visited.add(item)

	# Find blocks we can move to
	for nvec in ((0, 1), (0, -1), (1, 0), (-1, 0)):
		nx = x + nvec[0]
		ny = y + nvec[1]
		nc = grid[ny][nx]
		if nc == '#':
			continue
		if nvec == vec:
			check_and_add(((nx, ny), nvec), item, score + 1, queue, visited, scores, prev)
		else:
			new_score = score + 1000
			if nvec[0] == -vec[0] or nvec[1] == -vec[1]:
				# 180 degree turn. Add both
				new_item = ((x, y), clockwise[vec])
				check_and_add(((x, y), clockwise[vec]), item, new_score, queue, visited, scores, prev)
				check_and_add(((x, y), counterclockwise[vec]), item, new_score, queue, visited, scores, prev)
			else:
				check_and_add(((x, y), nvec), item, new_score, queue, visited, scores, prev)

# Part 1 - What is the lowest score
lowest_score = None
end_items = []
for nvec in ((0, 1), (0, -1), (1, 0), (-1, 0)):
	item = (end, nvec)
	if item in scores:
		if lowest_score is None:
			lowest_score = scores[item]
			end_items.append(item)
		if scores[item] < lowest_score:
			end_items = [item]
			lowest_score = scores[item]
		elif scores[item] == lowest_score:
			end_items.append(item)

print("Lowest score to finish: %d" % (lowest_score))

# Part 2 - Rebuild all lowest cost paths and get number of nodes visited
visited = set()
queue = deque(end_items)
while queue:
	pos = queue.popleft()
	visited.add(pos)
	if pos == start or pos not in prev:
		continue
	for npos in prev[pos]:
		if npos not in visited:
			queue.append(npos)

visited_nodes = set(item[0] for item in visited)
print("Visited positions: %d" % (len(visited_nodes)))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
