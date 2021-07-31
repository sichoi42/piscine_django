#!/usr/bin/python3
from local_lib.path import Path

def start_program():
	d = Path('./a')
	d.mkdir_p()
	d = Path('./a/my_file.py')
	d.touch()
	d.write_text('hello!', encoding='utf-8')
	print(d.read_text(encoding='utf-8'))
if __name__ == '__main__':
	start_program()
