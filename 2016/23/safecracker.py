#!/usr/bin/python

import sys

instructions = []
with open('instructions') as f:
    for line in f:
        instructions.append(line.strip().split(' '))

keypad = int(raw_input("Keypad: "))

register = {
    'a': keypad,
    'b': 0,
    'c': 0,
    'd': 0
}

counter = 0
ptr = 0
while ptr < len(instructions):
    if counter % 1000000 == 0:
        print "{0}: {1}".format(counter, register)
    counter += 1

    cmd = instructions[ptr]
    try:
        if cmd[0] == 'cpy':
            val = register[cmd[1]] if cmd[1] in register else int(cmd[1])
            register[cmd[2]] = val
        elif cmd[0] == 'inc':
            register[cmd[1]] = register[cmd[1]] + 1
        elif cmd[0] == 'dec':
            register[cmd[1]] = register[cmd[1]] - 1
        elif cmd[0] == 'jnz':
            tst = register[cmd[1]] if cmd[1] in register else int(cmd[1])
            if tst != 0:
                ptr += register[cmd[2]] if cmd[2] in register else int(cmd[2])
                continue
        elif cmd[0] == 'tgl':
            val = register[cmd[1]] if cmd[1] in register else int(cmd[1])
            change_ptr = ptr + val
            if change_ptr < 0 or change_ptr >= len(instructions):
                ptr += 1
                continue

            if len(instructions[change_ptr]) == 2:
                instructions[change_ptr][0] = 'dec' if instructions[change_ptr][0] == 'inc' else 'inc'
            else:
                instructions[change_ptr][0] = 'cpy' if instructions[change_ptr][0] == 'jnz' else 'jnz'
    except (KeyError, ValueError):
        # tgl can produce invalid instructions. Skip them
        print "Skipping invalid instruction: {0}".format(cmd)
    ptr += 1

print register
