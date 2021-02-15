# day 3 notes on functions

# unlimited number of arguments
#   Certain functions(like print()) need to handle any number of arguments.
#   Use asterisk before parameter name; turns parameter into tuple of X length.

def grade_ave(*args):
    """Calculates the average from any number of grades"""
    print ("Tuple created from arguments:", args) 
    total=0
    for i in args:
        total+=i
    grade_ave= total/len(args)
    return grade_ave

print(grade_ave(80, 82, 88, 90))
print(grade_ave(60, 70, 80, 90, 100))

# CHALLENGE: create a new function called make_omelette() that prints the ingredients
#   for an omelette. Pass in unlimited ingredient(s) as a paramenter (local variable) and use a 
#   global ingredient (eggs) to make at least 2 different omelettes with different ingredients.

eggs = "Eggs" # global ingredient

def make_omelette(*ingredients): # parameter defines local ingredients
    """Makes omelettes using both local and global variable ingredients and"""
    print("\nYou made an omelette with:\n" + eggs)
    for i in ingredients:
        print(i)
    
make_omelette("Peppers", "Onion", "Tomatoes")
make_omelette("Cheese", "Broccoli", "Fritos")


# default parameter values
#   you have the option to assign a default value, so that if no
#   value is passed to the function it will use the value assigned
#   trap: once you assign a default value to one parameter,
#   you must assign one to all parameters.
def bday(name="Missing", age=0):
    """prints name and birthday"""
    print ("Wow", name, "you are", age, "years old!")
bday()

#can override default with call (positional or keyword arguments)
bday("Matt",33)
bday("Matt")  # default parameters allow you to omit arguments from the function call
# bday()  # still required to send other arguents not asssigned a default value
bday(age = 33, name = "Frank") # keyword arguments allow you to pass arguments out of position

# How might this be useful?
#   Imagine you are writing a battle() function and want to assign the
#     enemy a default health of 100. You can use a default parameter for that.

import time, random

def battle(enemy_hp = 100): # enemy has full health by default (100)
    """a battle between a player and an enemy"""
    global hp
    flee = False
    while True:
        time.sleep(1)
        print("Player health:", hp, "\nEnemy health:", enemy_hp)
        hp -= 10
        enemy_hp -= 50
        flee = True
        if flee:
            break
    return enemy_hp

# global scope
hp = 100  # player starting health level

e_hp = battle() # enemy may still be alive!

print("Player health outside function:", hp, "\nEnemy health outside function:", e_hp)

if 
e_hp = battle(e_hp)

print("Player health outside function:", hp, "\nEnemy health outside function:", e_hp)
