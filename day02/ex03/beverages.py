#!/usr/bin/python3

class HotBeverage:
	def __init__(self, price=None, name=None):
		self.price = 0.30
		self.name = "hot beverage"

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		name = self.name
		price = self.price
		description = self.description()
		return	(f"name : {name}\n"
				f"price : {price:.2f}\n"
				f"description : {description}")

class Coffee(HotBeverage):
	def __init__(self):
		self.name = "coffee"
		self.price = 0.40

	def description(self):
		return "A coffeee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		self.name = "tea"
		self.price = 0.30

class Chocolate(HotBeverage):
	def __init__(self):
		self.name = "chocolate"
		self.price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		self.name = "cappuccino"
		self.price = 0.45

	def description(self):
		return "'Un po' di Italia nella sua tazza!"

def test():
	hot = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	choco = Chocolate()
	cappu = Cappuccino()
	print(hot)
	print(coffee)
	print(tea)
	print(choco)
	print(cappu)

if __name__ == '__main__':
	test()
