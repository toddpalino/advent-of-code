#!/usr/bin/python3


def calc_size(dir_dict):
	total = 0
	for entry, val in dir_dict.items():
		if entry[0] == '.':
			continue
		if type(val) is int:
			total += val
		else:
			total += calc_size(val)

	dir_dict['.size'] = total
	return total


root = {
	'..': None
}
pwd = None

with open('input.txt') as f:
	for line in f:
		cleaned = line.strip()
		if cleaned.startswith('$ cd '):
			to_dir = cleaned[5:]
			if to_dir == '/':
				pwd = root
			else:
				pwd = pwd[to_dir]
		elif cleaned == '$ ls':
			pass
		elif cleaned.startswith('dir '):
			pwd[cleaned[4:]] = {
				'..': pwd
			}
		else:
			parts = cleaned.split(' ')
			pwd[parts[1]] = int(parts[0])

calc_size(root)

total_small = 0
S = [root]
while S:
	pwd = S.pop()
	for entry, val in pwd.items():
		if entry == '..':
			continue
		if entry == '.size' and val <= 100000:
			total_small += val
		if type(val) is dict:
			S.append(val)

print(total_small)
