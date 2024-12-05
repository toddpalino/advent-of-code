#!/usr/bin/python3

#fn = "test.txt"
fn = "input.txt"

match_str = 'XMAS'

with open(fn, 'r') as f:
	grid = [line.strip() for line in f]

max_x = len(grid[0])
max_y = len(grid)


def strings_at(x, y, length):
	strings = []
	if x + length <= max_x:
		strings.append(grid[y][x:x+length])
		if y + length <= max_y:
			strings.append(''.join(grid[y+i][x+i] for i in range(0, length)))
		if y - length >= -1:
			strings.append(''.join(grid[y-i][x+i] for i in range(0, length)))
	if x - length >= -1:
		strings.append(grid[y][x-length+1:x+1][::-1])
		if y + length <= max_y:
			strings.append(''.join(grid[y+i][x-i] for i in range(0, length)))
		if y - length >= -1:
			strings.append(''.join(grid[y-i][x-i] for i in range(0, length)))
	if y + length <= max_y:
		strings.append(''.join(grid[y+i][x] for i in range(0, length)))
	if y - length >= -1:
		strings.append(''.join(grid[y-i][x] for i in range(0, length)))
	return strings


match_len = len(match_str)
first_char = match_str[0]
matches = 0

for y in range(max_y):
	for x in range(max_x):
		letter = grid[y][x]
		if letter != first_char:
			continue

		for s in strings_at(x, y, match_len):
			if s == match_str:
				matches += 1

print("Total matches: %d" % (matches))
