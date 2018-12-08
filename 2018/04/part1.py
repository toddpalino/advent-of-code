#!/usr/bin/env python3

guards = {}
guard = None
minute = 0
awake = True

with open('input', 'r') as f:
	for line in f:
		words = line.split(' ')
		if words[2] == 'Guard':
			if guard is not None:
				if not awake:
					for m in range(minute, 60):
						guards[guard][m] = guards[guard][m] + 1
			minute = 0
			guard = int(words[3][1:])
			awake = True
			if guard not in guards:
				guards[guard] = [0] * 60
		elif words[2] == 'falls':
			minute = int(words[1][3:5])
			awake = False
		else:
			end_minute = int(words[1][3:5])
			for m in range(minute, end_minute):
				guards[guard][m] = guards[guard][m] + 1
			awake = True
			minute = end_minute

# Our last guard wakes up as a last action, so we don't need a cleanup here

sleepiest_guard = None
for guard in guards:
	if sleepiest_guard is None:
		sleepiest_guard = guard
	else:
		if sum(guards[guard]) > sum(guards[sleepiest_guard]):
			sleepiest_guard = guard

sleepiest_minute = 0
for i, minutes_asleep in enumerate(guards[sleepiest_guard]):
	if minutes_asleep > guards[sleepiest_guard][sleepiest_minute]:
		sleepiest_minute = i

print("Strategy 1")
print("Sleepiest Guard: {}".format(sleepiest_guard))
print("Sleepiest Minute: {}".format(sleepiest_minute))

sleepiest_guard = None
sleepiest_minute = 0
for guard in guards:
	if sleepiest_guard is None:
		sleepiest_guard = guard

	for minute, minutes_asleep in enumerate(guards[guard]):
		if minutes_asleep > guards[sleepiest_guard][sleepiest_minute]:
			sleepiest_guard = guard
			sleepiest_minute = minute

print("\nStrategy 2")
print("Sleepiest Guard: {}".format(sleepiest_guard))
print("Sleepiest Minute: {}".format(sleepiest_minute))
