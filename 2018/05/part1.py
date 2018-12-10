#!/usr/bin/env python3

def reduce(chain):
	while True:
		mutations = 0

		for i in range(len(chain)):
			if chain[i] is None:
				continue
			next = i + 1
			while next < len(chain) and chain[next] is None:
				next += 1
			if next >= len(chain):
				break

			while abs(ord(chain[i]) - ord(chain[next])) == 32:
				chain[i] = None
				chain[next] = None
				mutations += 1

				while i >= 0 and chain[i] is None:
					i -= 1
				if i < 0:
					break
				while next < len(chain) and chain[next] is None:
					next += 1
				if next >= len(chain):
					break

		chain = [item for item in chain if item is not None]
		if mutations == 0:
			return chain


with open('input', 'r') as f:
	polymer = list(f.read().strip())

for c in range(ord('A'), ord('Z') + 1):
	test_polymer = reduce([item for item in polymer if ord(item) != c and ord(item) != c+32])
	print("{}: {}".format(chr(c), len(test_polymer)))

polymer = reduce(polymer)
print("None: {}".format(len(polymer)))
