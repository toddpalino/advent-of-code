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

@cache
def possible_designs(pattern):
	if len(pattern) == 0:
		return 1

	# Find all patterns that are a prefix for this pattern
	prefixes = [towel for towel in towels if pattern.startswith(towel)]
	return sum(possible_designs(pattern[len(prefix):]) for prefix in prefixes)

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	lines = [line.strip() for line in f]
	towels = lines[0].split(', ')
	patterns = lines[2:]

valid_patterns = [pattern for pattern in patterns if is_pattern_possible(pattern)]
print(f"Patterns that can be created: {len(valid_patterns)}")

p1_time = time.time()
print("Part 1 time: %f" % (p1_time - start_time))
print()

count = sum(possible_designs(pattern) for pattern in valid_patterns)
print(f"Possible Designs: {count}")

end_time = time.time()
print("Part 2 time: %f" % (end_time - p1_time))
