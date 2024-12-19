#!/usr/bin/env python

import time
from functools import cache

@cache
def is_pattern_possible(pattern):
	if len(pattern) == 0:
		return True

	# Find all patterns that are a prefix for this pattern
	for prefix in [towel for towel in towels if pattern.startswith(towel)]:
		if is_pattern_possible(pattern[len(prefix):]):
			return True
	return False

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	lines = [line.strip() for line in f]
	towels = lines[0].split(', ')
	patterns = lines[2:]

count = sum(is_pattern_possible(pattern) for pattern in patterns)
print(f"Patterns that can be created: {count}")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
