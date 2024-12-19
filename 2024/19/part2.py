#!/usr/bin/env python

import time
from functools import cache

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	lines = [line.strip() for line in f]
	towels = lines[0].split(', ')
	patterns = lines[2:]

@cache
def possible_designs(pattern):
	if len(pattern) == 0:
		return 1

	# Find all patterns that are a prefix for this pattern
	prefixes = [towel for towel in towels if pattern.startswith(towel)]
	return sum(possible_designs(pattern[len(prefix):]) for prefix in prefixes)

count = sum(possible_designs(pattern) for pattern in patterns)
print(f"Possible Designs: {count}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
