from random import randint
import math

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
name = "name"
level = 0
XP = 0
steps = 0
#these are global variables

	def main():
		global name = input("Welcome brave warrior! What is your " + name + "?")
		print("Your quest is to battle to the great beyond and retrieve what may lie there. The people of this hard drive believe there to be great riches which control these lands.")
		character_creation()
		print("Ah! Thank you " + name +" the mighty " + character)
		print("Your brave journey will first take you through this computers invisible folders. Be warned the path is treacherous and many have deleted vital files never to be seen again")
		print("Once through these folders you may come across a theme park of disk fragmentation. From here you may be tempted to wander through many-a application and plenty of shiny bits and bobbles. Deep in the core is where you seek.")
		print("Down the rabbithole you fall. To find the treasures this harddrive holds you must finally saunter the tombs of data past in the fiery holes of the recycling bin!")
		print("Safe travels, " + name + ".")
		
		while steps < 60:
			take_a_step()

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
			string name = "Random Soldier" 
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
		
	def item_options(): #these items need to be recoded as objects 
		
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
			
		def basic_chest_armour():
			name = "Basic Chest Armour" 
			description = "Adds 2 to Defense when equipped"
			worth = 1
			drop_percentage = 30
			max = 1
			ID_Type = 1 #identifies as chest armor so that I can tell the program you can only have 1 at a time
			
		def advance_chest_armour():
			name = "Advance Chest Armour"
			description = "Adds 5 to Defense and subtracts 2 from Strength when equipped"
			worth = 3
			drop_percentage = 20
			max = 1
			ID_Type = 1
		
		def basic_sword():
			name = "Basic Sword" 
			description = "Adds 2 attack when equipped"
			worth = 1
			drop_percentage = 30
			max =1 
			ID_Type = 2
			
		def advance_sword():
			name = "Advance Sword"
			description = "Adds 5 attack when equipped"
			worth = 3
			drop_percentage = 20
			max = 1
			ID_Type = 2
			
		def basic_shield():
			name = "Basic Shield"
			description = "Adds 1 to defense and subtracts 1 from strength when equipped"
			worth = 1
			drop_percentage = 30
			max = 1
			ID_Type = 3
			
		def advance_shield():
			name = "Advance Shield" 
			description = "Adds 2 to defense, subtracts 1 from strength, and subtracts 2 from dexterity"
			worth = 3 
			drop_percentage = 20
			max = 1 
			ID_Type = 3
			
		def basic_crossbow():
			name = "Basic Crossbow"
			description = "Adds 5 to attack when equipped"
			worth = 3
			drop_percentage = 20
			max = 1
			ID_Type = 4
			
		def advance_crossbow():
			name = "Advance Crossbow"
			description = "Adds 12 to attack and subtracts 2 from strength when equipped"
			worth = 10
			drop_percentage = 10
			max = 1 
			ID_Type = 4
			
		def basic_helmet():
			name = "Basic Helmet" 
			description = "Adds 1 to defense when equipped"
			worth = 1
			drop_percentage = 35
			max = 1
			ID_Type = 5
			
		def advance_helmet():
			name = "Advance Helmet" 
			description = "Adds 3 to defense and 1 to stamina when equipped" 
			worth = 2
			drop_percentage = 20
			max = 1 
			ID_Type = 5
			
		def basic_leggings()
			name = "Basic Leggings"
			description = "Adds 1 defense when equipped"
			worth = 1
			drop_percentage = 30
			max = 1
			ID_Type= 6
			
		def advance_leggings():
			name = "Advance Leggings"
			description = "Adds 3 defense and subtracts 1 dexterity when equipped"
			worth = 3 
			drop_percentage = 20
			max = 1
			ID_Type = 6
			
		def chainmail():
			name = "Chainmail"
			description = "Extra underbody armour. Add 1 to defense when equipped"
			worth = 1
			drop_percentage = 30
			max = 1
			ID_Type = 7
			
	def level_up(int which_level):
	
		global HP
		global Stamina
		global Intelligence
		global Wisdom
		global Luck
		global Strength
		global Defense 
		global Charisma
		global Dexterity
		global XP
		global level
		
		HP = HP + randint(1,5)
		Stamina = Stamina + randint(1,5)
	
		for(i = 0; i<3; i++): #for loop that reiterates 3 times 
			trait = randint(3,9)
			
			if trait == 3:	
				Intelligence = Intelligence + randint(1,3)
			else if trait ==4:
				Wisdom = Wisdom + randint(1,3)
			else if trait ==5:
				Luck = Luck + randint(1,3)
			else if trait == 6:
				Strength = Strength + randint(1,3)
			else if trait == 7: 
				Defense = Defense + randint(1,3)
			else if trait == 8:
				Charisma = Charisma + randint(1,3)
			else: 
				Dexterity = Dexterity + randint(1,3)
				
			XP = which_level-XP #subtracts XP used to level up
			
			level = level+1 #adds 1 level to global variable
			
			level_up_check() #This is used to make sure code doesn't break and forget to level up player that can go up two levels at once 
			
			#Add drop type values to try and increase the variety of dropped items
			
	def fight_enemy():
		#CODE ENEMY FIGHTING
		#ADD XP
		level_up_check()
	
	def special_ability():
	
	def level_up_check(): #This will check to see if user has enough XP to go up in level
	
		required_xp = 0
		
		if level >=4: #sets XP cap at 1500 after level 4
			required_XP=1500
		else:	
			required_XP=250*(level+1) #designs XP increments 
			
		if XP>required_XP: #tests if level up is required 
			level_up(required_XP)
		else:
			break
			
	def boss_check(): #This checks to see if the player has moved enough spaces to go further in the adventure
		if steps => 10 && steps < 30:
			boss_fight()
		else if steps => 30 && steps < 60:
			boss_fight()
		else: 
			boss_fight()
			
	def boss_fight():
		if steps => 10 && steps < 30:
			#CODE FIRST BOSS
		else if steps => 30 && steps < 60:
			#CODE SECOND BOSS
		else: 
			#CODE FINAL BOSS
		
	def take_a_step():
		global steps #allows you to manipulate steps counter
		boss_check() #checks if you've earned a boss yet
		continue = input("Roll the die to determine your fate! [Press any key]")
		roll = randint(1,6) #rolls die
		steps = steps + roll #adds step counter
		fight_enemy() #fights an enemy
		drop_item() #drops item
		drop_item()
		
	def drop_item():
		#CODE ITEM DROP. USE PERCENTAGES
	
	
		
	