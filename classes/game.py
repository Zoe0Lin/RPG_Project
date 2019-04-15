import random


class Color:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Person:
	def __init__(self, name, hp, mp, atk, df, magic,items):
		self.max_hp = hp
		self.hp = hp
		self.max_mp = mp
		self.mp = mp
		self.atkl = atk-10
		self.atkh = atk+10
		self.df = df
		self.magic = magic
		self.action = ["Attack", "Magic", "Items"]
		self.items = items
		self.name = name


	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)

	# def generate_spell_damage(self, i):
	# 	mgl = self.magic[i]["dmg"]-5
	# 	mgh = self.magic[i]["dmg"]+5
	# 	return random.randrange(mgl, mgh)

	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def heal(self, dmg):
		self.hp += dmg
		if self.hp > self.max_hp:
			self.hp = self.max_hp

	def get_hp(self):
		return self.hp

	def get_max_hp(self):
		return self.max_hp

	def get_mp(self):
		return self.mp

	def get_max_mp(self):
		return self.max_mp

	def reduce_mp(self, cost):
		self.mp -= cost

#	def get_spell_name(self, i):
#		return self.magic[i]["name"]

#	def get_spell_cost(self, i):
#		return self.magic[i]["cost"]

	def choose_action(self):
		i = 1

		print("\n" + Color.BOLD + self.name + Color.ENDC)
		print(Color.OKBLUE + Color.BOLD + "Actions" + Color.ENDC)
		for item in self.action:
			print("	"+str(i) + ":", item)
			i += 1

	def choose_magic(self):
		i = 1
		print("\n"+Color.OKBLUE + Color.BOLD + "Magic" + Color.ENDC)
		for spell in self.magic:
			print("	"+str(i) + ":", spell.name, "(cost:", str(spell.cost), ", damage:", str(spell.dmg) ,")")
			i += 1

	def choose_items(self):
		i = 1
		print(Color.OKBLUE + Color.BOLD + "Items" + Color.ENDC)
		for item in self.items:
			print("	" + str(i) , ":", item["item"].name + ": " + item["item"].description, "x"+ str(item["quantity"]))
			i += 1

	def choose_target(self, enemies):
		i = 1
		print(Color.FAIL + Color.BOLD + "Target" + Color.ENDC)
		for enemy in enemies:
			print("	" + str(i), ":", enemy.name )
			i +=1
		choice = int(input("Choose target:")) -1
		return choice





	def get_stats(self):

		hp_bar = ""
		bar_ticks = (self.get_hp()/self.get_max_hp()) * 25

		while bar_ticks > 0:
			hp_bar += "█"
			bar_ticks -= 1
		while len(hp_bar) < 25:
			hp_bar += " "

		mp_bar = ""
		mp_ticks = (self.get_mp()/self.get_max_mp()) * 10

		while mp_ticks > 0:
			mp_bar += "█"
			mp_ticks -= 1
		while  len(mp_bar) < 10:
			mp_bar += " "


		# print("                   _________________________           __________")
		hp_string = str(self.get_hp()) + "/" + str(self.max_hp)
		mp_string = str(self.get_mp()) + "/" + str(self.max_mp)

		print(Color.BOLD + self.name + " "*(20-len(self.name)-len(hp_string)) + hp_string + "|" +
			  Color.OKGREEN + hp_bar +Color.ENDC +"|" + " "*(9-len(mp_string))+ mp_string +
			  "|" +Color.OKBLUE + mp_bar   + Color.ENDC + "|")


	def get_enemy_stats(self):
		hp_bar = ''
		bar_ticks = (self.hp/self.max_hp)* 50
		while bar_ticks > 0:
			hp_bar += "█"
			bar_ticks -=1
		while len(hp_bar) < 50:
			hp_bar += " "

		hp_string = str(self.get_hp()) + "/" + str(self.max_hp)

		if self.hp != 0:
			print(Color.BOLD + self.name + " " * (20 - len(self.name) - len(hp_string)) + hp_string + "|" +
			  Color.FAIL + hp_bar + Color.ENDC + "|" )













