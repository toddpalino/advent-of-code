#!/usr/bin/python

# Real input
list_size = 256
lengths = [34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167]

# Test inputs
#list_size = 5
#lengths = [3, 4, 1, 5]

list = range(list_size)
ptr = 0
skip = 0

for length in lengths:
	# Get the section to reverse
	end_ptr = ptr + length
	if end_ptr > list_size:
		beginning_length = end_ptr - list_size
		section = list[ptr:] + list[0:beginning_length]
	else:
		section = list[ptr:end_ptr]

	# Reverse the list entries
	for i in reversed(range(len(section))):
		list[ptr] = section[i]
		ptr = (ptr + 1) % list_size

	# Skip and increase skip size
	ptr = (ptr + skip) % list_size
	skip += 1

print("LIST: {0}".format(list))
print("MULT: {0}".format(list[0] * list[1]))
