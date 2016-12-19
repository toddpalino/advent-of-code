#!/usr/bin/python

from collections import deque

elves = int(raw_input("Elves: "))

elf_list = []
for i in range(elves):
    elf_list.append({'id': i+1, 'presents': 1})
elf = deque(elf_list)

while len(elf) > 1:
    turn = elf.popleft()
    target = elf.popleft()
    turn['presents'] += target['presents']
    elf.append(turn)

print "ELF {0}: {1} presents".format(elf[0]['id'], elf[0]['presents'])
