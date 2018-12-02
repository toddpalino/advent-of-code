#!/usr/bin/python

def has_dupes(words):
	seen = {}
	for word in words:
		if word in seen:
			return True
		seen[word] = 1
	return False


def letter_count(word):
	letters = {}
	for letter in word:
		letters[letter] = letters.get(letter, 0) + 1
	return letters


def letters_match(src, tgt):
	for letter in src:
		if src[letter] != tgt.get(letter, 0):
			return False
	return True


def has_anagrams(words):
	for src in range(len(words)):
		src_letters = letter_count(words[src])
		for tgt in range(src+1, len(words)):
			if len(words[tgt]) != len(words[src]):
				continue
			tgt_letters = letter_count(words[tgt])
			if letters_match(src_letters, tgt_letters):
				return True


policy1 = 0
policy2 = 0
with open("input", "r") as f:
	for line in f:
		words = line.strip().split()
		if has_dupes(words):
			continue
		policy1 += 1
		if has_anagrams(words):
			continue
		policy2 += 1

print("Policy 1 valid: {0}".format(policy1))
print("Policy 2 valid: {0}".format(policy2))
