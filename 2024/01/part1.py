#!/usr/bin/python3

#fn = "test.txt"
fn = "input.txt"

left = []
right = []

with open(fn, 'r') as f:
	for line in f:
		nums = line.split()
		left.append(int(nums[0]))
		right.append(int(nums[1]))

left.sort()
right.sort()
total_difference = sum(abs(pair[0] - pair[1]) for pair in zip(left, right))

print("Total difference: %d" % (total_difference))
