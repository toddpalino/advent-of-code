#!/usr/bin/python3

def find_horizontal_reflection(pattern):
	found_reflection = 0
	num_rows = len(pattern)
	for i in range(len(pattern) - 1):
		if pattern[i] == pattern[i+1]:
			found_reflection = i+1
			rows_to_compare = min(i, num_rows - (i + 2))
			for j in range(1, rows_to_compare + 1):
				if pattern[i-j] != pattern[i+j+1]:
					found_reflection = 0
					break
		if found_reflection:
			return found_reflection
	return found_reflection


sum_rows = 0
sum_cols = 0

patterns = []
with open("input.txt") as f:
	pattern = []
	for line in f:
		if len(line) == 1:
			patterns.append(pattern)
			pattern = []
			continue
		pattern.append(line[0:-1])
	patterns.append(pattern)

for i, pattern in enumerate(patterns):
	found_reflection = find_horizontal_reflection(pattern)
	if found_reflection:
		sum_rows += found_reflection
	else:
		# Rotate pattern 90 degrees clockwise so cols become rows
		pattern = list(zip(*pattern[::-1]))
		found_reflection = find_horizontal_reflection(pattern)
		if found_reflection:
			sum_cols += found_reflection
		else:
			print("No reflection found: %d" % (i))

print(sum_cols + (100 * sum_rows))
