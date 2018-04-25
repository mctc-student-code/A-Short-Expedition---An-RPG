from random import randint

HP = 0
Stamina = 0
Intelligence = 0
Wisdom = 0
Luck = 0
Strength = 0
Defense = 0 
Charisma = 0
Dexterity = 0 
character = "None"
#these are global variables

	def character_creation():
	
		print("You may pick a character type. Each type has different base stats.")
		print("/n Your options are: Mage, Elf, Goblin, Human, or Fairy")
		print("/n A Mage has a base HP + Stamina of 5, a base Wisdom of 3, and 1 for all other stats. Their special ability is a 25% chance of obtaining an extra move roll.")
		print("/n An Elf has a base HP of 10, Stamina, Charisma, and Dexterity of 5, Wisdom of 3, Strength of 2, and 1 for all other stats. Their special ability is a 10% chance of avoiding battle.")
		print("/n A Goblin has a base HP and Strength of 5, Stamina of 10, Defense of 2, and 0 for all other stats. Their special ability is the option to intimidate weaker [1/2 of their HP or lower] enemies from battle.")
		print("/n A Human has a base HP and Stamina of 5, a Defense of 0, and 1 for all other stats. Their special ability is regaining 1 stamina per turn.")
		print("/n A Fairy has a base HP of 5,  Stamina of 10, Dexterity of 3, Strength of 0, and 1 for all other stats. Their special ability is regaining 1 HP per turn.")
		
		while character == "None": #This while loop makes the player re-pick whenever they don't have a character
			global character = input("Please pick your character type. Type "Mage, Elf, Goblin, Human, or Fairy" : ")
	
			character_stats(character)
		
		# Could soft code these values, but I hard coded them to put them in a particular order based off HP/Stamina priority and highest to weakest
		# Maybe put the stats printer in a separate method? To just print stats. Maybe even code 'hot keys' to print certain character stats VS all at once? 
		
	def character_stats(string character):
	
		#this chunk of code allows this method to change global variables 
		global HP
		global Stamina
		global Intelligence
		global Wisdom
		global Luck
		global Strength
		global Defense 
		global Charisma
		global Dexterity
		global character 
		
		if character == "Mage":
			HP = 5
			Stamina = 5
			Intelligence = 1
			Wisdom = 3
			Luck = 1
			Strength = 1
			Defense = 1
			Charisma = 1
			Dexterity = 1
		else if character == "Elf":
			HP = 10
			Stamina = 5
			Intelligence = 1
			Wisdom = 3
			Luck = 1
			Strength = 2
			Defense = 1
			Charisma = 5
			Dexterity = 5
		else if character == "Goblin":
			HP = 5
			Stamina = 10
			Intelligence = 0
			Wisdom = 0
			Luck = 0
			Strength = 5
			Defense = 2
			Charisma = 0
			Dexterity = 0
		else if character == "Human":
			HP = 5
			Stamina = 5
			Intelligence = 1
			Wisdom = 1
			Luck = 1
			Strength = 1
			Defense = 0
			Charisma = 1
			Dexterity = 1
		else if character == "Fairy":
			HP = 5
			Stamina = 10
			Intelligence = 1
			Wisdom = 1
			Luck = 1
			Strength = 0
			Defense = 1
			Charisma = 1
			Dexterity = 3
		else:
			character = "None" #if the input does not match any of these, it will reset the character to none and ask for new input 


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
		
	def item_options():
		
		def potion():
			name = "Potion"
			description = "This adds 5 HP"
			worth = 1
			drop_percentage = 35
		
		def hyper_potion():
			name = "Hyper Potion"
			description = "This adds 10 HP"
			worth = 2
			drop_percentage = 15
		
		def super_portion():
			name = "Super Potion"
			description = "This adds 20 HP"
			worth = 5
			drop_percentage = 5
		
		def apple():
			name = "Apple"
			description = "This adds 5 Stamina" 
			worth = 2
			drop_percentage = 35
		
		def chocolate_bar():
			name = "Chocolate Bar" 
			description = "This adds 10 Stamina" 
			worth = 5
			drop_percentage = 15
		
		def fruit_smoothie():
			name = "Fruit Smoothie"
			description = "This adds 10 Stamina and 5 HP"
			worth = 7
			drop_percentage = 10
			
		def chicken_breast():
			name = "Chicken Breast"
			description = "This adds 20 Stamina"
			worth = 7
			drop_percentage = 5
		
		def avocado_toast():
			name = "Avocado Toast"
			description = "This adds 5 Stamina and 5 HP. It also increases your Wisdom by 1" 
			worth = 10
			drop_percentage = 5
			
			#Add drop type values to try and increase the variety of dropped items