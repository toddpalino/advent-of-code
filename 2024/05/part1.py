#!/usr/bin/python3

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

middle_sum = 0
for update in updates:
	ordered = True
	for i, num in enumerate(update):
		if num not in rules:
			continue
		for later_num in rules[num]['before']:
			try:
				if update.index(later_num) < i:
					ordered = False
					break
			except ValueError:
				pass
		for earlier_num in rules[num]['after']:
			try:
				if update.index(earlier_num) > i:
					ordered = False
					break
			except ValueError:
				pass

	if ordered:
		middle_sum += update[len(update) // 2]

print("Middle sum: %d" % (middle_sum))
