#!/usr/bin/python3

test_races = [(7, 9), (15, 40), (30, 200)]
input_races = [(62, 644), (73, 1023), (75, 1240), (65, 1023)]
races = input_races

product_wins = 1
for race in races:
	first_win = None
	last_win = None

	# Find first winning hold time
	for i in range(1, race[0]):
		total_distance = (race[0] - i) * i
		if race[1] < total_distance:
			first_win = i
			break

	# Find last winning hold time
	for i in range(race[0] - 1, 1, -1):
		total_distance = (race[0] - i) * i
		if race[1] < total_distance:
			last_win = i
			break

	total_wins = (last_win - first_win) + 1
	product_wins *= total_wins

print(product_wins)
