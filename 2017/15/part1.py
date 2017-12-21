#!/usr/bin/python

# Real inputs
value_a = 634
value_b = 301

# Test inputs
#value_a = 65
#value_b = 8921

factor_a = 16807
factor_b = 48271

score = 0
for i in xrange(40000000):
	value_a = (value_a * factor_a) % 2147483647
	value_b = (value_b * factor_b) % 2147483647

	if (value_a & 0xFFFF) == (value_b & 0xFFFF):
		score += 1

print("SCORE: {0}".format(score))
