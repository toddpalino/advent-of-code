#!/usr/bin/python3

total_power = 0

with open('input.txt') as f:
	for line in f:
		cleaned = line.strip()
		p1 = cleaned.split(': ')

		id_parts = p1[0].split(' ')
		game_id = int(id_parts[1])

		max_red = 0
		max_blue = 0
		max_green = 0

		shows = p1[1].split('; ')
		for show in shows:
			show_parts = show.split(', ')
			for cubes in show_parts:
				p2 = cubes.split(' ')
				color = p2[1]
				count = int(p2[0])

				if color == 'blue':
					max_blue = max(max_blue, count)
				if color == 'red':
					max_red = max(max_red, count)
				if color == 'green':
					max_green = max(max_green, count)

		power = max_red * max_blue * max_green
		total_power += power
		print("id=%d r=%d b=%d g=%d p=%d" % (game_id, max_red, max_blue, max_green, power))

print("Total Power: %d" % (total_power))
