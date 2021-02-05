# day 3 notes on functions
import random

# default parameter values
#   you have the option to assign a default value, so that if no
#   value is passed to the function it will use the value assigned
#   trap: once you assign a default value to one parameter, you must assign one to all parameters.
def bday(name, age):
    """prints name and birthday"""
    print ("Wow", name, "you are", age, "years old!")
bday()

#can override default parameter at funciton call (using either positional or keyword arguments)


# How might this be useful?
#   Imagine you are writing a battle() function and want to assign the
#     enemy a default health of 100. You can use a default parameter for that.
