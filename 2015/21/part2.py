#!/usr/bin/python3

import time
from itertools import product, combinations
from math import ceil

# Puzzle input
boss_hp = 100
boss_damage = 8
boss_armor = 2

player_hp = 100

weapons = [
	{'name': 'Dagger', 'cost': 8, 'damage': 4, 'armor': 0},
	{'name': 'Shortsword', 'cost': 10, 'damage': 5, 'armor': 0},
	{'name': 'Warhammer', 'cost': 25, 'damage': 6, 'armor': 0},
	{'name': 'Longsword', 'cost': 40, 'damage': 7, 'armor': 0},
	{'name': 'Greataxe', 'cost': 74, 'damage': 8, 'armor': 0}
]

armors = [
	{'name': 'Leather', 'cost': 13, 'damage': 0, 'armor': 1},
	{'name': 'Chainmail', 'cost': 31, 'damage': 0, 'armor': 2},
	{'name': 'Splintmail', 'cost': 53, 'damage': 0, 'armor': 3},
	{'name': 'Bandedmail', 'cost': 75, 'damage': 0, 'armor': 4},
	{'name': 'Platemail', 'cost': 102, 'damage': 0, 'armor': 5}
]

rings = [
	{'name': 'Damage +1', 'cost': 25, 'damage': 1, 'armor': 0},
	{'name': 'Damage +2', 'cost': 50, 'damage': 2, 'armor': 0},
	{'name': 'Damage +3', 'cost': 100, 'damage': 3, 'armor': 0},
	{'name': 'Defense +1', 'cost': 20, 'damage': 0, 'armor': 1},
	{'name': 'Defense +2', 'cost': 40, 'damage': 0, 'armor': 2},
	{'name': 'Defense +3', 'cost': 80, 'damage': 0, 'armor': 3}
]

start_time = time.time()

# Figure out the options for each item type
possible_weapons = list(range(len(weapons)))
possible_armors = [None] + list(range(len(armors)))
possible_rings = [(None, None)] + [(ring, None) for ring in range(len(rings))] + list(combinations(range(len(rings)), 2))

maximum_cost = 0
for weapon, armor, ring in product(possible_weapons, possible_armors, possible_rings):
	items = [weapons[weapon]]
	if armor is not None:
		items.append(armors[armor])
	for r in ring:
		if r is not None:
			items.append(rings[r])

	player_cost = sum(item['cost'] for item in items)
	player_damage = sum(item['damage'] for item in items)
	player_armor = sum(item['armor'] for item in items)

	boss_damage_per_turn = boss_damage - player_armor
	player_damage_per_turn = player_damage - boss_armor

	if boss_damage_per_turn <= 0:
		# Player automatically wins
		continue

	boss_needs = ceil(player_hp / boss_damage_per_turn)
	player_needs = ceil(boss_hp / player_damage_per_turn)

	if player_needs > boss_needs:
		# Player loses
		maximum_cost = max(maximum_cost, player_cost)

print("Maximum player cost to lose: %d" % (maximum_cost))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
