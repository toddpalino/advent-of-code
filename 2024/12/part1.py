#!/usr/bin/python3

import time
from collections import deque

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [line.strip() for line in f]
len_x = len(grid[0])
len_y = len(grid)

regions = []

# Put all the coords into a set which we'll use to figure out what we haven't looked at
coords = set((x, y) for x in range(len_x) for y in range(len_y))

while coords:
	# Pull any coord from the set
	c = coords.pop()
	l = grid[c[1]][c[0]]

	# Create an empty region
	r = set([c])
	queue = deque([c])
	while queue:
		x, y = queue.popleft()
		for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
			if not ((0 <= nx < len_x) and (0 <= ny < len_y)):
				continue
			n = (nx, ny)
			if n not in coords:
				continue
			if grid[ny][nx] == l:
				# This adjacent plot is in the same region
				coords.remove(n)
				r.add(n)
				queue.append(n)

	regions.append(r)

fence_cost = 0
for region in regions:
	area = len(region)
	perimeter = 0

	for c in region:
		x = c[0]
		y = c[1]

		# Figure out how many sides of this plot do not have an adjacent plot in the region
		perimeter += sum(1 for n in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)) if n not in region)

	fence_cost += area * perimeter

print("Total fence cost: %d" % (fence_cost))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
