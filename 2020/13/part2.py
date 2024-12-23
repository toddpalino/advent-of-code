#!/usr/bin/python3

from functools import reduce

def multiplicative_inverse(a, b):
	if b == 1:
		return 1

	b0 = b
	x0, x1 = 0, 1
	while a > 1:
		quotient = a // b
		a, b = b, a % b
		x0, x1 = x1 - quotient * x0, x0
	if x1 < 0:
		x1 += b0
	return x1


def chinese_remainder(nums, remainders):
	rem_sum = 0
	prod = reduce(lambda a, b: a * b, nums)
	for num, remainder in zip(nums, remainders):
		p = prod // num
		rem_sum += remainder * multiplicative_inverse(p, num) * p
	return rem_sum % prod


#with open("test.txt") as f:
with open("input.txt") as f:
	ts = int(f.readline())
	id_strs = f.readline().split(',')


buses = []
remainders = []
for i in range(len(id_strs)):
	if id_strs[i] == 'x':
		continue

	bus_id = int(id_strs[i])
	buses.append(int(id_strs[i]))
	remainders.append(bus_id - i)

print(chinese_remainder(buses, remainders))
