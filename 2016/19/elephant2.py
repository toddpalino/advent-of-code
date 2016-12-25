#!/usr/bin/python

class Elf:
    def __init__(self, id):
        self.id = id
        self.presents = 1
        self.left = None
        self.right = None

elves = int(raw_input("Elves: "))
remaining = elves

# Build the linked list in a single loop
head = Elf(1)
last = head
for i in range(1, elves):
    elf = Elf(i + 1)
    elf.right = last
    last.left = elf
    last = elf
last.left = head
head.right = last

# Set the first turn taker and their target
turn = head
target = turn
for i in range(remaining / 2):
    target = target.left

while remaining > 1:
    turn.presents += target.presents

    # The target moves one spot if the number of elves is even, two if odd (before removal)
    next_target = target.left
    if remaining % 2 == 1:
        next_target = next_target.left

    # Remove the target from the circle
    target.left.right, target.right.left = target.right, target.left
    target = next_target

    remaining -= 1
    turn = turn.left
    if target == turn:
        break

print "ELF {0}: {1}".format(turn.id, turn.presents)
