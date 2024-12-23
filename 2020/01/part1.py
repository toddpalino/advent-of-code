#!/usr/bin/python3

numbers = [False] * 2021

with open("input.txt") as f:
	for line in f:
		n = int(line)
		if n <= 2020:
			numbers[n] = True

for n in range(2020):
	if not numbers[n]:
		continue
	m = 2020 - n
	if not numbers[m]:
		continue
	print("%d * %d = %d" % (n, m, n * m))

