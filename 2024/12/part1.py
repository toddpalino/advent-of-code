#!/usr/bin/python3

import time
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
