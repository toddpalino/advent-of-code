#!/usr/bin/python

# sample inputs
inputs = ["1212", "1221", "123425", "123123", "12131415"]

# Read in input
with open("input", "r") as f:
	line = f.read()
inputs.append(line.strip())

for input in range(len(inputs)):
	digits = inputs[input]
	digits_len = len(digits)

	# part 1 and part 2
	#advance = 1
	advance = digits_len / 2

	sum = 0
	for i in range(len(digits)):
		match = (i + advance) % digits_len
		if digits[i] == digits[match]:
			sum += int(digits[i])
	print("{0}: {1}".format(input, sum))
