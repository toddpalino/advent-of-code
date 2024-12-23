#!/usr/bin/python3

screen = [list(40 * ".") for i in range(6)]
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

for i in range(len(screen)):
	for j in range(len(screen[i])):
		# +1 because ticks starts at index 1, (0 is a placeholder)
		tick = (i * 40) + j + 1
		x = ticks[tick]
		if (x - 1) <= j <= (x + 1):
			screen[i][j] = '#'

for i in range(len(screen)):
	print(''.join(screen[i]))
