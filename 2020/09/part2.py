#!/usr/bin/python3

from itertools import combinations

# fn = "test.txt"
# preamble_length = 5

fn = "input.txt"
preamble_length = 25

all_nums = []

with open(fn) as f:
	for line in f:
		num = int(line)
		if len(all_nums) < preamble_length:
			all_nums.append(num)
			continue

		# Calculate sums of pairs in the buffer
		possibles = set(p[0] + p[1] for p in combinations(all_nums[-preamble_length:], 2))
		if num not in possibles:
			print(num)
			break

		all_nums.append(num)

i = len(all_nums) - 1
weakness_range = []
while i >= 0:
	if all_nums[i] > num:
		i -= 1
		continue
	for l in range(2, i+1):
		s = sum(all_nums[i-l:i])
		if s > num:
			i -= 1
			break
		if s == num:
			weakness_range = all_nums[i-l:i]
			break
	if weakness_range:
		break

print(weakness_range)
print(min(weakness_range) + max(weakness_range))
