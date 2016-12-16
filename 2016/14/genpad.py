#!/usr/bin/python

import md5
import re

class PadGenerator:
    salt = "jlmsuwbz"

    def __init__(self, stretch=0):
        self.used_iteration = 0
        self.ptr_lookahead = 0
        self.stretch_factor = stretch
        self._next_salt_int = 1
        self._hashes = []

    def get_next(self):
        if len(self._hashes) == 0:
            self._generate_hashes()
        self.ptr_lookahead = 0
        self.used_iteration += 1
        return self._hashes.pop(0)

    def peek_next(self):
        if (self.ptr_lookahead + 1) > len(self._hashes):
            self._generate_hashes()
        hash = self._hashes[self.ptr_lookahead]
        self.ptr_lookahead += 1
        return hash

    def _generate_hashes(self):
        for i in range(self._next_salt_int, self._next_salt_int + 1000):
            newhash = md5.new(self.salt + str(i)).hexdigest()
            for j in range(self.stretch_factor):
                newhash = md5.new(newhash).hexdigest()
            self._hashes.append(newhash)
        self._next_salt_int += 1000

def find_first_triple(hashstr):
    for i in range(len(hashstr) - 2):
        if hashstr[i] == hashstr[i + 1] and hashstr[i] == hashstr[i + 2]:
            return hashstr[i]
    return None

def find_pent(hashstr, match):
    for i in range(len(hashstr) - 4):
        if hashstr[i] != match:
            continue
        if hashstr[i] == hashstr[i + 1] and hashstr[i] == hashstr[i + 2] and hashstr[i] == hashstr[i + 3] and hashstr[i] == hashstr[i + 4]:
            return hashstr[i]
    return None

def gen_pads(g, num):
    pads = []
    iteration = 0

    while len(pads) < num:
        proposed = g.get_next()
        found_char = find_first_triple(proposed)
        if found_char is None:
            continue

        for i in range(1000):
            peek = g.peek_next()
            if find_pent(peek, found_char) is not None:
                pads.append(proposed)
                print "{0} ({1}) {2} ({3})".format(proposed, peek, g.used_iteration, g.used_iteration + i)
                break

g = PadGenerator(2016)
gen_pads(g, 64)

#for i in range(100):
#    print g.get_next()
