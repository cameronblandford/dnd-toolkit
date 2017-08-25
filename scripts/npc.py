import random

NAMES = ['Abrielle', 'Adara', 'Bastian', 'Cara', 'Caspian', 'Darius', 'Devlyn',
'Korbin', 'Lilith', 'Marius', 'Remus', 'Riona', 'Tressa', 'Xanthus', 'Zephyr',
'Yeriel', 'Zira', 'Torin', 'Torc', 'Tylien', 'Sephyra', 'Salina', 'Mora', 'Kirst',
'Glynn', 'Gavin', 'Lan', 'Ledo', 'Alayn', 'Agata', 'Kira']

RACES = ['Human', 'Dwarf', 'Elf', 'Tiefling', 'Orc', 'Gnome', 'Goblin', 'Kobold']
BACKGROUNDS = ['Beggar', 'Potion Seller', 'Vintner', 'Blacksmith', 'Hermit', 'Rich Eccentric', 
'Devout Acolyte', 'Entertainer', 'Deserter', 'Painter', 'Mercenary', 'Thief', 'Town Drunk', 'Sailor', 'Food truck owner', 'Scholar', 'Assassin', 'Royalty']
ACCENT = ['German', 'Russian', 'French', 'New Yorker', 'Surfer', 'Fast', 'Slow', 'Slurred', 'High', 'Low', 
'Suggestive', 'Breathy', 'Well-enunciated', 'Mumbling']
PERSONALITIES = ['passive-aggressive', 'extremely helpful', 'harmlessly paranoid', 'explosive', 'very shy', 'articulate', 'charming',
'optimistic', 'pessimistic', 'playful', 'lazy', 'serious', 'aloof', 'cruel', 'condescending', 'weak-willed',
'superficial', 'gluttonous', 'energetic', 'slothful', 'perceptive']
QUIRKS = ['has a glass eye', ' has a prosthetic limb', 'fidgets', 'has a scar', 'uses long words incorrectly',
'smells like something specific', 'has perfect skin', 'makes no noise when laughing', 'uses a parasol',
'is hard of hearing', 'is easily frightened', 'greatly exaggerates', 'gestures wildly', 'carries a huge backpack full of partially useful trinkets',
'carries a small pet in their pocket', 'calls characters by the wrong names', 'always has a new injury', 'picks lint off eveyrone\'s clothes',
'wears an obvious wig', 'chews bits of grass, sticks, and leaves']
GOALS = ['open a successful business', 'collect something from every city in the world', 'experience a real adventure', 'live a happy life with their spouse and children',
'bring about the end of the world', 'help the players out', 'make the perfect meal', 'get rich', 'find that special someone',
'run a successful food review periodical', 'overthrow the government', 'become immortal', 'have a statue built of themselves',
'acquire a noble title', 'learn as much as possible about every monster that exists', 'party REALLY hard',
'prove themselves to their god', 'cause chaos everywhere they go', 'befriend then kill the players', 'kill the players (but they\'re comically bad at it'
]

class NPC:
	def __init__(self):
		self.name = random.choice(NAMES)
		self.race = random.choice(RACES)
		self.background = random.choice(BACKGROUNDS)
		self.personality = random.choice(PERSONALITIES) + " and " + random.choice(PERSONALITIES)
		self.quirk = random.choice(QUIRKS)
		self.goal = random.choice(GOALS)

	def __str__(self):
		return self.name + " is a " + self.personality + " " + self.race + " " + \
		self.background + " who " + self.quirk + " and wants to " + self.goal

if __name__ == "__main__":
	print(NPC())