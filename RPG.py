from random import randint
import math
import sys

import game_config

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



def character_creation():

	global character
	print("You may pick a character type. Each type has different base stats.")
	print("/n Your options are: Mage, Elf, Goblin, Human, or Fairy")
	print("/n A Mage has a base HP + Stamina of 5, a base Wisdom of 3, and 1 for all other stats. Their special ability is a 25% chance of obtaining an extra move roll.")
	print("/n An Elf has a base HP of 10, Stamina, Charisma, and Dexterity of 5, Wisdom of 3, Strength of 2, and 1 for all other stats. Their special ability is a 10% chance of avoiding battle.")
	print("/n A Goblin has a base HP and Strength of 5, Stamina of 10, Defense of 2, and 0 for all other stats. Their special ability is the option to intimidate weaker [1/2 of their HP or lower] enemies from battle.")
	print("/n A Human has a base HP and Stamina of 5, a Defense of 0, and 1 for all other stats. Their special ability is regaining 1 stamina per turn.")
	print("/n A Fairy has a base HP of 5,  Stamina of 10, Dexterity of 3, Strength of 0, and 1 for all other stats. Their special ability is regaining 1 HP per turn.")

	while character == "None": #This while loop makes the player re-pick whenever they don't have a character
		character=input("Please pick your character type. Type 'Mage, Elf, Goblin, Human, or Fairy' : ")

		character_stats(character)

		# Could soft code these values, but I hard coded them to put them in a particular order based off HP/Stamina priority and highest to weakest
		# Maybe put the stats printer in a separate method? To just print stats. Maybe even code 'hot keys' to print certain character stats VS all at once?

def character_stats():
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
	elif character == "Elf":
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
	elif character == "Goblin":
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
	elif character == "Human":
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
	elif character == "Fairy":
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



def level_up(which_level):

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

	for i in range(3): #for loop that reiterates 3 times
		trait = randint(3,9)

		if trait == 3:
			Intelligence = Intelligence + randint(1,3)
		elif trait ==4:
			Wisdom = Wisdom + randint(1,3)
		elif trait ==5:
			Luck = Luck + randint(1,3)
		elif trait == 6:
			Strength = Strength + randint(1,3)
		elif trait == 7:
			Defense = Defense + randint(1,3)
		elif trait == 8:
			Charisma = Charisma + randint(1,3)
		else:
			Dexterity = Dexterity + randint(1,3)

		XP = which_level-XP #subtracts XP used to level up

		level = level+1 #inserts 1 level to global variable

		level_up_check() #This is used to make sure code doesn't break and forget to level up player that can go up two levels at once

		#insert drop type values to try and increase the variety of dropped items

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
				print("You can't attack! You need more stamina!")
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
	global steps
	global current_stamina
	if character == "Mage":
		roll = randint(1,4)
		if roll == 1:
			roll_die = randint(1,6)
			steps = steps+roll_die
			print("You inserted extra spaces!!!")
		else:
			print("Nothing happened")

	elif character == "Elf":
		roll == randint(1,10)
		if roll == 1:
			print("You skip this battle!")

		else:
			print("Nothing happened")
	elif character == "Human":
		current_stamina = current_stamina+1
	elif character == "Goblin":
		if enemy_HP <= current_HP*.5:
			print("You intimidated your opponent!")
		else:
			print("Nothing happened")
	else: #this one is if fairys exist
		current_HP = current_HP+1


def level_up_check(): #This will check to see if user has enough XP to go up in level

	required_xp = 0

	if level >=4: #sets XP cap at 1500 after level 4
		required_XP=1500
	else:
		required_XP=250*(level+1) #designs XP increments

	if XP>required_XP: #tests if level up is required
		level_up(required_XP)
	else:
		required_xp = 0

def boss_check(): #This checks to see if the player has moved enough spaces to go further in the adventure
	if steps >= 10 & steps < 30:
		boss_fight()
	elif steps >= 30 & steps < 60:
		boss_fight()
	else:
		boss_fight()

def boss_fight():
	if steps >= 10 & steps < 30:
		#CODE FIRST BOSS
		print("You've fought hard through the unknown and up ahead you see your gate")
		print("A creature fades in and out of existence. You can't make out much before you see flashing jaws lunge to attack you!")

		#Is there a way to overwrite code in the fight sequence? Or should I make a new method for each boss fight?

		print("You have defeated the dreaded ghostly foe and pass the gate into the Land of Disk Fragments")
	elif steps >= 30 & steps < 60:
		#CODE SECOND BOSS
		print("To your left a roller coaster whizzes by, and on your right you spot a tilt-a-whirl spinning your E Drive's contents.  Further down the center a hole in the ground opens up. The recycling bin. The coast looks clear so you step forward.")
		print("Your toes feel the edge of hole when a force pulls you back. A gruesome clown grins his teeth. Bits of disk protruding out of his body.")
	else:
		#CODE FINAL BOSS
		print("The harddrive glimmers below a pool of backlog. Your time has come. You reach toward the pool when a shadow overtakes the clear waters(?) The recycling bin was not quite as empty as you thought.... The conglomeration grabs hold of your wrist with it's folder fingers and application icon biceps and drags you beneath the depth.")



def take_a_step():
	global steps #allows you to manipulate steps counter
	boss_check() #checks if you've earned a boss yet
	continue_check=input("Roll the die to determine your fate! [Press any key]")
	special_ability() #checks for special ability ==some characters can get extra rolls==
	roll = randint(1,6) #rolls die
	steps = steps + roll #inserts step counter
	fight_enemy() #fights an enemy
	drop_item() #drops item
	drop_item()
	equip_item()

def drop_item():
	print("TO DO")
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
			break

		elif equip.get(item):
			break
		else:
			print("That item is not in your inventory")
		answer = input("Would you like to equip or use an item? (Y or N")


def main():
	global name

	game_objects = game_config.setup()   # A dictionary of things in the game, organized by type
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




if __name__ == "__main__":
	main()
