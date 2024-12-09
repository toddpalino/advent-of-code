#!/usr/bin/python3

class Spell:
	mana_cost = 0

	def __init__(self, game, is_copy=False):
		self.game = game
		if not is_copy:
			game.player_mana -= self.__class__.mana_cost
			game.mana_spent += self.__class__.mana_cost
			self.spell_action()

	def spell_action(self):
		pass


class MagicMissile(Spell):
	mana_cost = 53

	def spell_action(self):
		self.game.boss_hp -= 4


class Drain(Spell):
	mana_cost = 73

	def spell_action(self):
		self.game.boss_hp -= 2
		self.game.player_hp += 2


class Effect(Spell):
	default_turns = 6

	def __init__(self, game, is_copy=False):
		super().__init__(game, is_copy=is_copy)
		self.turns = self.__class__.default_turns

	def copy(self, new_game):
		new_effect = self.__class__(new_game, is_copy=True)
		new_effect.turns = self.turns
		return new_effect

	def is_expiring(self):
		return self.turns == 1

	def do(self):
		self.turns -= 1
		if self.turns == 0:
			self.game.effects.remove(self)


class Shield(Effect):
	mana_cost = 113

	def spell_action(self):
		self.game.player_armor += 7

	def do(self):
		super().do()
		if self.turns == 0:
			self.game.player_armor -= 7


class Poison(Effect):
	mana_cost = 173

	def do(self):
		super().do()
		self.game.boss_hp -= 3


class Recharge(Effect):
	mana_cost = 229
	default_turns = 5

	def do(self):
		super().do()
		self.game.player_mana += 101


class Game:
	def __init__(self, boss_hp, boss_damage, player_hp, player_mana, hard=False):
		self.boss_hp = boss_hp
		self.boss_damage = boss_damage
		self.player_hp = player_hp
		self.player_mana = player_mana
		self.player_armor = 0
		self.effects = []
		self.mana_spent = 0
		self.hard = hard
		self.turns = 0

	def copy(self):
		new_game = Game(self.boss_hp, self.boss_damage, self.player_hp, self.player_mana, hard=self.hard)
		new_game.player_armor = self.player_armor
		new_game.mana_spent = self.mana_spent
		new_game.turns = self.turns
		for effect in self.effects:
			new_game.effects.append(effect.copy(new_game))
		return new_game

	def can_cast(self, spell):
		if spell.mana_cost > self.player_mana:
			return False
		if issubclass(spell, Effect):
			for effect in self.effects:
				if effect.__class__ == spell and (not effect.is_expiring()):
					return False
		return True

	def turn(self, spell):
		self.turns += 1
		if self.hard:
			self.player_hp -= 1
			if self.is_over():
				return

		# Player's turn first
		# Execute effects
		for effect in self.effects:
			effect.do()

		if self.is_over():
			return

		# Cast player's spell
		cast_spell = spell(self)
		if issubclass(spell, Effect):
			self.effects.append(cast_spell)

		if self.is_over():
			return

		# Boss's turn next
		# Execute effects
		for effect in self.effects:
			effect.do()

		if self.is_over():
			return

		# Boss attacks
		self.player_hp -= max(1, self.boss_damage - self.player_armor)

	def is_over(self):
		return self.player_hp <= 0 or self.boss_hp <= 0

	def player_won(self):
		return self.is_over() and self.player_hp > 0

	def __repr__(self):
		return f"Game(boss_hp={self.boss_hp} player_hp={self.player_hp} player_mana={self.player_mana})"



spells = [MagicMissile, Drain, Shield, Poison, Recharge]
