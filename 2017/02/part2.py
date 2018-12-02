#!/usr/bin/python

# sample inputs
inputs = [[[5,9,2,8],[9,4,7,3],[3,8,6,5]]]

# Read in input
rows = []
with open("input", "r") as f:
	for line in f:
		rows.append([int(x) for x in line.strip().split()])
inputs.append(rows)

def check_row(row):
	for p1 in range(len(row)):
		for p2 in range(p1 + 1, len(row)):
			n1 = row[p1]
			n2 = row[p2]
			if n1 % n2 == 0:
				return n1 / n2
			elif n2 % n1 == 0:
				return n2 / n1
	return 0

for input in range(len(inputs)):
	table = inputs[input]
	sum = 0

	for row in table:
		sum += check_row(row)
	print("{0}: {1}".format(input, sum))
