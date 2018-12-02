#!/usr/bin/env python3

frequency = 0

with open("input", "r") as f:
	for line in f:
		frequency += int(line)

print(frequency)
