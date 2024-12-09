#!/usr/bin/python3

import time
from collections import deque
from game import Game, spells

boss_hp = 55
boss_damage = 8

player_hp = 50
player_mana = 500


start_time = time.time()

minimum_mana_spent = 999999
queue = deque([Game(boss_hp, boss_damage, player_hp, player_mana)])
while queue:
	game = queue.popleft()

	# Generate list of spells we can cast, and a new game object for each
	castable = [spell for spell in spells if game.can_cast(spell)]
	new_games = [game.copy() for _ in range(len(castable) - 1)]
	new_games.append(game)

	# Execute the next turn for each game
	for i in range(len(castable)):
		new_game = new_games[i]
		new_game.turn(castable[i])

		# Add it to the queue, checking to see if it's over first
		if new_game.is_over():
			if new_game.player_won():
				if minimum_mana_spent is None:
					minimum_mana_spent = new_game.mana_spent
				else:
					minimum_mana_spent = min(minimum_mana_spent, new_game.mana_spent)
		else:
			if new_game.mana_spent < minimum_mana_spent:
				queue.append(new_game)

print("Minimum mana spent to win: %d" % (minimum_mana_spent))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
