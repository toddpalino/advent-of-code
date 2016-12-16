#!/usr/bin/python

import itertools
import sys
from copy import deepcopy

state_cache = {}
max_depth = 999999999

#num_pairs = 2
#num_pairs = 5
num_pairs = 7

class State:
    floors = 3

    def __init__(self, elevator=None, pairs=None, depth=max_depth):
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

    def is_finish(self):
        return self.key == finish_state.key

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

    def set_next_states(self):
        items_can_move = []
        for item_id, item in enumerate(self.pairs):
            for t in range(2):
                if item[t] == self.elevator:
                    items_can_move.append((item_id, t))
        item_sets = []
        for i, item in enumerate(items_can_move):
            item_sets.append([item])
            for j in range(i + 1, len(items_can_move)):
                # Only valid combos are both items are the same type (RTG or chip), or of the same quality (e.g. lithium)
                if (item[0] == items_can_move[j][0]) or (item[1] == items_can_move[j][1]):
                    item_sets.append([item, items_can_move[j]])

        floors = []
        if self.elevator > 0:
            floors.append(self.elevator - 1)
        if self.elevator < self.floors:
            floors.append(self.elevator + 1)

        possible = []
        for floor in floors:
            for items in item_sets:
                test_state = self.copy()
                test_state.elevator = floor
                for item in items:
                    test_state.pairs[item[0]][item[1]] = floor
                test_state.set_key()
                if not test_state.is_valid():
                    continue

                if test_state.key not in state_cache:
                    state_cache[test_state.key] = test_state
                self.next.append(state_cache[test_state.key])

    def copy(self):
        new_state = State(elevator=self.elevator, pairs=deepcopy(self.pairs))
        return new_state

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return str(self.key)


def prime_cache(num_pairs):
    test_state = State(0, [[0, 0] for i in range(num_pairs)])
    for coord in itertools.product(range(State.floors + 1), repeat=(num_pairs*2)+1):
        test_state.elevator = coord[0]
        for i in range(num_pairs*2):
            test_state.pairs[i / 2][i % 2] = coord[i+1]
        if test_state.is_valid():
            test_state.set_key()
            state_cache[test_state.key] = test_state.copy()

def bfs(start_state):
    state_stack = [start_state]

    while len(state_stack) > 0:
        state = state_stack.pop(0)
        state.set_next_states()
        for child in state.next:
            if child.depth < max_depth:
                continue
            child.depth = state.depth + 1
            if child.is_finish():
                return child.depth
            state_stack.append(child)
    return -1

#start_state = State(elevator=0, pairs=[[0, 1], [0, 2]])
#finish_state = State(elevator=3, pairs=[[3, 3], [3, 3]])

#start_state = State(elevator=0, pairs=[[1, 0], [0, 0], [1, 0], [0, 0], [0, 0]])
#finish_state = State(elevator=3, pairs=[[3, 3], [3, 3], [3, 3], [3, 3], [3, 3]])

start_state = State(elevator=0, pairs=[[1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
finish_state = State(elevator=3, pairs=[[3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]])

#prime_cache(num_pairs)
#print "CACHE: {0}".format(len(state_cache))
#start_state = state_cache[start_key]
#finish_state = state_cache[finish_key]
start_state.depth = 0

print "DISTANCE: {0}".format(bfs(start_state))

