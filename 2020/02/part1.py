#!/usr/bin/python3

from collections import Counter


# 1-3 a: abcde
def parse_line(ln):
	parts = ln.split()
	range_parts = parts[0].split('-')
	return (int(range_parts[0]), int(range_parts[1]), parts[1][0], parts[2])


valid_count = 0

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		min_count, max_count, ltr, password = parse_line(line)
		counts = Counter(password)
		if (ltr in counts) and (min_count <= counts[ltr] <= max_count):
			valid_count += 1

print(valid_count)
