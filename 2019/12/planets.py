from itertools import combinations

# Test inputs
tests = [
	{
		'planets': [
			{'position': [-1, 0, 2], 'velocity': [0, 0, 0]},
			{'position': [2, -10, -7], 'velocity': [0, 0, 0]},
			{'position': [4, -8, 8], 'velocity': [0, 0, 0]},
			{'position': [3, 5, -1], 'velocity': [0, 0, 0]},
		],
		'expects': [
			{'position': [2, 1, -3], 'velocity': [-3, -2, 1]},
			{'position': [1, -8, 0], 'velocity': [-1, 1, 3]},
			{'position': [3, -6, 1], 'velocity': [3, 2, -3]},
			{'position': [2, 0, 4], 'velocity': [1, -1, -1]},
		],
		'energy': 179,
		'iterations': 10,
		'repeat': 2772,
},
	{
		'planets': [
			{'position': [-8, -10, 0], 'velocity': [0, 0, 0]},
			{'position': [5, 5, 10], 'velocity': [0, 0, 0]},
			{'position': [2, -7, 3], 'velocity': [0, 0, 0]},
			{'position': [9, -8, -3], 'velocity': [0, 0, 0]},
		],
		'expects': [
			{'position': [8, -12, -9], 'velocity': [-7, 3, 0]},
		    {'position': [13, 16, -3], 'velocity': [3, -11, -5]},
		    {'position': [-29, -11, -1], 'velocity': [-3, 7, 4]},
		    {'position': [16, -13, 23], 'velocity': [7, 1, 1]},
		],
		'energy': 1940,
		'iterations': 100,
		'repeat': 4686774924,
	}
]

# Puzzle input
planets = [
	{'position': [0, 6, 1], 'velocity': [0, 0, 0]},
	{'position': [4, 4, 19], 'velocity': [0, 0, 0]},
	{'position': [-11, 1, 8], 'velocity': [0, 0, 0]},
	{'position': [2, 19, 15], 'velocity': [0, 0, 0]},
]

def simulate(planets, iterations=1):
	print(planets[0]['position'][0], planets[0]['velocity'][0])
	for _ in range(iterations):
		# First apply gravity
		for p1, p2 in combinations(planets, 2):
			for axis in range(3):
				if p1['position'][axis] < p2['position'][axis]:
					p1['velocity'][axis] += 1
					p2['velocity'][axis] -= 1
				elif p1['position'][axis] > p2['position'][axis]:
					p1['velocity'][axis] -= 1
					p2['velocity'][axis] += 1

		# Now apply velocity
		for p1 in planets:
			for axis in range(3):
				p1['position'][axis] += p1['velocity'][axis]
		print(planets[0]['position'][0], planets[0]['velocity'][0])

def calculate_energy(planets):
	sum_energy = 0
	for p in planets:
		pe = sum(abs(n) for n in p['position'])
		ke = sum(abs(n) for n in p['velocity'])
		sum_energy += pe * ke
	return sum_energy
