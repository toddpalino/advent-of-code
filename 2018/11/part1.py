#!/usr/bin/env python3

import sys

def calculate_power(levels, grid, x, y):
	if (x, y) not in levels:
		# Find the fuel cell's rack ID, which is its X coordinate plus 10.
		# Begin with a power level of the rack ID times the Y coordinate.
		# Increase the power level by the value of the grid serial number (your puzzle input).
		# Set the power level to itself multiplied by the rack ID.
		# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
		# Subtract 5 from the power level.
		rack_id = x + 10
		level = int(((((rack_id * y) + grid) * rack_id) % 1000) / 100) - 5
		levels[(x, y)] = level
	return levels[(x, y)]


if len(sys.argv) != 2:
	print("usage: part1.py <grid serial>")
	sys.exit(1)

grid_serial = int(sys.argv[1])

levels = {}

max_power = 0
max_coords = None

for sx in range(298):
	for sy in range(298):
		power = sum(calculate_power(levels, grid_serial, x, y) for x in range(sx, sx + 3) for y in range(sy, sy + 3))
		if power > max_power:
			max_power = power
			max_coords = (sx, sy)

print("Max Power: {}".format(max_power))
print("Coords: {}".format(max_coords))
