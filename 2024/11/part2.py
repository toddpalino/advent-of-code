#!/usr/bin/python3

import time
from functools import cache
from collections import Counter

#fn = "test.txt"
#iterations = 6

fn = "input.txt"
iterations = 75

def strip_extra_zeros(s):
	new_s = s.lstrip('0')
	return new_s if len(new_s) > 0 else '0'

@cache
def transform(num):
	if num == '0':
		return ['1']
	elif len(num) % 2 == 0:
		halfway = len(num) // 2
		return [strip_extra_zeros(num[0:halfway]), strip_extra_zeros(num[halfway:])]
	else:
		return [str(int(num) * 2024)]

start_time = time.time()

with open(fn, 'r') as f:
	# Storing these as strings since most of the time we want string manipulation
	stones = Counter(f.read().strip().split())

for _ in range(iterations):
	new_counter = Counter()
	for num in stones:
		for s in transform(num):
			new_counter[s] += stones[num]
	stones = new_counter

print("Number of stones: %d" % (sum(stones.values())))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
