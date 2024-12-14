#!/usr/bin/python3

import re
import time
from math import prod
from bots import chunk_list, position_at_tick, print_bots

fn = "input.txt"
len_x = 101
len_y = 103

ticks = 100

start_time = time.time()

with open(fn, 'r') as f:
	bots = list(chunk_list([int(n) for n in re.findall(r'-?\d+', f.read())], 4))

# What we are supposed to do for part 2 is very unclear - we're supposed to have the bots
# draw something, but we don't really know what except for "a christmas tree". But if
# we're going to draw something on a 101x103 grid, chances are we only have one bot per
# coordinate. We'll try that first, and move on to a different approach if we don't get
# a quick solution

i = 0
locs = None
num_bots = len(bots)
while True:
	i += 1
	locs = set(position_at_tick(i, len_x, len_y, *bot) for bot in bots)
	if len(locs) == num_bots:
		break

print_bots(locs, len_x, len_y)
print("Single positions after %d ticks" % (i))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
