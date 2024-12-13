#!/usr/bin/python3

import time

def cost(a, b, prize, limit=True):
	ax, ay = a
	bx, by = b
	px, py = prize

	# Yes, I used Wolfram Alpha to solve the system of equations
	press_a = ((bx * py) - (by * px)) / ((bx * ay) - (ax * by))
	press_b = ((ax * py) - (ay * px)) / ((ax * by) - (bx * ay))

	# Make sure we have whole numbers
	if int(press_a) == press_a and int(press_b) == press_b:
		if not limit or (press_a < 100 and press_b < 100):
			return press_b + (3 * press_a)
	return 0


#fn = "test.txt"
fn = "input.txt"

# Prize location offset for part 2
offset = 10000000000000

start_time = time.time()

machines = []
with open(fn, 'r') as f:
	a = None
	b = None
	prize = None

	for line in f:
		if len(line) < 7:
			machines.append((a, b, prize))
		elif line[7] in ('A', 'B'):
			parts = line[10:-1].split(', ')
			move = (int(parts[0][2:]), int(parts[1][2:]))
			if line[7] == 'A':
				a = move
			else:
				b = move
		elif line[0] == 'P':
			parts = line[7:-1].split(', ')
			prize = [int(parts[0][2:]), int(parts[1][2:])]

	# Make sure to add the last one
	machines.append((a, b, prize))

total_cost = sum(cost(a, b, prize) for a, b, prize in machines)
print("Part 1 - Tokens spent: %d" % (total_cost))

# Part 2 - increase the prize locations by the offset amount
for i in range(len(machines)):
	machines[i][2][0] += offset
	machines[i][2][1] += offset

total_cost = sum(cost(a, b, prize, limit=False) for a, b, prize in machines)
print("Part 2 - Tokens spent: %d" % (total_cost))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
