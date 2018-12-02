#!/usr/bin/python

class Group(object):
	def __init__(self, stream, ptr, parent_score):
		end_token = '}'
		self.is_garbage = False
		self.groups = []
		self.starts_at = ptr
		self.ends_at = -1
		self.score = parent_score + 1

		if stream[ptr] == '<':
			self.is_garbage = True
			self.score = 0
			end_token = '>'

		self._content = ''
		while ptr < len(stream):
			ptr += 1
			if stream[ptr] == end_token:
				self.ends_at = ptr
				self._content = stream[self.starts_at+1:ptr]
				return
			if stream[ptr] == '!':
				ptr += 1
				continue
			if not self.is_garbage and ((stream[ptr] == '{') or (stream[ptr] == '<')):
				new_group = Group(stream, ptr, self.score)
				self.groups.append(new_group)
				ptr = new_group.ends_at
				if stream[ptr] == ',':
					ptr += 1

	def total_score(self):
		total = self.score
		for group in self.groups:
			total += group.total_score()
		return total

	def garbage_characters(self):
		total = 0
		if self.is_garbage:
			ptr = 0
			while ptr < len(self._content):
				if self._content[ptr] == '!':
					ptr += 1
				else:
					total += 1
				ptr += 1
		else:
			for group in self.groups:
				total += group.garbage_characters()
		return total


streams = []
with open("input", "r") as f:
	streams.append(f.read().strip())

# Scoring test input
#streams = [
#	'{}',
#	'{{{}}}',
#	'{{},{}}',
#	'{{{},{},{{}}}}',
#	'{<a>,<a>,<a>,<a>}',
#	'{{<ab>},{<ab>},{<ab>},{<ab>}}',
#	'{{<!!>},{<!!>},{<!!>},{<!!>}}',
#	'{{<a!>},{<a!>},{<a!>},{<ab>}}'
#]

# Garbage Count test input
#streams = [
#	'<>',
#	'<random characters>',
#	'<<<<>',
#	'<{!>}>',
#	'<!!>',
#	'<!!!>>',
#	'<{o"i!a,<{i<a>'
#]

for stream in streams:
	print stream
	group = Group(stream, 0, 0)
	print("SCORE: {0}".format(group.total_score()))
	print("GARBAGE: {0}".format(group.garbage_characters()))
