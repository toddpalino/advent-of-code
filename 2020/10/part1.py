#!/usr/bin/python3

from collections import Counter

#with open("test.txt") as f:
#with open("test2.txt") as f:
with open("input.txt") as f:
	adapters = [int(line) for line in f]

adapters.sort()
device = adapters[-1] + 3

differences = Counter()
differences[adapters[0]] += 1
differences[3] += 1

for i in range(1, len(adapters)):
	differences[adapters[i] - adapters[i-1]] += 1

print(differences)
print(differences[1] * differences[3])
