#!/usr/bin/python

from math import sqrt

def isPrime(num):
	for i in range(2, int(sqrt(num))):
		if num % i == 0:
			return False
	return True

b = 108100
c = 125100

# Decomposition of the assembly instructions shows that it counts non-prime numbers between
# The values b and c (which are calculated in the skipped over instructions)

notPrimeCount = 0
for num in range(b, c+1, 17):
	if not isPrime(num):
		notPrimeCount += 1

print("NOT PRIME: {}".format(notPrimeCount))
