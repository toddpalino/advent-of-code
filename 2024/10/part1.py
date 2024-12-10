#!/usr/bin/python3

import time
from collections import deque

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [[int(x) for x in ln.strip()] for ln in f]
len_x = len(grid[0])
len_y = len(grid)

# Find all the trailheads
trailheads = {}
for x in range(len_x):
	for y in range(len_y):
		if grid[y][x] == 0:
			trailheads[(x, y)] = {'trails': 0, 'endpoints': set()}

queue = deque((t, t) for t in trailheads.keys())
while queue:
	trailhead, current = queue.popleft()
	x = current[0]
	y = current[1]
	nh = grid[y][x] + 1
	for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
		if (0 <= nx < len_x) and (0 <= ny < len_y):
			if grid[ny][nx] == nh:
				if nh == 9:
					trailheads[trailhead]['trails'] += 1
					trailheads[trailhead]['endpoints'].add((nx, ny))
				else:
					queue.append((trailhead, (nx, ny)))

print("Sum of trailhead scores: %d" % (sum(len(t['endpoints']) for t in trailheads.values())))
print("Sum of trailhead ratings: %d" % (sum(t['trails'] for t in trailheads.values())))
				
end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
