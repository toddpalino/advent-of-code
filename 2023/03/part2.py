#!/usr/bin/python3

engine = []

with open('input.txt') as f:
	for line in f:
		engine.append(list(line.strip()))

	for i in range(len(engine)):
		for j in range(len(engine[i])):
			if engine[i][j] == '.':
				engine[i][j] = None

max_i = len(engine)
max_j = len(engine[0])

gears = {}

i = 0
while i < max_i:
	j = 0
	while j < max_j:
		if engine[i][j] is not None and engine[i][j].isdigit():
			end = j + 1
			while (end < max_j) and (engine[i][end] is not None) and (engine[i][end].isdigit()):
				end += 1
			number = int(''.join(engine[i][j:end]))

			symbol = None
			try:
				for s_i in range(i-1, i+2):
					for s_j in range(j-1, end+1):
						if (0 <= s_i < max_i) and (0 <= s_j < max_j) and (engine[s_i][s_j] == '*'):
							gear = (s_i, s_j)
							print("Potential gear at (%d, %d) with %d" % (s_i, s_j, number))

							if gear not in gears:
								gears[gear] = [number]
							else:
								gears[gear].append(number)
							raise ValueError
			except ValueError:
				pass

			j = end
		else:
			j += 1
	i += 1

total_ratios = 0
for _, vals in gears.items():
	if len(vals) == 2:
		total_ratios += vals[0] * vals[1]

print(gears)
print(total_ratios)
