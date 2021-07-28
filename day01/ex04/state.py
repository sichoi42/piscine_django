import sys

def print_state():
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
	states = dict(zip(states.values(), states.keys()))
	capital_cities = dict(zip(capital_cities.values(), capital_cities.keys()))
	if sys.argv[1] not in capital_cities:
		print('Unknown capital city')
	else:
		city = capital_cities[sys.argv[1]]
		print(states[city])

if __name__ == '__main__':
	print_state()
