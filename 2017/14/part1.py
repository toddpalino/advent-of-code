#!/usr/bin/python

import sys
import time

def knot_hash(key_string, rounds=64):
	lengths = [ord(c) for c in key_string] + [17, 31, 73, 47, 23]
	hash = range(256)

	ptr = 0
	skip = 0
	list_size = len(hash)

	for round in range(rounds):
		for length in lengths:
			# Get the section to reverse
			end_ptr = ptr + length
			if end_ptr > list_size:
				beginning_length = end_ptr - list_size
				section = hash[ptr:] + hash[0:beginning_length]
			else:
				section = hash[ptr:end_ptr]

			# Reverse the list entries
			for i in reversed(range(len(section))):
				hash[ptr] = section[i]
				ptr = (ptr + 1) % list_size

			# Skip and increase skip size
			ptr = (ptr + skip) % list_size
			skip += 1

	# Convert to hex string
	dense_hash = ''
	for i in range(0, list_size, 16):
		c = 0
		for j in range(i, i + 16):
			c ^= hash[j]
		dense_hash += format(c, '02x')

	return dense_hash


def print_grid(grid):
	size = len(grid)
	for i in range(size):
		for j in range(size):
			if grid[i][j]:
				sys.stdout.write('#')
			else:
				sys.stdout.write('.')
		print


# Real input
key_string = 'vbqugkhl'

# Test inputs
#key_string = 'flqrgnkx'

grid = []
size = 128
for i in range(size):
	line = [False] * size
	line_hash = knot_hash("{0}-{1}".format(key_string, i))
	bin_str = bin(int(line_hash, 16))[2:].zfill(size)
	for j in range(len(bin_str)):
		line[j] = bin_str[j] == '1'
	grid.append(line)

count = 0
for i in range(size):
	for j in range(size):
		if grid[i][j]:
			count += 1

# Counting regions is essentially flood filling False values, counting each time
regions = 0
start_x = 0
start_y = 0
printed = False
while start_y < size:
	# Find next used square
	if grid[start_y][start_x]:
		regions += 1
		coords = [(start_x, start_y)]
		while len(coords) > 0:
			c = coords.pop()
			x = c[0]
			y = c[1]

			# Blank the block so we don't count it again
			grid[y][x] = None

			# Add neighbors to the region
			if (x > 0) and grid[y][x-1]:
				coords.append((x-1, y))
			if (x < (size-1)) and grid[y][x+1]:
				coords.append((x+1, y))
			if (y > 0) and grid[y-1][x]:
				coords.append((x, y-1))
			if (y < (size-1)) and grid[y+1][x]:
				coords.append((x, y+1))

	start_x += 1
	if start_x == size:
		start_x = 0
		start_y += 1



print("USED: {0}".format(count))
print("REGIONS: {0}".format(regions))
