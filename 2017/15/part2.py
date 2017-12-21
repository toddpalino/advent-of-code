#!/usr/bin/python

# Real inputs
value_a = 634
value_b = 301

# Test inputs
#value_a = 65
#value_b = 8921

factor_a = 16807
factor_b = 48271

max_count = 5000000
score_a = [0] * max_count
idx_a = 0
score_b = [0] * max_count
idx_b = 0

while True:
	if idx_a < max_count:
		value_a = (value_a * factor_a) % 2147483647
		if value_a % 4 == 0:
			score_a[idx_a] = value_a & 0xFFFF
			idx_a += 1

	if idx_b < max_count:
		value_b = (value_b * factor_b) % 2147483647
		if value_b % 8 == 0:
			score_b[idx_b] = value_b & 0xFFFF
			idx_b += 1

	if (idx_a >= max_count) and (idx_b >= max_count):
		break

score = 0
for i in xrange(max_count):
	if score_a[i] == score_b[i]:
		score += 1

print("SCORE: {0}".format(score))
