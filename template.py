#!/opt/homebrew/bin/python3

import time

fn = "test.txt"
#fn = "input.txt"

start_time = time.time()

with open(fn, 'r') as f:
	pass

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
