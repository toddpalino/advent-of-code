from functools import cache
from itertools import groupby, permutations

# These lookup tables provide options for each move so we can find the shortest set of moves

# This dict is the sequence of commands the numeric keypad robot needs to be given to press a button (to_key) based
# on where it starts (from_key). Use it via numeric_keypad[from_key][to_key]
numeric_keypad = {
	'A': {'A': ('A',), '0': ('<A',), '1': ('^<<A',), '2': ('^<A', '<^A',), '3': ('^A',), '4': ('^^<<A',),
	      '5': ('^^<A', '<^^A',), '6': ('^^A',), '7': ('^^^<<A',), '8': ('^^^<A', '<^^^A',), '9': ('^^^A',)},
	'0': {'A': ('>A',), '0': ('A',), '1': ('^<A',), '2': ('^A',), '3': ('^>A', '>^A',), '4': ('^^<A',),
	      '5': ('^^A',), '6': ('^^>A', '>^^A',), '7': ('^^^<A',), '8': ('^^^A',), '9': ('^^^>A', '>^^^A',)},
	'1': {'A': ('>>vA',), '0': ('>vA',), '1': ('A',), '2': ('>A',), '3': ('>>A',), '4': ('^A',),
	      '5': ('^>A', '>^A',), '6': ('^>>A', '>>^A',), '7': ('^^A',), '8': ('^^>A', '>^^A',), '9': ('^^>>A', '>>^^A',)},
	'2': {'A': ('v>A', '>vA',), '0': ('vA',), '1': ('<A',), '2': ('A',), '3': ('>A',), '4': ('^<A', '<^A',),
	      '5': ('^A',), '6': ('^>A', '>^A',), '7': ('^^<A', '<^^A',), '8': ('^^A',), '9': ('^^>A', '>^^A',)},
	'3': {'A': ('vA',), '0': ('v<A', '<vA',), '1': ('<<A',), '2': ('<A',), '3': ('A',), '4': ('^<<A', '<<^A',),
	      '5': ('^<A', '<^A',), '6': ('^A',), '7': ('<<^^A', '^^<<A',), '8': ('^^<A', '<^^A',), '9': ('^^A',)},
	'4': {'A': ('>>vvA',), '0': ('>vvA',), '1': ('vA',), '2': ('v>A', '>vA',), '3': ('v>>A', '>>vA',), '4': ('A',),
	      '5': ('>A',), '6': ('>>A',), '7': ('^A',), '8': ('^>A', '>^A',), '9': ('^>>A', '>>^A',)},
	'5': {'A': ('vv>A', '>vvA',), '0': ('vvA',), '1': ('v<A', '<vA',), '2': ('vA',), '3': ('v>A', '>vA',), '4': ('<A',),
	      '5': ('A',), '6': ('>A',), '7': ('^<A', '<^A',), '8': ('^A',), '9': ('^>A', '>^A',)},
	'6': {'A': ('vvA',), '0': ('vv<A', '<vvA',), '1': ('v<<A', '<<vA',), '2': ('v<A', '<vA',), '3': ('vA',), '4': ('<<A',),
	      '5': ('<A',), '6': ('A',), '7': ('^<<A', '<<^A',), '8': ('^<A', '<^A',), '9': ('^A',)},
	'7': {'A': ('>>vvvA',), '0': ('>vvvA',), '1': ('vvA',), '2': ('vv>A', '>vvA',), '3': ('vv>>A', '>>vvA',), '4': ('vA',),
	      '5': ('v>A', '>vA',), '6': ('v>>A', '>>vA',), '7': ('A',), '8': ('>A',), '9': ('>>A',)},
	'8': {'A': ('vvv>A', '>vvvA',), '0': ('vvvA',), '1': ('vv<A', '<vvA',), '2': ('vvA',), '3': ('vv>A', '>vvA',),
	      '4': ('v<A', '<vA',), '5': ('vA',), '6': ('v>A', '>vA',), '7': ('<A',), '8': ('A',), '9': ('>A',)},
	'9': {'A': ('vvvA',), '0': ('vvv<A', '<vvvA',), '1': ('vv<<A', '<<vvA',), '2': ('vv<A', '<vvA',), '3': ('vvA',),
	      '4': ('v<<A', '<<vA',), '5': ('v<A', '<vA',), '6': ('vA',), '7': ('<<A',), '8': ('<A',), '9': ('A',)},
}

# This dict is the sequence of commands a directional keypad robot needs to be given to press a button (to_key)
# based on where it is (from_key). Use it via directional_keypad[from_key][to_key]
# Since this robot always lands on the A key, we don't need to maintain a state (i.e. a from_key)
directional_keypad = {
	'A': {'A': ('A',), '^': ('<A',), 'v': ('<vA', 'v<A',), '<': ('v<<A',), '>': ('vA',)},
	'^': {'A': ('>A',), '^': ('A',), 'v': ('^A',), '<': ('v<A',), '>': ('v>A', '>vA',)},
	'v': {'A': ('>^A', '^>A',), '^': ('^A',), 'v': ('A',), '<': ('<A',), '>': ('>A',)},
	'<': {'A': ('>>^A',), '^': ('>^A',), 'v': ('>A',),  '<': ('A',), '>': ('>>A',)},
	'>': {'A': ('^A',), '^': ('<^A', '^<A',), 'v': ('<A',), '<': ('<<A',), '>': ('A',)}
}

def calculate_complexity(code, seq_len):
	return seq_len * int(code[:-1])

def expand_command(command):
	bot_state = 'A'
	commands = []
	for key in command:
		commands.append(directional_keypad[bot_state][key])
		bot_state = key
	return commands

def expand_numeric_command(command):
	bot_state = 'A'
	commands = []
	for key in command:
		commands.append(numeric_keypad[bot_state][key])
		bot_state = key
	return commands

# Any move&press command has up to 2 variants. We'll test both of them and
# take the better one
@cache
def get_optimized_command_length(variants, depth):
	if depth == 0:
		return len(variants[0])
	return min(sum(get_optimized_command_length(cmd, depth - 1) for cmd in expand_command(variant)) for variant in variants)
