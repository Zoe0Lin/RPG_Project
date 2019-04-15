from classes.game import Person, Color
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140,  "black")

cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Item
potion = Item("Potion", "potion", "Heals 50 HP.", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP.", 100)
superpotion = Item("Super Potion", 'potion', "Heals 500 HP.", 500)
elixir = Item("Elixir", 'elixir', 'Fully restores HP/MP of one party member.', 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP.",9999)

grenade = Item("Grenade", "attack", "Deals 500 Damage.", 500)

# Instantiate Player
player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15},
				{"item": hipotion, "quantity":5},
				{"item": superpotion, "quantity":5},
				{"item": elixir, "quantity": 5},
				{"item": hielixir, "quantity":2},
				{"item": grenade, "quantity":5}]


player1 = Person("Luis", 460, 65, 500, 34, player_magic, player_items)
player2= Person("Joe", 400, 60, 520, 34, player_magic, player_items)
player3 = Person("Ken", 420, 50, 510, 34, player_magic, player_items)
players = [player1, player2, player3]

# Instantiate Enemy
enemy1 = Person('Imp',2000, 300, 50, 80, [],[])
enemy2 = Person('Vincent',1000, 800, 90, 25, [],[])
enemy3 = Person("Imp", 2000, 300, 50, 80,[],[])
enemies = [enemy1, enemy2, enemy3]

# Procedure
running = True
i = 1

print(Color.FAIL + Color.BOLD + "An Enemy Attacks!" + Color.ENDC)

while running:
	print("\n")

	print("====================================================================")
	print("NAME" + " " * 15 + "HP" + "_" * 25 + " " * 9 + "MP" + "_" * 10)

	for player in players:
		player.get_stats()
	print("\n")

	print("ENEMY" + " " * 14 + "HP" + "_" * 50)
	for enemy in enemies:
		enemy.get_enemy_stats()


	for player in players:
		# player.get_stats()

		player.choose_action()

		choice = input("Choose action:")
		index = int(choice) - 1


		# Choose Attack
		if index == 0:
			dmg = player.generate_damage()
			enemy = player.choose_target(enemies)
			enemies[enemy].take_damage(dmg)
			print( Color.FAIL + "\nYou attacked "+ enemies[enemy].name + " for", dmg, "points of damage."+ Color.ENDC)

			if enemies[enemy].get_hp() == 0:
				print(Color.FAIL + enemies[enemy].name + " has been defeated" + Color.ENDC )
				del enemies[enemy]



		# Choose Magic
		elif index == 1:
			player.choose_magic() # Call function
			magic_choice = int(input("Choose magic: "))-1 # User input
			if magic_choice == -1:
				continue

			spell = player.magic[magic_choice] # Choose magic
			magic_dmg = spell.generate_damage() # Get magic damage
			cost = spell.cost # Get magic cost

			current_mp = player.get_mp()

			if spell.cost > current_mp:
				print(Color.FAIL + "\nNo Enough MP\n"+ Color.ENDC)
				continue
			player.reduce_mp(cost)

			if spell.type == "white":
				player.heal(magic_dmg)
				print(Color.OKBLUE + '\n' + spell.name + " heals for", magic_dmg, "HP." + Color.ENDC )
				print(Color.OKBLUE + spell.name + " cost " + str(cost) + " points of MP.",Color.ENDC)
			elif spell.type == "black":
				enemy = player.choose_target(enemies)
				enemies[enemy].take_damage(magic_dmg)
				# enemy.take_damage(magic_dmg)
				print(Color.OKBLUE + "\n" + spell.name + " deals",enemies[enemy].name ,str(magic_dmg)+" points of damage."+ Color.ENDC)
				print(Color.OKBLUE + spell.name + " cost " + str(cost) + " points of MP.", Color.ENDC)

				if enemies[enemy].get_hp() == 0:
					print(Color.FAIL + enemies[enemy].name + " has been defeated" + Color.ENDC)
					del enemies[enemy]



		# Choose Items
		elif index == 2:
			player.choose_items()
			item_choice = int(input("Choose items: "))-1
			if item_choice == -1:
				continue

			item = player.items[item_choice]

			if player.items[item_choice]['quantity'] == 0:
				print(Color.FAIL, "None Left....", Color.ENDC)
				continue

			player.items[item_choice]['quantity'] -=1



			if item["item"].type == 'potion':
				player.heal(item['item'].prop)
				print(Color.BOLD + Color.OKGREEN + "\n" + item['item'].name, "heals for ", item['item'].prop ,"HP." + Color.ENDC)

			elif item['item'].type == "elixir":
				if item['item'].name == "MegaElixir":
					for i in players:
						i.hp = i.max_hp
						i.mp = i.max_mp
					print(Color.OKGREEN + "\n" + "Fully restored party's HP/MP." + Color.ENDC)

				else:

					player.hp = player.max_hp
					player.mp = player.max_mp
					print(Color.OKGREEN + "\n" + item['item'].name + " fully restored HP/MP." + Color.ENDC)


			elif item['item'].type == "attack":
				enemy = player.choose_target(enemies)
				enemies[enemy].take_damage(item['item'].prop)
				print(Color.FAIL + "\n" + item['item'].name + " deals " + str(item['item'].prop)+" points damage to "
					  + enemies[enemy].name + Color.ENDC)

				if enemies[enemy].get_hp() == 0:
					print(Color.FAIL+ Color.BOLD + enemies[enemy].name + " has been defeated" + Color.ENDC)
					del enemies[enemy]

	# ### Show Status
	# print("*" * 22)
	# print(Color.BOLD + "Enemy HP:", Color.FAIL + str(enemy.get_hp()) + "/" + str(enemy.max_hp) + Color.ENDC)
	# print(Color.BOLD + "Your HP:", Color.OKGREEN + str(player.get_hp()) + "/" + str(player.max_hp) + Color.ENDC)
	# print(Color.BOLD + "Your MP:", Color.OKBLUE + str(player.get_mp()) + "/" + str(player.max_mp) + Color.ENDC)
	#

	# Enemy Always Attack
	Enemy_choice = 1
	target = random.randrange(0,3)
	enemy_dmg = enemies[enemy].generate_damage()
	players[target].take_damage(enemy_dmg)
	print(Color.FAIL + "Enemy attacks " + players[target].name, "for", str(enemy_dmg) +" points!" + Color.ENDC)


	# End Game
	defeated_enemies = 0
	for enemy in enemies:
		if enemy.get_hp() == 0:
			defeated_enemies += 1

	if defeated_enemies==3:
		print(Color.BOLD + Color.OKGREEN + "You win!" + Color.ENDC)
		running = False

	defeated_players = 0
	for play in players:
		if player.get_hp() == 0:
			defeated_players +=1
	if defeated_players == 3:
		print(Color.BOLD + Color.FAIL + "Your enemies have defeated you!" + Color.ENDC)
		running = False





