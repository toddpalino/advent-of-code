#!/usr/bin/python

password = [ord(c) for c in raw_input("Password: ")]

while True:
    carry = 1
    skip_password = False
    for i in range(-1, -(len(password)+1), -1):
        newval = password[i] + carry
        carry = newval / 123
        password[i] = ((newval - 97) % 26) + 97
        if password[i] in [105, 108, 111]:
            skip_password = True
    if carry > 0:
        password = [97] + password
    if skip_password:
        # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
        continue

    has_straight = False
    num_pairs = 0
    i = 0
    pwlen = len(password)
    while i < pwlen:
        # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
        if i < (pwlen - 2) and password[i+1] == (password[i] + 1) and password[i+2] == (password[i] + 2):
            has_straight = True

        # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
        if i < (pwlen - 1) and password[i] == password[i+1]:
            num_pairs += 1

            # Need to consume the pair, but make sure we don't kill a possible straight that overlaps
            if i < (pwlen - 2) and password[i+2] == (password[i] + 1):
                i += 1
            else:
                i += 2
        else:
            i += 1

    if has_straight and num_pairs >= 2:
        print "NEXT PASSWORD: {0}".format(''.join([chr(c) for c in password]))
