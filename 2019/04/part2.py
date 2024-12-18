#!/usr/bin/env python

import time

def password_valid(password):
	digits = [int(x) for x in list(str(password))]
	len_password = len(digits)

	found_double = False
	for i in range(1, len(digits)):
		if digits[i] < digits[i-1]:
			return False
		if digits[i] == digits[i-1]:
			if (i >= 2 and digits[i-2] == digits[i]) or (i < (len_password - 1) and digits[i+1] == digits[i]):
				pass
			else:
				found_double = True
	return found_double

password_range = (235741, 706948)

start_time = time.time()

tests = [
	{'password': 112233, 'result': True},
	{'password': 123444, 'result': False},
	{'password': 111122, 'result': True}
]

for i, test in enumerate(tests):
	result = password_valid(test['password'])
	if result == test['result']:
		print(f"Test {i} passed")
	else:
		print(f"Test {i} failed (expected {test['result']}, got {result})")

valid_passwords = 0
for password in range(password_range[0], password_range[1] + 1):
	if password_valid(password):
		valid_passwords += 1

print(f"{valid_passwords} valid passwords")

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
