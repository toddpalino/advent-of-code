#!/usr/bin/env python

import re
import time

def manhattan_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

bot_re = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')
bots = {}

with open(fn, 'r') as f:
	for line in f:
		m = bot_re.match(line)
		bots[(int(m.group(1)), int(m.group(2)), int(m.group(3)))] = int(m.group(4))

# Find the strongest bot
pos = max(bots, key=bots.get)
strength = bots[pos]

in_range = 0
for bot in bots.keys():
	if manhattan_distance(pos, bot) <= strength:
		in_range += 1

print("Bots in range: %d" % (in_range))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
