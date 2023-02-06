# day 3 notes on functions
import random

# unlimited number of arguments
#	  Certain functions(like print() ) need to handle any number of arguments
#		Use asterisk before parameter name; turns parameter into a tuple of X length.

def grade_avg(*args):
	"""Calculates the average from any number of grades"""
	print("Tuple created from arguments:", args)
	total = 0
	for i in args:
		total += i
	grade_ave = total / len(args)
	return grade_ave

ave = grade_avg(80, 82, 84, 86, 88)
print("The grade average is:", ave)
print("The grade average is:", grade_avg(100,90, 80))

# default parameter values
#   you have the option to assign a default value, so that if no
#   value is passed to the function it will use the value assigned
#   trap: once you assign a default value to one parameter, you must assign one to all parameters.
def bday(name = "Missing", age = 0):
    """prints name and birthday"""
    print ("Wow", name, "you are", age, "years old!")
bday(age = 11, name = "Frank") # keyword arguments
bday("Heather", 36) # positional arguments
bday() # relying on default parameters
bday("Tim") # combining positional and default parameters


# can override default parameter at function call (using either positional or keyword arguments)
#  POSITIONAL ARGUMENTS - arguments passed in the same order as the parameters are specified
#  KEYWORD ARGUMENTS - arguments passed in a different order than the parameters are specified

# How might this be useful?
#   Imagine you are writing a battle() function for the Oregon Trail and want to assign the
#     potential enemy a default health of 100. You can use a default parameter for that.

import time
# globals
hero = "Link"
health = 100  

def battle(enemy_hp = 10):
	"""Allows a battle to occur between a hero and an enemy of any strength.
 	param - enemy_hp = the starting hp of the enemy we want to fight. Defaults to 10.
  	return - enemy's hp after the battle
	"""
	global health
	print(f"\n{hero} has encountered an enemy!")
	print("The enemy's hp is", enemy_hp)
	fight = input("Would you like to attack? (y or n): ").lower()
	if fight == "y":
		while enemy_hp > 0 and health > 0:
			print("\nYou swing and attack the enemy!")
			time.sleep(1)
			rand = random.randrange(3)
			if rand == 1:
				print("You miss and the enemy strikes you!")
				health -= 10
			else:
				print("You scored a direct hit!")
				enemy_hp -= 10
			print(f"\n{hero}'s health:{health}")
			print(f"Enemy's health:{enemy_hp}")
		if enemy_hp <= 0:
			print("\nThe enemy has been slain!")
		else:
			print(f"\n{hero} has been been tragically defeated...")
	return enemy_hp

# main
print("\nLet the battle commence!")

battle()  # battle a default enemy
battle(100)  # battle an equal strength enemy
battle(500)  # battle a boss enemy

print("\nThe battle is over!")
