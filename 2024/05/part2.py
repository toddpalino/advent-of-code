#!/usr/bin/python3

from functools import cmp_to_key

#fn = "test.txt"
fn = "input.txt"

rules = {}
updates = []

with open(fn, 'r') as f:
	reading_rules = True
	for line in f:
		ln = line.strip()
		if reading_rules:
			if ln == '':
				reading_rules = False
				continue
			parts = ln.split('|')
			first = int(parts[0])
			second = int(parts[1])

			if first not in rules:
				rules[first] = {'before': [], 'after': []}
			if second not in rules:
				rules[second] = {'before': [], 'after': []}
			rules[first]['before'].append(second)
			rules[second]['after'].append(first)
		else:
			updates.append([int(num) for num in ln.split(',')])


# This should be a key function, but it's way easier to let the compiler do that for me
def rules_cmp(a, b):
	if a not in rules:
		return 0
	if b in rules[a]['before']:
		return -1
	if b in rules[a]['after']:
		return 1
	return 0


middle_sum = 0
for update in updates:
	new_update = sorted(update, key=cmp_to_key(rules_cmp))
	if update != new_update:
		middle_sum += new_update[len(new_update) // 2]

print("Middle sum: %d" % (middle_sum))
