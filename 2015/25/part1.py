#!/usr/bin/python3

import time

# Test input - 9250759
#row = 5
#col = 5

# Puzzle input
row = 2978
col = 3083

def num_in_series(row, col):
	# Calc the start of the row first
	val = 1
	for r in range(2, row + 1):
		val += r - 1

	# Now move to the column
	for c in range(2, col + 1):
		val += row + c - 1
	return val

def next_code(prev):
	return (prev * 252533) % 33554393

def code_in_sequence(n):
	val = 20151125
	for _ in range(n - 1):
		val = next_code(val)
	return val

n = num_in_series(row, col)
code = code_in_sequence(n)

print("Activation code: %d" % (code))

start_time = time.time()

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
