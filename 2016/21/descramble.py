#!/usr/bin/python


plaintext = list(raw_input("Password: "))

instructions = []
with open('instructions') as f:
    for line in f:
        instructions.append(line.strip())
instructions.reverse()

for line in instructions:
    print line.strip()
    parts = line.strip().split(' ')
    if parts[0] == 'swap':
        if parts[1] == 'position':
            plaintext[int(parts[5])], plaintext[int(parts[2])] = plaintext[int(parts[2])], plaintext[int(parts[5])]
        elif parts[1] == 'letter':
            pos1 = plaintext.index(parts[5])
            pos2 = plaintext.index(parts[2])
            plaintext[pos1], plaintext[pos2] = plaintext[pos2], plaintext[pos1]
    elif parts[0] == 'reverse':
        start = int(parts[2])
        segment = plaintext[start:int(parts[4])+1]
        print segment
        segment.reverse()
        print segment
        for i in range(len(segment)):
            plaintext[start+i] = segment[i]
    elif parts[0] == 'rotate':
        if parts[1] == 'based':
# len=8 0->1, 1->3, 2->5, 3->7, 4->2, 5->4, 6->6, 7->0
0 = ? (-9 / 7)
1 = ? (-1 / 7)
2 = ? (-6 / 2 / 10)
3 = ? (-2 / 6)
4 = ? (-7 / 1 / 9)
5 = ? (-3 / 5) 
6 = ? (-8 / 8) 6 - 14
7 = ? (-4 / 4)
rotmap = [1, 1, 6, 2, 7, 3, 0, 4]

# len=5 0->1, 1->3, 2->0, 3->2, 4->0
            idx = plaintext.index(parts[6])
            rot = rotmap[idx]
            for i in range(rot):
                letter = plaintext.pop(0)
                plaintext.append(letter)
            
        elif parts[1] == 'right':
            for i in range(int(parts[2])):
                letter = plaintext.pop(0)
                plaintext.append(letter)
        else:
            for i in range(int(parts[2])):
                letter = plaintext.pop()
                plaintext.insert(0, letter)
    elif parts[0] == 'move':
        letter = plaintext.pop(int(parts[5]))
        plaintext.insert(int(parts[2]), letter)
    print ''.join(plaintext)

print ''.join(plaintext)
