#!/usr/bin/python3
import requests, json, dewiki, sys

def requesting(word):
	url = "https://en.wikipedia.org/w/api.php"

	payload ={
		"action": "parse",
		"summary": word,
		"page": word,
		"redirects": "true",
		"prop": "wikitext",
		"format": "json",
	}
	r = requests.get(url, payload)
	try:
		r.raise_for_status()
	except requests.HTTPError as e:
		raise e
	data = json.loads(r.text)
	if "The page you specified doesn't exist." in str(data):
		data = dewiki.from_string(data['error']['info'])
	else:
		data = dewiki.from_string(data['parse']['wikitext']['*'])
	return data

def make_result_file(data, word):
	word = word.replace(' ', '_')
	file = open(word + '.wiki', 'w')
	file.write(data)
	file.close()

def searching():
	if len(sys.argv) != 2:
		print("You should give one parameter to search!")
		sys.exit()
	else:
		try:
			date = requesting(sys.argv[1])
		except Exception as e:
			print(e)
			sys.exit()
		try:
			make_result_file(date, sys.argv[1])
		except Exception as e:
			print(e)


if __name__ == '__main__':
    searching()

