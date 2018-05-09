from random import randint
import math
import sys

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
current_HP = 0
current_stamina = 0
#these are global variables

def main():
	global name
	enemy_options()
	name=input("Welcome brave warrior! What is your " + name + "?")
	print("Your quest is to battle to the great beyond and retrieve what may lie there. The people of this hard drive believe there to be great riches which control these lands.")
	character_creation()
	print("Ah! Thank you " + name +" the mighty " + character)
	print("Your brave journey will first take you through this computers invisible folders. Be warned the path is treacherous and many have deleted vital files never to be seen again")
	print("Once through these folders you may come across a theme park of disk fragmentation. From here you may be tempted to wander through many-a application and plenty of shiny bits and bobbles. Deep in the core is where you seek.")
	print("Down the rabbithole you fall. To find the treasures this harddrive holds you must finally saunter the tombs of data past in the fiery holes of the recycling bin!")
	print("Safe travels, " + name + ".")
		
	while steps < 60:
		take_a_step()
			
	
	print("Congratulations on your journey, " + name + "!")
	print("You've fought long and hard. You've even made it all the way to level " + level + "!")
	print("What a proud " + character + " you must be!")
	print("You've collected lots of items and battled fearlessly along the way.")
	print("Through this effort and riches you've scored " + score() + " points! To travel again just re-run this code!")

	def character_creation():
	
		print("You may pick a character type. Each type has different base stats.")
		print("/n Your options are: Mage, Elf, Goblin, Human, or Fairy")
		print("/n A Mage has a base HP + Stamina of 5, a base Wisdom of 3, and 1 for all other stats. Their special ability is a 25% chance of obtaining an extra move roll.")
		print("/n An Elf has a base HP of 10, Stamina, Charisma, and Dexterity of 5, Wisdom of 3, Strength of 2, and 1 for all other stats. Their special ability is a 10% chance of avoiding battle.")
		print("/n A Goblin has a base HP and Strength of 5, Stamina of 10, Defense of 2, and 0 for all other stats. Their special ability is the option to intimidate weaker [1/2 of their HP or lower] enemies from battle.")
		print("/n A Human has a base HP and Stamina of 5, a Defense of 0, and 1 for all other stats. Their special ability is regaining 1 stamina per turn.")
		print("/n A Fairy has a base HP of 5,  Stamina of 10, Dexterity of 3, Strength of 0, and 1 for all other stats. Their special ability is regaining 1 HP per turn.")
		
		while character == "None": #This while loop makes the player re-pick whenever they don't have a character
			global character
			character= input("Please pick your character type. Type "Mage, Elf, Goblin, Human, or Fairy" : ")
	
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
		global current_HP
		global current_stamina
		
		#maybe put this in some sort of data organizer like a hashmap or array
		if character == "Mage":
			HP = 5
			current_HP = HP
			Stamina = 5
			current_stamina = Stamina
			Intelligence = 1
			Wisdom = 3
			Luck = 1
			Strength = 1
			Defense = 1
			Charisma = 1
			Dexterity = 1
		else if character == "Elf":
			HP = 10
			current_HP = HP
			Stamina = 5
			current_stamina = Stamina
			Intelligence = 1
			Wisdom = 3
			Luck = 1
			Strength = 2
			Defense = 1
			Charisma = 5
			Dexterity = 5
		else if character == "Goblin":
			HP = 5
			current_HP = HP
			Stamina = 10
			current_stamina = Stamina
			Intelligence = 0
			Wisdom = 0
			Luck = 0
			Strength = 5
			Defense = 2
			Charisma = 0
			Dexterity = 0
		else if character == "Human":
			HP = 5
			current_HP = HP
			Stamina = 5
			current_stamina = stamina
			Intelligence = 1
			Wisdom = 1
			Luck = 1
			Strength = 1
			Defense = 0
			Charisma = 1
			Dexterity = 1
		else if character == "Fairy":
			HP = 5
			current_HP = HP
			Stamina = 10
			current_stamina = Stamina 
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
		enemies = []
		enemies.add(1, "Mud Monster", 0,0)
		enemies.add(2, "Random Solider", 3, 1)
		enemies.add(3, "hyperMouse Ninja",10,2)
		enemies.add(4, "Mole People",5,1)
		enemies.add(5, "Gargoyle",2,5)
		
	def item_options(): #these items need to be recoded as objects 
	
		drop_items_food = []
		
		# Item ID, Name, Description, Worth in Gold, Drop Percent
	
		drop_items_food.add(1, "Potion", "This adds 5 HP", 1, 35)
		drop_items_food.add(2, "Hyper Potion", "This adds 10 HP", 2, 15)
		drop_items_food.add(3, "Super Potion", "This adds 20 HP", 5, 5)
		drop_items_food.add(4, "Apple", "This adds 5 Stamina", 2, 35)
		drop_items_food.add(5, "Chocolate Bar", "This adds 10 Stamina", 5, 15)
		drop_items_food.add(6, "Fruit Smoothie", "This adds 10 Stamina and 5 HP", 7, 10)
		drop_items_food.add(7, "Chicken Breast", "This adds 20 Stamina" 7, 10)
		drop_items_food.add(8, "Avocado Toast", "This adds 5 Stamina and 5 HP. It also increases your Wisdom by 1", 10, 5)
		
		drop_items_armor = []
		
		#Item ID, Item Type ID to determine equipability, name, description, worth in gold, drop percentage
		drop_items_armor.add(1, 1, "Basic Chest Armor", "Adds 2 defense when equipped", 1, 30)
		drop_items_armor.add(2, 1, "Advance Chest Armor","Adds 5 defense and subtracts 2 strength when equipped", 3, 20)
		drop_items_armor.add(3, 2, "Basic Sword", "Adds 2 attack when equipped",  1, 30)
		drop_items_armor.add(4, 2, "Advance Sword", "Adds 5 attack when equipped", 3, 20)
		drop_items_armor.add(5, 3, "Basic Shield", "Adds 1 to defense and subtracts 1 from strength when equipped", 1, 30)
		drop_items_armor.add(6, 3, "Advance Shield", "Adds 2 to defense, subtracts 1 from strength, and subtracts 2 from dexterity", 3, 20)
		drop_items_armor.add(7, 4, "Basic Crossbow", "Adds 5 to attack when equipped", 3, 20)
		drop_items_armor.add(8, 4, "Advance Crossbow", "Adds 12 to attack and subtracts 2 from strength when equipped", 10, 10)
		drop_items_armor.add(9, 5, "Basic Helmet", "Adds 1 to defense when equipped", 1, 15)
		drop_items_armor.add(10, 5, "Advance Helmet", "Adds 3 to defense and 1 to stamina when equipped", 2, 20)
		drop_items_armor.add(11, 6, "Basic Leggings", "Adds 1 defense when equipped", 1, 30)
		drop_items_armor.add(11, 6, "Advance Leggings", "Adds 3 defense and subtracts 1 dexterity when equipped", 3, 20)
		drop_items_armor.add(12, 7, "Chainmail", "Extra underbody armour. Add 1 to defense when equipped", 1, 30)
			
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
		global current_HP
		enemy_type = randint(1,5)
		enemy_HP = (random.randint(character_level,character_level*3))
		enemy_current_HP = enemy_HP
		xp_worth = (random.randint(hp*1.5,hp*2.5))
		enemy_name = enemies.get(enemy_type[2])
		enemy_stamina = enemies.get(enemy_type[3])
		enemy_defense = enemies.get(enemy_type[4])
		
		while enemy_current_HP> 0:
			if current_HP <= 0: #checks to make sure player isn't dead
				print("You died. Feel free to try again.")
				sys.exit()
			else:
				if current_stamina <=0:
					special_ability() #checks for characters special ability
					print("You can't attack! You need more stamina!)
					equip_item() #allows user to use item to get more stamina
					print("The " + enemy_name + " is attacking you!")
					current_HP = current_HP - (enemy_attack-defense)
					enemy_stamina = enemy_stamina-1
					print("You've lost " + enemy_attack-defense + " HP. Your foes current stamina is " + enemy_stamina)
				else:
					if enemy_stamina <=0:
						print("The enemy can no longer fight!")
						print("You attacked the " + enemy_name + "!")
						enemy_current_HP = enemy_current_HP - (attack-enemy_defense)
						print("You attacked for " + attack-enemy_defense + " HP! Lost 1 Stamina")
						current_stamina = current_stamina-1
					else:
						special_ability() #checks for characters special ability
						print("You attacked the " + enemy_name + "!")
						enemy_current_HP = enemy_current_HP - (attack-enemy_defense)
						print("You attacked for " + attack-enemy_defense + " HP! Lost 1 Stamina")
						current_stamina = current_stamina-1
						print("The " + enemy_name + " is attacking you!")
						current_HP = current_HP - (enemy_attack-defense)
						enemy_stamina = enemy_stamina-1
						print("You've lost " + enemy_attack-defense + " HP. Your foes current stamina is " + enemy_stamina)
		
		XP = XP + xp_worth
		level_up_check()
	
	def special_ability():
		if character = "Mage":
		
		else if character = "Elf":
		
		else if character = "Human":
		
		else if character = "Goblin":
		
		else: #this one is if fairys exist
		
	
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
			
	def get_Item_Name(int id):
		if id == 1:
			return "Potion"
		else if id == 2:
			return "Super Potion"
		
	def take_a_step():
		global steps #allows you to manipulate steps counter
		boss_check() #checks if you've earned a boss yet
		continue = input("Roll the die to determine your fate! [Press any key]")
		special_ability() #checks for special ability ==some characters can get extra rolls==
		roll = randint(1,6) #rolls die
		steps = steps + roll #adds step counter
		fight_enemy() #fights an enemy
		drop_item() #drops item
		drop_item()
		equip_item()
		
	def drop_item():
		#CODE ITEM DROP. USE PERCENTAGES
	
	
	def score():
		score = 0
		score = XP + score + level + inventory_count + current_HP
		
		return score
		
	def equip_item():	
		answer = input("Would you like to equip/unequip or use an item? (E or U or N")
		while answer != N:
			item = input("Please enter the item you would like to equip or use")
			if inventory.get(item):
			
			else if equip.get(item):
				
			else:
				print("That item is not in your inventory")
			answer = input("Would you like to equip or use an item? (Y or N")
	
	
	#TO DO 
	# Code Database online to store Scores
	# Add Inventory Table to store items
	