#!/usr/bin/python

space_cache = {}
max_depth = 99999999
finish_x = 31
finish_y = 39

class Space:
    favorite_number = 1364

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_wall = self._is_wall()
        self.next = []
        self.depth = max_depth
        space_cache[(x, y)] = self

    def _is_wall(self):
        val = (self.x * self.x) + (3 * self.x) + (2 * self.x * self.y) + self.y + (self.y * self.y) + self.favorite_number

        ones = 0
        for bit in bin(val)[2:]:
            if bit == '1':
                ones += 1
        return ones % 2 == 1

    def set_next(self):
        test_coords = [(self.x, self.y-1), (self.x, self.y+1), (self.x-1, self.y), (self.x+1, self.y)]
        for coord in test_coords:
            if coord[0] < 0 or coord[1] < 0:
                continue
            next_space = space_cache[(coord[0], coord[1])] if (coord[0], coord[1]) in space_cache else Space(coord[0], coord[1])
            if next_space.is_wall:
                continue
            self.next.append(next_space)

def bfs(start_state):
    state_stack = [start_state]

    while len(state_stack) > 0:
        state = state_stack.pop(0)
        print "({0}, {1}) - {2}".format(state.x, state.y, "wall" if state.is_wall else "space")
        state.set_next()
        for child in state.next:
            if child.depth < max_depth:
                continue
            child.depth = state.depth + 1
            if child.x == finish_x and child.y == finish_y:
                return child.depth
            state_stack.append(child)
    return -1

def bfs_less_than(start_state, max_steps=50):
    state_stack = [start_state]

    while len(state_stack) > 0:
        state = state_stack.pop(0)
        print "({0}, {1}) - {2}".format(state.x, state.y, "wall" if state.is_wall else "space")
        state.set_next()
        for child in state.next:
            if child.depth < max_steps:
                continue
            child.depth = state.depth + 1
            state_stack.append(child)
    return -1

start_space = Space(1, 1)
start_space.depth = 0
print "DISTANCE: {0}".format(bfs(start_space))

bfs_less_than(start_space)
count = 0
for coord, space in space_cache.iteritems():
    if (not space.is_wall) and space.depth <= 50:
        count += 1
print "COUNT: {0}".format(count)
