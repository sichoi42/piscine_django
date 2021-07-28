import sys

def treat_input(file):
	data = file.readline()
	data = data.split(sep='=')
	name = data[0]
	data = data[1:]
	data = ' '.join(data).replace(' ', '')
	data = data.split(sep=",")
	lst = list()
	for i in range(0,4):
		lst.append(data[i].split(sep=":"))
		lst[i] = {lst[i][0] : lst[i][1]}
	lst.append(name)
	return lst

def make_html():
	mod = sys.modules[__name__]
	file2 = open('periodic_table.html', 'w', encoding = 'UTF-8')
	write_top(file2)
	file2.write("<body>\n")
	file2.write("<h1 style=\"text-align: center;\">periodic_table</h1>\n")
	file = open("periodic_table.txt", "r")
	for i in range(1, 89):
		tmp = treat_input(file)
		j = int(tmp[1]['number'])
		setattr(mod, 'lst_{}'.format(j), tmp)
		make_table(file2, globals()['lst_{}'.format(j)], j)
	make_La(file2)
	make_Ac(file2)
	file.close()
	file2.write("</body>\n")
	file2.write("</html>\n")
	file2.close()

def write_top(file2):
	file2.write("<!DOCTYPE html>\n")
	file2.write("<html lang=\"en\">\n")
	file2.write("<head>\n")
	file2.write("<title>periodic_table</title>\n")
	write_style(file2)
	file2.write("</head>\n")

def make_table(file2, lst, number):
	if number == 1:
		file2.write("<table class=\"period_1 group_1\">\n")
	elif number == 2:
		file2.write("<table class=\"period_1 group_18\">\n")
	elif number >= 3 and number <= 10:
		if number <= 4:
			s = "<table class=\"period_2 group_" + str(number - 2) + "\">\n"
			file2.write(s)
		else:
			s = "<table class=\"period_2 group_" + str(number + 8) + "\">\n"
			file2.write(s)
	elif number >= 11 and number <= 18:
		if number <= 12:
			s = "<table class=\"period_3 group_" + str(number - 10) + "\">\n"
			file2.write(s)
		else:
			s = "<table class=\"period_3 group_" + str(number) + "\">\n"
			file2.write(s)
	elif number >= 19 and number <= 56:
		solve = number // 18
		mod = number % 18
		if mod == 0:
			solve = solve - 1
			mod = mod + 18
		solve += 3
		s = "<table class=\"period_" + str(solve) + " group_" + str(mod) + "\">\n"
		file2.write(s)
	elif number >= 55 and number <= 86:
		if number <= 56:
			s = "<table class=\"period_6 group_" + str(number - 55) + "\">\n"
		else:
			s = "<table class=\"period_6 group_" + str(number - 68) + "\">\n"
		file2.write(s)
	else:
		if number <= 88:
			s = "<table class=\"period_7 group_" + str(number - 86) + "\">\n"
		else:
			s = "<table class=\"period_7 group_" + str(number - 100) + "\">\n"
		file2.write(s)

	file2.write("<tr>\n")
	file2.write("<td>\n")
	small = lst[2]['small']
	s = "<h2>" + small + "</h2>\n"
	file2.write(s)
	file2.write("<ul>\n")
	s = "<li>" + str(number) + "</li>\n"
	file2.write(s)
	name = lst[4]
	s = "<li>" + name + "</li>\n"
	file2.write(s)
	molar = lst[3]['molar']
	s = "<li>" + str(molar) + "</li>\n"
	file2.write(s)
	file2.write("</ul>\n")
	file2.write("</td>\n")
	file2.write("</tr>\n")
	file2.write("</table>\n")

def make_La(file2):
	file2.write("<table class=\"period_6 group_3\" style=\"background-color:pink\">\n")
	file2.write("<tr>\n")
	file2.write("<td>\n")
	file2.write("<h2>La</h2>\n")
	file2.write("<ul>\n")
	file2.write("<li>57~71</li>\n")
	file2.write("<li>lanthanoids</li>\n")
	file2.write("<li>.</li>\n")
	file2.write("</ul>\n")
	file2.write("</td>\n")
	file2.write("</tr>\n")
	file2.write("</table>\n")

def make_Ac(file2):
	file2.write("<table class=\"period_7 group_3\" style=\"background-color:coral\">\n")
	file2.write("<tr>\n")
	file2.write("<td>\n")
	file2.write("<h2>Ac</h2>\n")
	file2.write("<ul>\n")
	file2.write("<li>89~103</li>\n")
	file2.write("<li>actinoids</li>\n")
	file2.write("<li>.</li>\n")
	file2.write("</ul>\n")
	file2.write("</td>\n")
	file2.write("</tr>\n")
	file2.write("</table>\n")

def write_style(file2):
	file2.write("<style>\n")

	make_period(file2)
	make_group(file2)

	file2.write("ul\n")
	file2.write("{\n")
	file2.write("\tlist-style: none;\n")
	file2.write("\tpadding-left: 0px;\n")
	file2.write("}\n")

	file2.write("td\n")
	file2.write("{\n")
	file2.write("\ttext-align: center;\n")
	file2.write("\tborder: 1px solid black;\n")
	file2.write("}\n")
	file2.write("</style>\n")

def make_period(file2):
	for i in range(1, 8):
		s1 = '.period_' + str(i) + '\n'
		s2 = '\ttop: ' + str(150 * i - 80) + 'px;\n'
		file2.write(s1)
		file2.write("{\n")
		file2.write("\tposition: absolute;\n")
		file2.write(s2)
		file2.write("\theight: 70px;\n")
		file2.write("\twidth: 110px;\n")
		file2.write("}\n")

def make_group(file2):
	for i in range(1, 19):
		s1 = '.group_' + str(i) + '\n'
		s2 = '\tleft: ' + str(110 * i - 80) + 'px;\n'
		file2.write(s1)
		file2.write("{\n")
		file2.write("\tposition: absolute;\n")
		file2.write(s2)
		file2.write("}\n")

if __name__ == '__main__':
	make_html()
