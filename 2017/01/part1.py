#!/usr/bin/python

# sample inputs
#digits = "1122"
#digits = "1111"
#digits = "1234"
#digits = "91212129"

# Read in input
with open("input", "r") as f:
	line = f.read()
digits = line.strip()

sum = 0
for i in range(len(digits)):
	next = i + 1
	if i == (len(digits) - 1):
		next = 0
	if digits[i] == digits[next]:
		sum += int(digits[i])

print sum
