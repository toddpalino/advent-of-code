#!/usr/bin/python3

from collections import deque
from itertools import combinations

# fn = "test.txt"
# preamble_length = 5

fn = "input.txt"
preamble_length = 25

buffer = deque(maxlen = preamble_length)

with open(fn) as f:
	for line in f:
		num = int(line)
		if len(buffer) < preamble_length:
			buffer.append(num)
			continue

		# Calculate sums of pairs in the buffer
		possibles = set(p[0] + p[1] for p in combinations(buffer, 2))
		if num not in possibles:
			print(num)
			break
		else:
			buffer.append(num)
