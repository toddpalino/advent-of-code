#!/usr/bin/python

import operator

max_depth = 9999999999
state_cache = {}

replacements = {}
with open('replacements') as f:
    for line in f:
        src, sep, target = line.strip().partition(' => ')
        replacements[target] = src
print len(replacements)
replacements = [(k, replacements[k]) for k in sorted(replacements, key=len, reverse=True)]
print replacements

class State:
    def __init__(self, molecule):
        self.molecule = molecule
        self.next = []
        self.depth = max_depth
        state_cache[self.molecule] = self

    def set_next(self):
        for src, target in replacements:
            segments = self.molecule.split(src)
            for i in range(1, len(segments)):
                newstr = src.join(segments[0:i]) + target + src.join(segments[i:])
                newstate = state_cache[newstr] if newstr in state_cache else State(newstr)
                if newstate not in self.next:
                    self.next.append(newstate)

    def is_finish(self):
        self.molecule == "e"

def bfs(start_state):
    state_stack = [start_state]
    visit_count = 0

    while len(state_stack) > 0:
        visit_count += 1
        if visit_count % 10000 == 0:
            print "{0} - {1} - {2}".format(visit_count, state.depth, state.molecule)
        state = state_stack.pop(0)
        state.set_next()
        for child in state.next:
            if child.depth < max_depth:
                continue
            child.depth = state.depth + 1
            if child.is_finish():
                return child.depth
            state_stack.append(child)
    return -1

start_state = State("CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr")
start_state.depth = 0

print "STEPS: {0}".format(bfs(start_state))
