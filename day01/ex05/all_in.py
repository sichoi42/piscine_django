#!/usr/bin/python3
import sys

def trict_input(word):
	if word == ' ':
		return
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
	word = word.strip()
	tmp = word
	word = word.title()
	if word in states.keys():
		state = states[word]
		print(capital_cities[state], "is the capital of", word, end = "\r\n")
	elif word in capital_cities.values():
		for key, value in capital_cities.items():
			if value == word:
				for key2, value2 in states.items():
					if key == value2:
						print(word, "is the capital of", key2, end = "\r\n")
	else:
		print(tmp, "is neither a capital city nor a state", end = "\r\n")




def print_all():
	if len(sys.argv) != 2:
		sys.exit()
	lst = sys.argv[1].split(',')
	for i in range(0, len(lst)):
		trict_input(lst[i])

if __name__ == '__main__':
	print_all()
