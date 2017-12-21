#!/usr/bin/python

# Input
steps = 348

# Test input
#steps = 3

position_in_buffer = 0
after = 0

# i is the number of items in the buffer
for i in xrange(1, 50000001):
	# Step forwards to the next spot to insert
	position_in_buffer = ((position_in_buffer + steps) % i) + 1

	# If we're at position 1, keep track of what we would insert here
	if position_in_buffer == 1:
		after = i

print("AFTER 0: {0}".format(after))
