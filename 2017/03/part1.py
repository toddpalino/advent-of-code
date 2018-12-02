#!/usr/bin/python

inputs = [1, 12, 23, 1024, 347991]

for n in inputs:
	if n == 1:
		print("{0} = {1}".format(n, 0))
		continue

	x = 1
	east = 2
	north = 4
	west = 6
	south = 8
	while True:
		size_of_square = x * 8
		length_of_side = size_of_square / 4
		side_minus = (length_of_side / 2) - 1
		side_plus = length_of_side / 2

		if (n >= east - side_minus) and (n <= east + side_plus):
			offset = abs(n - east)
			print("{0} = {1}".format(n, x + offset))
			break
		if (n >= north - side_minus) and (n <= north + side_plus):
			offset = abs(n - north)
			print("{0} = {1}".format(n, x + offset))
			break
		if (n >= west - side_minus) and (n <= west + side_plus):
			offset = abs(n - west)
			print("{0} = {1}".format(n, x + offset))
			break
		if (n >= south - side_minus) and (n <= south + side_plus):
			offset = abs(n - south)
			print("{0} = {1}".format(n, x + offset))
			break

		x += 1
		east += 1 + size_of_square
		north += 3 + size_of_square
		west += 5 + size_of_square
		south += 7 + size_of_square
