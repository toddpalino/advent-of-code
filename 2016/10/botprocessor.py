#!/usr/bin/python

import re
import sys

value_re = re.compile("value ([0-9]+) goes to bot ([0-9]+)")
instruction_re = re.compile("bot ([0-9]+) gives low to (output|bot) ([0-9]+) and high to (output|bot) ([0-9]+)")

bots = {}
outputs = {}

def give_chip(chip, bot):
    if bot not in bots:
        bots[bot] = {'chips': [chip], 'low': None, 'high': None}
    else:
        if len(bots[bot]['chips']) == 2:
            print "bot {0} can't have 3 chips".format(bot)
            sys.exit(1)
        bots[bot]['chips'].append(chip)

def output_chip(chip, output):
    if output not in outputs:
        outputs[output] = [chip]
    else:
        outputs[output].append(chip)

for ln in sys.stdin.readlines():
    m = value_re.match(ln)
    if m:
        give_chip(int(m.group(1)), int(m.group(2)))
        continue

    m = instruction_re.match(ln)
    if m:
        bot = int(m.group(1))
        if bot not in bots:
            bots[bot] = {'chips': [], 'low': None, 'high': None}
        if m.group(2) == 'output':
            bots[bot]['low'] = -(int(m.group(3)) + 1)
        else:
            bots[bot]['low'] = int(m.group(3))
            
        if m.group(4) == 'output':
            bots[bot]['high'] = -(int(m.group(5)) + 1)
        else:
            bots[bot]['high'] = int(m.group(5))

did_work = True
while did_work:
    did_work = False
    for bot_id, bot in bots.iteritems():
        if len(bot['chips']) < 2:
            continue

        did_work = True
        chips = {'low': min(bot['chips']), 'high': max(bot['chips'])}
        if (chips['low'] == 17) and (chips['high'] == 61):
            print "FOUND: bot {0}".format(bot_id)

        for t in ['low', 'high']:
            if bot[t] >= 0:
                give_chip(chips[t], bot[t])
            else:
                output_chip(chips[t], -(bot[t] + 1))
        bot['chips'] = []

print outputs[0][0] * outputs[1][0] * outputs[2][0]
