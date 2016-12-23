#!/usr/bin/python

plaintext = list(raw_input("Password: "))

with open('instructions') as f:
    for line in f:
        parts = line.strip().split(' ')
        if parts[0] == 'swap':
            if parts[1] == 'position':
                plaintext[int(parts[2])], plaintext[int(parts[5])] = plaintext[int(parts[5])], plaintext[int(parts[2])]
            elif parts[1] == 'letter':
                pos1 = plaintext.index(parts[2])
                pos2 = plaintext.index(parts[5])
                plaintext[pos1], plaintext[pos2] = plaintext[pos2], plaintext[pos1]
        elif parts[0] == 'reverse':
            start = int(parts[2])
            segment = plaintext[start:int(parts[4])+1]
            for i in range(len(segment)):
                plaintext[start+i] = segment[-(i+1)]
        elif parts[0] == 'rotate':
            if parts[1] == 'based':
                for i in range(plaintext.index(parts[6]) + (1 if idx < 4 else 2)):
                    letter = plaintext.pop()
                    plaintext.insert(0, letter)
            elif parts[1] == 'left':
                for i in range(int(parts[2])):
                    letter = plaintext.pop(0)
                    plaintext.append(letter)
            else:
                for i in range(int(parts[2])):
                    letter = plaintext.pop()
                    plaintext.insert(0, letter)
        elif parts[0] == 'move':
            letter = plaintext.pop(int(parts[2]))
            plaintext.insert(int(parts[5]), letter)

print "SCRAMBLED: " + ''.join(plaintext)
