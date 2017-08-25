import random

QUEST_GIVERS = ['A treant', 'The local bartender', 'A local prostitute', 'A dragon communicating with you telepathically', 'A colony of sentient mice', 'A pair of lovers',
'An angry old man who sometimes yells at clouds', 'The captain of the local militia', 'A member of a local anarchist group']

REQUESTS = ['requests', 'demands', 'politely asks', 'begs']

ACTIONS = ['find', 'kill', 'retrieve', 'rescue', 'obliterate', ]

OBJECTS = ['their family heirloom', 'their beloved pet', 'their teen son/daughter', 'their arch-rival', 'some precious pieces of art']


class Quest:
	def __init__(self):
		self.quest_giver = random.choice(QUEST_GIVERS)
		self.request = random.choice(REQUESTS)
		self.action = random.choice(ACTIONS)
		self.object = random.choice(OBJECTS)

	def __str__(self):
		return self.quest_giver + " " + self.request + " that you " + self.action + " " + self.object


if __name__ == '__main__':
	print(Quest())