#!/usr/bin/python3


digit_strings = {
	'one': "1",
	'two': "2",
	'three': "3",
	'four': "4",
	'five': "5",
	'six': "6",
	'seven': "7",
	'eight': "8",
	'nine': "9"
}


def get_digit(str, idx):
	if str[idx].isdigit():
		return str[idx]
	else:
		for k, v in digit_strings.items():
			if str[idx:].startswith(k):
				return v
	return None


calibration = 0
with open('input.txt') as f:
	for line in f:
		cleaned_line = line.strip()

		cal_string = ""
		for i in range(len(cleaned_line)):
			digit = get_digit(cleaned_line, i)
			if digit is not None:
				cal_string += digit
				break
		for i in reversed(range(len(cleaned_line))):
			digit = get_digit(cleaned_line, i)
			if digit is not None:
				cal_string += digit
				break

		calibration += int(cal_string)

print(calibration)
