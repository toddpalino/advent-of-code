#!/usr/bin/python3

# The challenge for part 2 is to count sides. The easy way I came up with to do this is to look at
# the rectangle that contains the region and look at each row and then each column to determine
# how many contiguous sections of plots there are with nothing beside them (outside edges).
#
# For example, given a row we are looking at and the one above it: (. is not in region)
#
#      .......A......
#      ...AA..A..A...
#
# there are 2 contiguous blocks of A plots, which means 2 sides. The middle A in the bottom row
# is not counted because the top edge is not an outside edge of the region (there's an A above)

import time
from collections import deque
from regions import make_regions

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	grid = [line.strip() for line in f]

regions = make_regions(grid)

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

	# For each row, find the number of contiguous plots that are outside edges
	for y in range(min_y, max_y+1):
		# Do this twice, once with the outside as the north, and once for the south
		for outside in (-1, 1):
			x = min_x
			while x <= max_x:
				try:
					# Increment X until we find a plot in the region
					while (x, y) not in region or (x, y+outside) in region:
						x += 1
						if x > max_x:
							raise StopIteration()
				except StopIteration:
					# We couldn't find a clear edge
					continue

				# Increment X until we find the end of the section
				while (x, y) in region and (x, y+outside) not in region:
					x += 1

				# Increment the number of sides
				sides += 1

	# For each column find the number of contiguous plots that are outside edges
	for x in range(min_x, max_x+1):
		# Do this twice, once with the outside as the west, and once for the east
		for outside in (-1, 1):
			y = min_y
			while y <= max_y:
				try:
					# Increment Y until we find a plot in the region
					while (x, y) not in region or (x+outside, y) in region:
						y += 1
						if y > max_y:
							raise StopIteration()
				except StopIteration:
					# We couldn't find a clear edge
					continue

				# Increment Y until we find the end of the section
				while (x, y) in region and (x+outside, y) not in region:
					y += 1

				# Increment the number of sides
				sides += 1

	fence_cost += area * sides

print("Total fence cost: %d" % (fence_cost))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
