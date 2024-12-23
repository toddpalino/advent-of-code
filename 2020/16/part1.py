#!/usr/bin/python3

fields = {}
my_ticket = []
nearby_tickets = []

#with open("test.txt") as f:
with open("input.txt") as f:
	parsing_tickets = False

	for line in f:
		ln = line.strip()
		if len(ln) == 0:
			continue

		if 'ticket' in ln:
			parsing_tickets = True
			continue
			
		if parsing_tickets:
			ticket = [int(n) for n in ln.split(',')]
			if not my_ticket:
				my_ticket = ticket
			else:
				nearby_tickets.append(ticket)
			continue

		# Parsing fields
		parts = ln.split(': ')
		ranges = parts[1].split(' or ')
		fields[parts[0]] = [[int(n) for n in r.split('-')] for r in ranges]

invalid_sum = sum(num for ticket in nearby_tickets for num in ticket if all(not r[0] <= num <= r[1] for ranges in fields.values() for r in ranges))
print(invalid_sum)
		
