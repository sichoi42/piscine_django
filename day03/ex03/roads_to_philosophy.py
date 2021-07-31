#!/usr/bin/python3
import sys, requests
from bs4 import BeautifulSoup

def jumping(wiki_url, word):
	jump_count = 0
	url = wiki_url + '/wiki/' + word
	r = requests.get(url)
	try:
		r.raise_for_status()
	except requests.HTTPError:
		print("It's a dead end !")
		sys.exit()
	Next = ''
	name = ''
	tmp = [name,]
	while True:
		jump_count += 1
		soup = BeautifulSoup(r.text, 'html.parser')
		name = soup.find(attrs= {'id':'firstHeading'}).text
		print(name)
		tmp.append(name)
		for value in tmp:
			if tmp.count(value) > 1:
				print("It leads to an infinite loop !")
				sys.exit()
		if name == 'Philosophy':
			break
		find_p = soup.find('p')
		while True:
			if str(find_p.attrs) == "{}":
				break
			find_p = find_p.find_next('p')
		find_a = find_p.find_next('a')
		while True:
			if str(find_a.atrrs) != "{}":
				if find_a != None and find_a.get('href') != None:
					if not 'Help' in find_a.get('href') and not '#' in find_a.get('href'):
						break
			find_a = find_a.find_next('a')
		Next = find_a.get('href')
		url = wiki_url + Next
		r = requests.get(url)
		try:
			r.raise_for_status()
		except requests.HTTPError as e:
			raise e
	print('{number} roads from {request} to philosophy !'.format(number=jump_count, request=word))

def roads_to_philo():
	if len(sys.argv) != 2:
		print("You should give one parameter to search!")
		sys.exit()
	wiki_url = "https://en.wikipedia.org"
	jumping(wiki_url, sys.argv[1])

if __name__ == '__main__':
	roads_to_philo()
