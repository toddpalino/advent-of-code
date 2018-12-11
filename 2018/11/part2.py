#!/usr/bin/env python3

import sys

def calculate_power(grid, x, y):
	# Find the fuel cell's rack ID, which is its X coordinate plus 10.
	# Begin with a power level of the rack ID times the Y coordinate.
	# Increase the power level by the value of the grid serial number (your puzzle input).
	# Set the power level to itself multiplied by the rack ID.
	# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
	# Subtract 5 from the power level.
	rack_id = x + 10
	return int(((((rack_id * y) + grid) * rack_id) % 1000) / 100) - 5


if len(sys.argv) != 2:
	print("usage: part1.py <grid serial>")
	sys.exit(1)
grid_serial = int(sys.argv[1])

# Create summed area table (https://en.m.wikipedia.org/wiki/Summed-area_table)
sa_table = [[0] * 300 for i in range(300)]

# Special case for x or y = 0
sa_table[0][0] = calculate_power(grid_serial, 0, 0)
for x in range(1, 300):
	sa_table[x][0] = calculate_power(grid_serial, x, 0) + sa_table[x-1][0]
for y in range(1, 300):
	sa_table[0][y] = calculate_power(grid_serial, 0, y) + sa_table[0][y-1]

for x in range(1, 300):
	for y in range(1, 300):
		sa_table[x][y] = calculate_power(grid_serial, x, y) + sa_table[x][y-1] + sa_table[x-1][y] - sa_table[x-1][y-1]

max_power = 0
max_coords = None
max_size = None

for grid_size in range(300, 0, -1):
	# The max cell power level is 9, so the max score of a square of this size is 9*size^2.
	# If we've already found a max score greater than that, we're done
	if max_power >= 9 * grid_size * grid_size:
		break

	for x in range(0, 300 - grid_size + 1):
		for y in range(0, 300 - grid_size + 1):
			mx = x + grid_size - 1
			my = y + grid_size - 1
			power = sa_table[mx][my]
			if x > 0:
				power -= sa_table[x-1][my]
			if y > 0:
				power -= sa_table[mx][y-1]
			if x > 0 and y > 0:
				power += sa_table[x-1][y-1]

			if power > max_power:
				max_power = power
				max_coords = (x, y)
				max_size = grid_size

print("Max Power: {}".format(max_power))
print("Coords: {}".format(max_coords))
print("Size: {}".format(max_size))
