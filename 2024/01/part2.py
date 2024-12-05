#!/usr/bin/python3

from collections import Counter

#fn = "test.txt"
fn = "input.txt"

left = []
right = []

with open(fn, 'r') as f:
	for line in f:
		nums = line.split()
		left.append(int(nums[0]))
		right.append(int(nums[1]))

right_counts = Counter(right)
similarity = sum(num * right_counts[num] for num in left)

print("Similarity: %d" % (similarity))
