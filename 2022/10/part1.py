#!/usr/bin/python3

ticks = [1]
x = 1

with open("input.txt") as f:
	for line in f:
		cleaned = line.strip()

		if cleaned == "noop":
			ticks.append(x)
		else:
			parts = cleaned.split(' ')
			ticks.extend([x, x])
			x += int(parts[1])

print(sum(ticks[i] * i for i in [20, 60, 100, 140, 180, 220]))

