#!/usr/bin/python3

import re

calibration = []
with open('input.txt') as f:
	for line in f:
		numbers = re.sub("[^0-9]", "", line)
		calibration_string = numbers[0] + numbers[-1]
		calibration.append(int(calibration_string))

print(sum(calibration))
