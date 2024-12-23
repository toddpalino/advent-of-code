#!/usr/bin/python3

passports = []

with open("input.txt") as f:
#with open("test.txt") as f:
	passport = {}
	for line in f:
		ln = line.strip()
		if len(ln) == 0:
			passports.append(passport)
			passport = {}
			continue

		fields = ln.split()
		for field in fields:
			parts = field.split(':')
			passport[parts[0]] = parts[1]

	# Append last passport
	passports.append(passport)

valid = 0
for passport in passports:
	if (len(passport) == 8) or (len(passport) == 7 and 'cid' not in passport):
		valid += 1

print(valid)
