# Chapter 6 notes #1: Functions Intro

# Python lets you create your own functions.
# A FUNCTION is a reusable block of code that performs a specific task.
#   Functions allow you to abstract away unneccessary information and leverage modular design.

#  ABSTRACTION is hiding all but the most relevant details. 
#   Lets you think about the big picture without worrying about the details.
#   e.g. variable or function names are an abstraction of their actual contents.

# 1: Creating a function is reffered to as
#    "Defining a Function"

# entire function is called the FUNCTION DEFINITION
def function():  # first line is the FUNCTION HEADER
    print ("Hello, I'm a function!\n")

# 2: Using a function is referred to as 
#    "Calling a function", or a FUNCTION CALL

function()
print(function())   # returns 'None'

# 3: DOCSTRING. A special way to document a function;
#    It must be triple quoted (single or double), and on the first line after the function header. 
#    Can provide useful information when attempting to use the function.

def greeting():
    """This will greet the user to a program"""
    print("\nWelcome to the program!")

greeting()
help(greeting) # help function is one way to see documentation for a function
help(len)

# 4: PARAMETERS: Variable names inside the parentheses of a
#      function header. A function recieves a value through its
#      parameters. Parameters catch values sent to the function
#      from a function call. 
#    ARGUMENTS: Values sent to a function to use. (put in parentheses of a 
#      function call)
#   *note: These terms are sometimes used interchangably, but we will stick to these strict definitions for this class.

def display(message):   # message is a parameter
    print (message)

display("Here is a message for you.\n") # the string "Here is a message for you.\n" is an argument

# Trap... If I define a function with one parameter, then I must
#       use the same number of arguments when calling the function

# display() ERROR
# display("Hi", "Jake") ERROR

# 5: You can have multiple parameters:

def display2(message, name):
    print (message, name)

name1 = input("Name: ").title()
display2("Here is a message for you", name1) # arguments sent and assigned by position
# display2("Here is a message for you") is an ERROR


# 6: RETURNING.  You can get value(s) out of a function by returning value(s). 
#   A RETURN VALUE is a value recieved back from a funciton call.
#    You can return a value from a function by using
#    a RETURN STATEMENT. A function always ends after
#    executing a return statement, and the RETURN VALUE is returned.

def give_me_five():
    return 5
    print("test") # unreachable code (function ends after the return statement)

number = give_me_five()
print ("Return value: ", number)

# A function can return any type of value, but only one value at a time
def give_me_ten():
    lefthand= 5
    righthand= 5
    return (lefthand, righthand) # tuple

return_value = give_me_ten() 
number1, number2 = return_value # unpack tuple into its elements
print("Return value:", return_value)
print("Left", number1)
print("Right", number2)

# CHALLENGE: Can you define a function that can simulate
#           the rolling of two dies and return both values?
# CHALLENGE 2: Create a new function to add your two die rolls
#           together and return the total.

import random

# define all functions at the top of your program:
def dub_roll():
    '''Generates a double die roll and returns it as a tuple'''
    die1 = random.randint(1,6)
    die2 = random.randrange(1,7)
    return (die1, die2)

def add_2(num1, num2):
    '''adds two number together and returns the total'''
    total = num1 + num2
    return total

# use all functions below in your main code
roll1, roll2 = dub_roll()
roll3, roll4 = dub_roll()

print("The first roll is",roll1,"and the second is",roll2)
print("The first roll is",roll3,"and the second is",roll4)

tot = add_2(roll1, roll2)
tot2 = add_2(roll3, roll4)

print("\nThe total of rolls 1 & 2 is", tot)
print("\nThe total of rolls 3 & 4 is", tot2)


input("Press enter to exit.")
