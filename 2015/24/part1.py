#!/usr/bin/python3

import time
from itertools import combinations
from math import prod

#fn = "test.txt"
fn = "input.txt"

def combination_with_size(package_set, total):
	ary = sorted(list(package_set))

	# Figure out the maximum number of packages to reach the total
	max_num = 1
	while sum(ary[0:max_num]) < total:
		max_num += 1

	# Figure out the minimum number of package to reach the total
	min_num = 1
	while sum(ary[-min_num:]) < total:
		min_num += 1

	for i in range(min_num, max_num + 1):
		for c in combinations(ary, i):
			if sum(c) == total:
				yield set(c)


start_time = time.time()

with open(fn, 'r') as f:
	packages = set(int(weight) for weight in f.read().strip().split())

# Weight per compartment
group_weight = sum(packages) // 3

# Loop over every possible combination of packages for g1 (regardless of the other 2 groups)
# We only need the first one, because the combinations will come out in order of length and lower digits first
ideal_g1 = None
for g1 in combination_with_size(packages, group_weight):
	# Make sure that we can make at least one group 2 with the remaining packages
	remaining = packages - g1
	valid_g1 = False
	for g2 in combination_with_size(remaining, group_weight):
		ideal_g1 = tuple(g1)
		break
	if ideal_g1 is not None:
		break

print("Ideal Group 1: %s (QE: %d)" % (ideal_g1, prod(ideal_g1)))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
