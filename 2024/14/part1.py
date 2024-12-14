#!/opt/homebrew/bin/python3

import re
import time
from itertools import batched
from math import prod
from bots import position_at_tick, quadrant_counts

# Test input
#fn = "test.txt"
#len_x = 11
#len_y = 7

fn = "input.txt"
len_x = 101
len_y = 103

ticks = 100

start_time = time.time()

with open(fn, 'r') as f:
	bots = list(batched([int(n) for n in re.findall(r'-?\d+', f.read())], n=4, strict=True))

locs = [position_at_tick(100, len_x, len_y, *bot) for bot in bots]
quadrants = quadrant_counts(locs, len_x, len_y)

print("Safety factor: %d" % (prod(quadrants)))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
