#!/usr/bin/python3

from collections import deque

mask = [None] * 36
mem = {}

#with open("test2.txt") as f:
with open("input.txt") as f:
	for line in f:
		if line.startswith("mask"):
			mask = [None if c == 'X' else int(c) for c in line[7:-1]]
			continue
		if line.startswith("mem"):
			parts = line.split(' = ')
			val = int(parts[1])

			# Convert the mem location to a 36-bit binary string (as list)
			loc = list(format(int(parts[0][4:-1]), '036b'))

			# Apply the mask, replacing 1s where needed and inserting X if variable
			for i in range(36):
				if mask[i] is None:
					loc[i] = 'X'
				elif mask[i] == 1:
					loc[i] = '1'

			# Generate addresses to write
			addrs = deque()
			queue = deque([''.join(loc)])
			while queue:
				a = queue.pop()
				if 'X' in a:
					queue.appendleft(a.replace('X', '0', 1))
					queue.appendleft(a.replace('X', '1', 1))
				else:
					addrs.append(int(a, 2))

			# Write the value to the memory locations
			for loc in addrs:
				mem[loc] = val

print(sum(mem.values()))

