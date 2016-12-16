#!/usr/bin/python

# Outputs a list of all valid states

import itertools

state_cache = {}
#num_pairs = 2
num_pairs = 5

class State:
    floors = 3

    def __init__(self, elevator=None, pairs=None, depth=999999999):
        self.elevator = 0 if elevator is None else elevator
        self.pairs = [
            [0, 1],
            [0, 2]
        ] if pairs is None else pairs
        self.next = []
        self.parents = []
        self.depth = depth
        self.set_key()

    def set_key(self):
        self.key = (self.elevator, tuple([val for sublist in self.pairs for val in sublist]))

    def is_valid(self):
        for floor in range(self.floors + 1):
            chips = [item_id for item_id, item in enumerate(self.pairs) if item[0] == floor]
            rtgs = [item_id for item_id, item in enumerate(self.pairs) if item[1] == floor]
            if len(rtgs) == 0 and len(chips) == 0 and self.elevator == floor:
                return False
            if len(rtgs) == 0:
                continue
            if len(chips) > 0:
                for chip in chips:
                    if chip not in rtgs:
                        return False
        return True

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return str(self.key)


test_state = State(0, [[0, 0] for i in range(num_pairs)])
for coord in itertools.product(range(State.floors + 1), repeat=(num_pairs*2)+1):
    test_state.elevator = coord[0]
    for i in range(num_pairs*2):
        test_state.pairs[i / 2][i % 2] = coord[i+1]
    if test_state.is_valid():
        test_state.set_key()
        state_cache[test_key] = test_state.copy()


