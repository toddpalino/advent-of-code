#!/usr/bin/python3

passports = []

with open("input.txt") as f:
#with open("test2.txt") as f:
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
	if (len(passport) <= 6) or (len(passport) == 7 and 'cid' in passport):
		# Missing fields other than cid - automatic invalid
		continue

	try:
		byr = int(passport['byr'])
		if len(passport['byr']) != 4 or not (1920 <= byr <= 2002):
			continue

		iyr = int(passport['iyr'])
		if len(passport['iyr']) != 4 or not (2010 <= iyr <= 2020):
			continue

		eyr = int(passport['eyr'])
		if len(passport['eyr']) != 4 or not (2020 <= eyr <= 2030):
			continue

		hgt = int(passport['hgt'][0:-2])
		if not (((passport['hgt'][-2:] == 'in') and (59 <= hgt <= 76)) or ((passport['hgt'][-2:] == 'cm') and (150 <= hgt <= 193))):
			continue

		if passport['hcl'][0] != '#':
			continue
		int("0x" + passport['hcl'][1:], 16)

		if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
			continue

		if len(passport['pid']) != 9:
			continue
		int(passport['pid'])

		valid += 1
	except ValueError:
		# Failed validation
		pass

print(valid)
