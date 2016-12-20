#!/usr/bin/python

blacklist = []
with open('addresses') as f:
    for line in f:
        ip1, ip2 = line.split('-')
        ip1 = int(ip1)
        ip2 = int(ip2)
        blacklist.append((min(ip1, ip2), max(ip1, ip2)))

highest_ip = 4294967295

blocked_count = 1
max_ip = 0
for ip_range in sorted(blacklist, key=lambda r: r[0]):
    # Check if the next IPs are not covered by the range
    # NOTE - The input only ever skips one, but for correctness we need to iterate here
    for ip in range(max_ip + 1, ip_range[0]):
        print "NOT BLOCKED: {0}".format(ip)

    # Count blocked IPs, taking into account overlapping ranges
    if max_ip < ip_range[0]:
        blocked_count += ip_range[1] - ip_range[0] + 1
    elif max_ip < ip_range[1]:
        blocked_count += ip_range[1] - max_ip
    max_ip = max(max_ip, ip_range[1])

print "BLOCKED: {0} IPs".format(blocked_count)
print "UNBLOCKED: {0} IPs".format(highest_ip - blocked_count + 1)
