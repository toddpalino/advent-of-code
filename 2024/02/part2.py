#!/usr/bin/python3

#fn = "test.txt"
fn = "input.txt"

def is_safe(report):
        differences = None
        if report[-1] > report[0]:
                differences = [report[i] - report[i-1] for i in range(1, len(report))]
        else:
                differences = [report[i-1] - report[i] for i in range(1, len(report))]
        return min(differences) > 0 and max(differences) <= 3


def is_safe_damped(report):
	if is_safe(report):
		return True

	num_levels = len(report)
	for i in range(num_levels):
		if is_safe(report[0:i] + report[i+1:num_levels]):
			return True

	return False


with open(fn, 'r') as f:
	reports = [[int(num) for num in ln.split()] for ln in f]

total_safe = sum(int(is_safe_damped(report)) for report in reports)

print("Total safe: %d" % (total_safe))
