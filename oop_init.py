class Person:
	def __init__(self,name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is ',self.name)

name = input('enter the name:')
p = Person(name)
p.say_hi()
