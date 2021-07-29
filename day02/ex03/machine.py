#!/usr/bin/python3
import random
from beverages import *

class CoffeeMachine:

	def __init__(self):
		self.count = 0

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def serve(self, HotBeverage):
		self.count += 1
		if self.count > 10:
			raise CoffeeMachine.BrokenMachineException
		else:
			if random.randint(0, 5) == 0:
				return CoffeeMachine.EmptyCup()
			else:
				return HotBeverage

	def repair(self):
		self.count = 0
		print("repaired!")


def test():
	c = CoffeeMachine()
	for i in range(0, 12):
		try:
			print(c.serve(random.choice([Coffee(), Tea(), Cappuccino(), Chocolate()])))
		except c.BrokenMachineException as e:
			print(e)
			c.repair()

if __name__ == '__main__':
	test()
