#!/usr/bin/python

# sample inputs
inputs = [[[5,1,9,5],[7,5,3],[2,4,6,8]]]

# Read in input
rows = []
with open("input", "r") as f:
	for line in f:
		rows.append([int(x) for x in line.strip().split()])
inputs.append(rows)

for input in range(len(inputs)):
	table = inputs[input]
	sum = 0

	for row in table:
		least = min(row)
		most = max(row)
		sum += most - least
	print("{0}: {1}".format(input, sum))
