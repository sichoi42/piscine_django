#!/usr/bin/python3
import sys
import os
import settings

def treat_argv():
	if len(sys.argv) != 2:
		sys.exit()
	file_path = sys.argv[1]
	if os.path.splitext(file_path)[1] != '.template':
		sys.exit()
	if os.path.isfile(file_path) == False:
		sys.exit()
	return file_path

def is_match(temp, v):
	v = "{" + v + "}"
	if v in temp:
		return True, v
	else:
		return False, v

def rendering():
	f = treat_argv()
	var = dir(settings)[8:]
	dic = dict()
	for v in var:
		dic[v] = getattr(settings, v)
	file_temp = open(f, 'r')
	temp = file_temp.read()
	for key in dic.keys():
		if type(dic[key]) == int:
			dic[key] = str(dic[key])
		result, brace = is_match(temp, key)
		if result == True:
			temp = temp.replace(brace, dic[key])
	file_html = open("myCV.html", 'w')
	file_html.write(temp)
	file_html.close()
	file_temp.close()

if __name__ == '__main__':
	rendering()
