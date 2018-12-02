#!/usr/bin/env python3

frequency = 0
frequencies = {}

with open("input", "r") as f:
	input = [int(line) for line in f]

first_duplicate = None
while first_duplicate is None:
	for val in input:
		frequency += val
		if frequency in frequencies:
			first_duplicate = frequency
			break
		frequencies[frequency] = True

print(first_duplicate)
