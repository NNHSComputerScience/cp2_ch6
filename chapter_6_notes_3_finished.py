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

def battle(enemy_hp = 100):
	"""a battle between a player and an enemy"""
	pass

battle()
battle(50)
battle(1000)

# CHALLENGE: create a new function called make_omelette() that prints the ingredients for an omelette. 
#   Pass in unlimited ingredient(s) as a paramenter (local variable) and use a global ingredient (eggs) 
#   to make at least 2 different omelettes with different ingredients. In the function, print all the ingredients
#   in the omelette using a for loop.

eggs = "Eggs" # global ingredient

def make_omelette(*ingredients):  # paramenter defines an unlimited number of local ingredients
	print("\nYou made an omelette with:\n" + eggs)
	for ing in ingredients:
		print(ing)

make_omelette("Peppers", "Onion", "Tomatoes")
make_omelette("Cheese", "Bacon")
make_omelette("Fritos", "Olives", "Fish", "Toothpaste")
