#you chose... poorly

class Hero():
	
	def __init__(self, name, Class):

		self.name = name
		self.inventory = []
		self.Class = Class

		self.mage = 0
		self.warrior = 0
		self.berserker = 0
		self.assassin = 0
		self.yeet = 0
		self.hidden_class = 0
		
		#player stats
		self.speed = 0
		self.perception = 0
		self.magic = 0
		self.strength = 0
		self.stealth = 0
		self.speech = 0
		self.constitution = 0
		
		#player skills for chapter 1
		self.pickpocket = 0
		self.lock_pick = 0
		self.self_combust = 0
		self.hold_breath = 0
		self.animal_lang = 0
		self.premonition = 0
		self.apocalypse = 0
		
	def pickup(self, item):
		
		self.inventory.append(item)
		 

player = Hero("NONAME", "NOCLASS")