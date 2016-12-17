#!/usr/bin/python

import md5

is_open = ['b', 'c', 'd', 'e', 'f']
salt = raw_input("Salt: ")

class Room:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p
        self.next = []

    def set_next(self):
        hash = md5.new(salt + self.p).hexdigest()
        for i in range(4):
            if hash[i] in is_open:
                if i == 0 and self.y > 0:
                    self.next.append(Room(self.x, self.y-1, self.p + 'U'))
                    continue
                if i == 1 and self.y < 3:
                    self.next.append(Room(self.x, self.y+1, self.p + 'D'))
                    continue
                if i == 2 and self.x > 0:
                    self.next.append(Room(self.x-1, self.y, self.p + 'L'))
                    continue
                if i == 3 and self.x < 3:
                    self.next.append(Room(self.x+1, self.y, self.p + 'R'))
                    continue

def bfs(start_state):
    state_stack = [start_state]

    while len(state_stack) > 0:
        state = state_stack.pop(0)
        state.set_next()
        for child in state.next:
            if child.x == 3 and child.y == 3:
                print "({0}, {1}) - {2} - {3}".format(child.x, child.y, len(child.p), child.p)
            else:
                state_stack.append(child)

start = Room(0, 0, '')
bfs(start)
