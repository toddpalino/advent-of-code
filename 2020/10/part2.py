#!/usr/bin/python3

#with open("test.txt") as f:
#with open("test2.txt") as f:
with open("input.txt") as f:
	adapters = [int(line) for line in f]

adapters.sort()
device = adapters[-1] + 3

differences = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]
differences.insert(0, adapters[0])
differences.append(3)

i = 0
count = 0
combinations = 1
for i in range(len(differences)):
	if differences[i] == 1:
		count += 1
	elif count > 0:
		combinations *= (2 ** (count - 1)) - (1 if count == 4 else 0)
		count = 0

if count > 0:
	combinations *= (2 ** (count - 1)) - (1 if count == 4 else 0)

print(differences)
print(combinations)
