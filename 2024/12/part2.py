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
	sides = 0

	# Get a minimum and maximum x and y for the containing block
	min_x = 9999
	min_y = 9999
	max_x = 0
	max_y = 0
	for c in region:
		min_x = min(min_x, c[0])
		max_x = max(max_x, c[0])
		min_y = min(min_y, c[1])
		max_y = max(max_y, c[1])

	# For each row, find the number of contiguous plots with nothing to the north
	for y in range(min_y, max_y+1):
		x = min_x
		while x <= max_x:
			try:
				# Increment X until we find a plot in the region
				while (x, y) not in region or (x, y-1) in region:
					x += 1
					if x > max_x:
						raise StopIteration()
			except StopIteration:
				# We couldn't find a clear edge
				continue

			# Increment X until we find the end of the section
			while (x, y) in region and (x, y-1) not in region:
				x += 1

			# Increment the number of sides
			sides += 1

		# Do it again, looking for nothing to the south
		x = min_x
		while x <= max_x:
			try:
				# Increment X until we find a plot in the region
				while (x, y) not in region or (x, y+1) in region:
					x += 1
					if x > max_x:
						raise StopIteration()
			except StopIteration:
				# We couldn't find a clear edge
				continue

			# Increment X until we find the end of the section
			while (x, y) in region and (x, y+1) not in region:
				x += 1

			# Increment the number of sides
			sides += 1

	# For each column, find the number of contiguous plots with nothing to the west
	for x in range(min_x, max_x+1):
		y = min_y
		while y <= max_y:
			try:
				# Increment Y until we find a plot in the region
				while (x, y) not in region or (x-1, y) in region:
					y += 1
					if y > max_y:
						raise StopIteration()
			except StopIteration:
				# We couldn't find a clear edge
				continue

			# Increment Y until we find the end of the section
			while (x, y) in region and (x-1, y) not in region:
				y += 1

			# Increment the number of sides
			sides += 1

		# Do it again, looking for nothing to the east
		y = min_y
		while y <= max_y:
			try:
				# Increment Y until we find a plot in the region
				while (x, y) not in region or (x+1, y) in region:
					y += 1
					if y > max_y:
						raise StopIteration()
			except StopIteration:
				# We couldn't find a clear edge
				continue

			# Increment Y until we find the end of the section
			while (x, y) in region and (x+1, y) not in region:
				y += 1

			# Increment the number of sides
			sides += 1

	fence_cost += area * sides

print("Total fence cost: %d" % (fence_cost))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
