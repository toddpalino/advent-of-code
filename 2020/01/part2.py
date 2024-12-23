#!/usr/bin/python3

numbers = [False] * 2021

with open("input.txt") as f:
	for line in f:
		n = int(line)
		if n <= 2020:
			numbers[n] = True

for i in range(2020):
	if not numbers[i]:
		continue
	subtotal = 2020 - i
	for j in range(subtotal):
		if not numbers[j]:
			continue
		k = subtotal - j
		if not numbers[k]:
			continue
		print("%d * %d * %d = %d" % (i, j, k, i * j * k))

