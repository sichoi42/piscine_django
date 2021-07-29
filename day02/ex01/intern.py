#!/usr/bin/python3

class Intern:

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def __init__(self, Name=None):
		if Name == None:
			self.Name = "My name? I'm nobody, an intern, I have no name."
		else:
			self.Name = Name
	def __str__(self):
		return self.Name
	def work(self):
		raise Exception("I'm just an intern, I can't do that...")
	def make_coffee(self):
		return Intern.Coffee()

def testing():
	intern1 = Intern()
	intern2 = Intern("Mark")
	print(intern1.Name)
	print(intern2.Name)
	print(intern2.make_coffee())
	try:
		intern1.work()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	testing()
