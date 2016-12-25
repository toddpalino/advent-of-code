#!/usr/bin/python

import sys

class LoopBreakerException (Exception):
    pass


instructions = []
with open('instructions') as f:
    for line in f:
        instructions.append(line.strip().split(' '))

start_val = 0
while True:
    register = {
        'a': start_val,
        'b': 0,
        'c': 0,
        'd': 0
    }

    try:
        ptr = 0
        last_out = 1
        out_count = 0
        while ptr < len(instructions):
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
                elif cmd[0] == 'out':
                    val = register[cmd[1]] if cmd[1] in register else int(cmd[1])
                    if last_out == val:
                        raise LoopBreakerException
                    last_out = val
                    out_count += 1
                    if out_count >= 10000:
                        print "START VAL: {0}".format(start_val)
                        sys.exit(0)
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
    except LoopBreakerException:
        start_val += 1
        continue
