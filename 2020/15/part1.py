#!/usr/bin/python3

inputs = [
	# Test inputs
	# [0, 3, 6],
	# [1, 3, 2],
	# [2, 1, 3],
	# [1, 2, 3],
	# [2, 3, 1],
	# [3, 2, 1],
	# [3, 1, 2],

	# Real input
	[0, 8, 15, 2, 12, 1, 4]
]

# Note - we are zero indexed, so the first number spoken is the 0th number.
max_i = 30000000

for input in inputs:
	spoken = {}

	# First rounds - just speaking the inputs
	for i in range(len(input)):
		spoken[input[i]] = i

	# Subsequent rounds - game rules
	last_num = input[-1]
	for i in range(len(input), max_i):
		# Figure out what number will be spoken in this round
		speak = 0
		if last_num in spoken:
			speak = i - spoken[last_num] - 1

		# Log the number spoken in the previous round and say the new one
		spoken[last_num] = i - 1
		last_num = speak

		if i == 2019:
			print("Inputs: %s - 2020: %d" % (input, last_num))

	print("Inputs: %s - 30m number: %d" % (input, last_num))
