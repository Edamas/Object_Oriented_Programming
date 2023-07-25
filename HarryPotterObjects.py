import random

valid_houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
with open('personagens.csv', 'r', encoding='utf-8') as f:
	valid_names = f.read().split('\n')

class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house

	# Get student and house
	@classmethod
	def get(cls):
		name = Choose.name()  #'Harry Potter'  # input('Name: ')
		house = Choose.house()  #'Gryffindor'  # input('House: ')
		return cls(name, house)

	# name
	@property  # Getter
	def name(self):
		return self._name
	
	@name.setter  # Setter
	def name(self, name):
		global valid_names
		if name in valid_names:
			self._name = name
		else:
			raise ValueError(f'Invalid name. Valid names are {valid_names}')
	
	# house		
	@property  # Getter
	def house(self):
		return self._house
	
	@house.setter  # Setter
	def house(self, house):
		global valid_houses
		if house in valid_houses:
			self._house = house
		else:
			raise ValueError(f'Invalid house. Valid houses are {valid_houses}')

	def __str__(self):
		return f'{self.name} from {self.house}'


class Choose:
	global valid_houses
	global valid_names

	@classmethod
	def name(cls):
			return random.choice(valid_names)
	
	@classmethod
	def house(cls):
		return random.choice(valid_houses)


def main():
	student = Student.get()
	print(student)


if __name__ == '__main__':
		main()
