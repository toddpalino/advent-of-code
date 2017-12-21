#!/usr/bin/python

map = []
with open("input", "r") as f:
	for line in f:
		map.append(list(line))

# Test input
test_map = [
	[' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ','|',' ',' ','+','-','-','+',' ',' ',' ',' '],
	[' ',' ',' ',' ',' ','A',' ',' ','|',' ',' ','C',' ',' ',' ',' '],
	[' ','F','-','-','-','|','-','-','-','-','E','|','-','-','+',' '],
	[' ',' ',' ',' ',' ','|',' ',' ','|',' ',' ','|',' ',' ','D',' '],
	[' ',' ',' ',' ',' ','+','B','-','+',' ',' ','+','-','-','+',' ']
]
#map = test_map

# Find the start in the first row
y = 0
x = map[y].index('|')

trail = []
move = (0, 1)
steps = 0
while True:
	check_char = map[y][x]
	if check_char == ' ':
		break

	if check_char not in ('|', '-', '+'):
		trail.append(check_char)

	# Change direction
	if check_char == '+':
		if move[0] == 0:
			# Change direction to east or west
			if ((x - 1) >= 0) and (map[y][x-1] != ' '):
				move = (-1, 0)
			else:
				move = (1, 0)
		else:
			# Change direction to north or south
			if ((y - 1) >= 0) and (map[y-1][x] != ' '):
				move = (0, -1)
			else:
				move = (0, 1)

	# Move
	x += move[0]
	y += move[1]
	steps += 1

print("TRAIL: {0}".format(''.join(trail)))
print("STEPS: {0}".format(steps))
