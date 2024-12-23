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

free_space = 70000000 - calc_size(root)
print("Starting free space: %d" % (free_space))

dir_to_delete = root['.size']
S = [root]
while S:
	pwd = S.pop()
	for entry, val in pwd.items():
		if entry == '..':
			continue
		if entry == '.size':
			free_space_if_deleted = free_space + val
			if free_space_if_deleted < 30000000:
				continue
			if free_space_if_deleted < (free_space + dir_to_delete):
				print("Found better candidate: %d" % (val))
				dir_to_delete = val
		if type(val) is dict:
			S.append(val)

print(dir_to_delete)
