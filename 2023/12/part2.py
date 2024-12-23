#!/usr/bin/python3

from functools import cache

@cache
def check(row, groups):
	# Exit criteria - ran out of input
	if not groups:
		# If no more groups, we're possible only if there's no more # in the row
		return (0 if '#' in row else 1)
	if '#' not in row and '?' not in row:
		# If more groups, we HAVE to have ? or # in the row
		return 0

	first_char = row[0]
	if first_char == '.':
		return check(row[1:], groups)

	possibilities = 0
	if first_char == '?':
		# Get possibilities if it's a . (like above)
		possibilities = check(row[1:], groups)

	# First char is either # or ?, and here we're going to treat it as #
	# Get the next group size
	num_hashes = groups[0]

	# Make sure we have enough input
	row_len = len(row)
	if row_len < num_hashes:
		return possibilities

	# Check that the next num_hashes-1 chars are either ? or # as well
	for i in range(1, num_hashes):
		if row[i] not in '?#':
			return possibilities

	# Check that the following char is a ? or . if there is more input
	if row_len > num_hashes and row[num_hashes] not in '?.':
		return possibilities

	# Check the rest of the input
	return possibilities + check(row[num_hashes+1:], groups[1:])


possible_solutions = 0
with open("input.txt") as f:
	for line in f:
		parts = line[0:-1].split(' ')
		groups = tuple([int(x) for x in parts[1].split(',')] * 5)
		row = '?'.join([parts[0]] * 5)

		possible_solutions += check(row, groups)

print(possible_solutions)
