#!/usr/bin/python3

# 1-3 a: abcde
def parse_line(ln):
	parts = ln.split()
	range_parts = parts[0].split('-')
	return (int(range_parts[0]) - 1, int(range_parts[1]) - 1, parts[1][0], parts[2])


valid_count = 0

#with open("test.txt") as f:
with open("input.txt") as f:
	for line in f:
		pos1, pos2, ltr, password = parse_line(line)
		if (password[pos1] == ltr) ^ (password[pos2] == ltr):
			valid_count += 1

print(valid_count)
