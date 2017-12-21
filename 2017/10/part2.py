#!/usr/bin/python

def knot_hash(hash, lengths, rounds=64):
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
	return hash

# Real input
length_strings = ['34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167']

# Test inputs
#length_strings = [
#	'',
#	'AoC 2017',
#	'1,2,3',
#	'1,2,4'
#]

for input in length_strings:
	# Calculate lengths
	lengths = [ord(c) for c in input] + [17, 31, 73, 47, 23]

	# Starting hash
	list_size = 256
	starting_hash = range(list_size)

	# Sparse hash
	sparse_hash = knot_hash(starting_hash, lengths)

	# Dense hash
	dense_hash = ''
	for i in range(0, list_size, 16):
		c = 0
		for j in range(i, i + 16):
			c ^= sparse_hash[j]
		dense_hash += format(c, '02x')

	print dense_hash
