#!/usr/bin/python3

from collections import deque
import time

test_time = 71530
test_distance = 940200
input_time = 62737565
input_distance = 644102312401023

race_time = input_time
race_distance = input_distance

t0 = time.process_time()

# Find two winning points in the middle. It doesn't really matter where they are
winners = []
queue = deque([(0, race_time)])
while queue:
	r = queue.pop()
	x = r[0]
	y = r[1]
	midpoint = x + ((y - x) // 2)
	if ((race_time - midpoint) * midpoint) > race_distance:
		winners.append(midpoint)
	if len(winners) == 2:
		break
	queue.append((x, midpoint))
	queue.append((midpoint + 1, x))

# These starting ranges are guaranteed to have exactly one endpoint be winning and one be losing
winners.sort()
queue = deque([(0, winners[0]), (winners[1], race_time)])
total_wins = (winners[1] - winners[0]) - 1

while queue:
	try_times = queue.pop()
	x = try_times[0]
	y = try_times[1]
	win_0 = ((race_time - x) * x) > race_distance
	win_1 = ((race_time - y) * y) > race_distance

	if win_0 and win_1:
		# If both ends of the range win, the entire range wins. Count it and discard
		total_wins += (y - x) + 1
	elif win_0 or win_1:
		# If only one end of the range wins, keep testing
		# This implicitly discards ranges where both ends lose, as the entire range loses
		middle = x + ((y - x) // 2)
		queue.append((x, middle))
		queue.append((middle + 1, y))

t1 = time.process_time()

print(total_wins)
print("Time: %f" % (t1 - t0))
