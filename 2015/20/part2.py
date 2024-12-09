#!/usr/bin/python3

import time
from functools import reduce
from math import sqrt

target = 36000000

max_houses = 50


def factors(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__,
		   ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def presents_for_house(house_num):
	return sum(factor for factor in factors(house_num) if (max_houses * factor) >= house_num) * 11

start_time = time.time()

house_num = 1
while True:
	if presents_for_house(house_num) >= target:
		break
	house_num += 1

print("House number: %d" % (house_num))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
