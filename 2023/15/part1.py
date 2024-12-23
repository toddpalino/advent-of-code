#!/usr/bin/python3

from functools import reduce

def get_hash(step):
	return reduce(lambda hash, c: ((hash + ord(c)) * 17) % 256, step, 0)

with open("input.txt") as f:
	steps = f.read().strip().split(',')

hash_sum = reduce(lambda total, step: total + get_hash(step), steps, 0)
print("Sum: %d" % (hash_sum))
