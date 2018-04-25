from random import randint

	def character_creation():
	
		print("You may pick a character type. Each type has different base stats.")
		print("/n Your options are: Mage, Elf, Goblin, Human, or Fairy")
		print("/n A Mage has a base HP + Stamina of 5, a base Wisdom of 3, and 1 for all other stats. Their special ability is a 25% chance of obtaining an extra move roll.")
		print("/n An Elf has a base HP of 10, Stamina, Charisma, and Dexterity of 5, Wisdom of 3, Strength of 2, and 1 for all other stats. Their special ability is a 10% chance of avoiding battle.")
		print("/n A Goblin has a base HP and Strength of 5, Stamina of 10, Defense of 2, and 0 for all other stats. Their special ability is the option to intimidate weaker [1/2 of their HP or lower] enemies from battle.")
		print("/n A Human has a base HP and Stamina of 5, a Defense of 0, and 1 for all other stats. Their special ability is regaining 1 stamina per turn.")
		print("/n A Fairy has a base HP of 5,  Stamina of 10, Dexterity of 3, Strength of 0, and 1 for all other stats. Their special ability is regaining 1 HP per turn.")
		
		string character = input("Please pick your character type. Type "Mage, Elf, Goblin, Human, or Fairy" : ")
		
		# Could soft code these values, but I hard coded them to put them in a particular order based off HP/Stamina priority and highest to weakest


	def enemy_options():
	
		def enemy_one():
			string name = "Mud Monster"
			int hp = (random.randint(character_level,character_level*3))
			int stamina = 5
			int defense = 0
			int xp_worth = (random.randint(hp*1.5,hp*2.5))
			
		def enemy_two():
			string name = "Random Solider" 
			int hp = (random.randint(character_level,character_level*3))
			int stamina = 3
			int defense = 1
			int xp_worth = (random.randint(hp*1.5,hp*2.5))
		
		def enemy_three():
			string name = "hyperMouse Ninja"
			int hp = (random.randint(character_level,character_level*3))
			int stamina = 10
			int defense = 2
			int xp_worth = (random.randint(hp*1.5,hp*2.5))
		
		def enemy_four():
			string name = "Mole People" 
			int hp = (random.randint(character_level,character_level*3))
			int stamina = 5
			int defense = 1
			int xp_worth = (random.randint(hp*1.5,hp*2.5))
		
		def enemy_five():
			string name = "Gargoyle"
			int hp = (random.randint(character_level,character_level*3))
			int stamina = 2
			int defense = 5
			int xp_worth = (random.randint(hp*1.5,hp*2.5))
		
	def 