#!/usr/bin/python3

import time
from functools import reduce
from math import sqrt

#target = 150
target = 36000000


def factors(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__,
		   ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


start_time = time.time()

# If we div by 10 here, we can do the same in calculating for number of presents
target /= 10

house_num = 1
while True:
	if sum(factors(house_num)) >= target:
		break
	house_num += 1

print("House number: %d" % (house_num))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
