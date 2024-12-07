#!/usr/bin/python3

import time
from collections import deque

#fn = "test.txt"
fn = "input.txt"

start_time = time.time()

equations = []

with open(fn, 'r') as f:
	for line in f:
		total_str, nums = line.strip().split(': ')
		equations.append([int(total_str), [int(num) for num in nums.split()]])

total_calibration = 0

for equation in equations:
	target = equation[0]
	nums = equation[1]
	len_nums = len(nums)

	# Queue entries will be a tuple of (index of last used num, total at this point)
	queue = deque([(0, nums[0])])

	while queue:
		item = queue.popleft()
		idx = item[0] + 1
		num = nums[idx]
		total = item[1]

		total_add = total + num
		total_mul = total * num
		total_concat = int(str(total) + str(num))
		if idx + 1 >= len_nums:
			if total_add == target or total_mul == target or total_concat == target:
				total_calibration += target
				break
		else:
			if total_add <= target:
				queue.append((idx, total_add))
			if total_mul <= target:
				queue.append((idx, total_mul))
			if total_concat <= target:
				queue.append((idx, total_concat))

print("Total calibration result: %d" % (total_calibration))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
