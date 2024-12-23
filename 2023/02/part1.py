#!/usr/bin/python3

# Game 1: 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red

count_red = 12
count_green = 13
count_blue = 14
possible_ids = 0
impossible_ids = 0

with open('input.txt') as f:
	for line in f:
		cleaned = line.strip()
		p1 = cleaned.split(': ')

		id_parts = p1[0].split(' ')
		game_id = int(id_parts[1])

		shows = p1[1].split('; ')
		try:
			for show in shows:
				show_parts = show.split(', ')
				for cubes in show_parts:
					p2 = cubes.split(' ')
					if (p2[1] == 'blue' and int(p2[0]) > count_blue) or (p2[1] == 'green' and int(p2[0]) > count_green) or (p2[1] == 'red' and int(p2[0]) > count_red):
						raise ValueError
			possible_ids += game_id
		except ValueError:
			impossible_ids += game_id

print("Possible IDs: %d" % (possible_ids))
print("Impossible IDs: %d" % (impossible_ids))
