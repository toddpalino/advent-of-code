#!/usr/bin/python3

import time
from collections import deque


def find_all(a_str, sub):
	start = 0
	try:
		while True:
			start = a_str.index(sub, start)
			yield start
			start += len(sub)
	except ValueError:
		return


#target = "HOHOHO"
#fn = "test_replacements"

target = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
fn = "replacements"

start_time = time.time()

# We're going to reverse engineer the target, so we want reverse replacements
replacements = {}
with open(fn, 'r') as f:
	for line in f:
		parts = line.strip().split(' => ')
		replacements[parts[1]] = parts[0]

sorted_srcs = sorted(replacements.keys())

total_moves = None
queue = deque([(0, target)])
while queue:
	state = queue.popleft()
	swap_count = state[0]
	current_str = state[1]
	if current_str == 'e':
		total_moves = swap_count
		break

	for src in sorted_srcs:
		tgt = replacements[src]
		src_len = len(src)
		for i in find_all(current_str, src):
			queue.appendleft((swap_count + 1, current_str[0:i] + tgt + current_str[i+src_len:]))

print("Swaps Required: %d" % (total_moves))

end_time = time.time()
print("Elapsed time: %f" % (end_time - start_time))
