def file_open():
	file = open("numbers.txt", "r")
	line = file.read().replace(',', '\n')
	print(line, end='')
	file.close()

if __name__ == '__main__':
	file_open()
