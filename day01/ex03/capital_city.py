#!/usr/bin/python3
import sys

def print_capital():
	if len(sys.argv) != 2:
		sys.exit()
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if sys.argv[1] not in states:
		print('Unknown state')
	else:
		state = states[sys.argv[1]]
		print(capital_cities[state])


if __name__ == '__main__':
	print_capital()
