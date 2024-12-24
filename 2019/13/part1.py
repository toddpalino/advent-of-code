#!/usr/bin/env python

import time
from itertools import batched
from aoc.utils.intcode import Intcode, read_intcode_from_file


start_time = time.time()

computer = Intcode(read_intcode_from_file("input.txt"))
computer.run()
count = sum(1 for t in batched(computer.get_output(), 3) if t[2] == 2)
print(f'Drew {count} block squares')

end_time = time.time()
print("Part 1 Elapsed time: %f" % (end_time - start_time))
