#!/usr/bin/python3

def calculate_load(platform):
	row_count = len(platform)
	return sum(row.count('O') * (row_count - i) for i, row in enumerate(platform))

def print_platform(platform):
	for row in platform:
		print(''.join(row))

def tilt_north(platform):
	for x in range(len(platform[0])):
		space = 0
		for y in range(len(platform)):
			c = platform[y][x]
			if c == '#':
				space = 0
			elif c == '.':
				space += 1
			else:
				if space > 0:
					platform[y-space][x] = 'O'
					platform[y][x] = '.'
	return platform

platform = []
with open("input.txt") as f:
	for line in f:
		platform.append(list(line[0:-1]))

# Rotate CW so north points right
platform = tilt_north(platform)

print_platform(platform)
print(calculate_load(platform))
