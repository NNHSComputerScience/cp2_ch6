# Chapter 6 guided notes #2



# 1: GLOBAL vs. LOCAL SCOPE
#   Scope defines the accessibility of separate parts of a program. Functions
#       have a local scope by default, which means variables (including parameters)
#       initialized within a function are LOCAL VARIBALES, and only exist within that particular function.
#       GLOBAL VARIABLES initialized outside of functions are accessible throughout 
#       a program, and therefore have a global scope.
 
# Global Reach Example - demonstrates local and global variables
#   define functions
def read_global():
    """Accessing a global variable from inside a function"""
    print("From inside the local scope of read_global(), value is:", value)

# Shadowing - When a local variable has the same name as a global variable we say that the local shadows the global. 
#  A shadow means that the global variable cannot be accessed by Python because the local variable will be found first. 
#  This is another good reason not to use global variables. 
def shadow_global():
    """Creating a local copy of the global variable name""" 
    value = -10 # using the same variable name is not encouraged to avoid this!
    print("From inside the local scope of shadow_global(), value is:", value)
  
def change_global():
    """Changing a global variable from inside a function (not encouraged)"""
    global value
    value = -10
    print("From inside the local scope of change_global(), value is:", value)

# main program WRITE THIS PART FIRST TOGETHER AND THEN WRITE FUNCTIONS
value = 10 # value is a global variable because we're in the global scope here
print("In the global scope, value has been set to:", value, "\n")

read_global() #prints the global variable
print("Back in the global scope, value is still:", value, "\n")

shadow_global() #creates and prints the local variable 'value' with a value of -10
print("Back in the global scope, value is still:", value, "\n")

change_global() # changes the global variable to -10 and prints it
print("Back in the global scope, value has now changed to:", value)

input("\nPress the enter key to continue.")

# CHALLENGE: create a new function called make_omelette() that prints the ingredients
#   for an omelette. Pass in the ingredient(s) as a paramenter (local variable) and use a 
#   global ingredient (eggs) to make at least 2 different omelettes.

eggs = "Eggs" # global ingredient

def make_omelette(*ingredients): # parameter defines local ingredients
    """Makes omelettes using both local and global variable ingredients"""
    print("\nYou made an omelette with:\n" + eggs)
    for i in ingredients:
        print(i)
    
make_omelette("Peppers", "Onion", "Tomatoes")
make_omelette("Cheese", "Broccoli", "Fritos")

input("Press enter to continue.")

# 2: main function
#   encapsulates main program

#   define functions
def grade_ave(score1, score2, score3):
    """Calculates the average of 3 grades"""
    total = score1 + score2 + score3
    grade_ave = total/3
    return grade_ave

#   define main function
def main(): # will never have any parameters
    """Runs main program"""
    print("Welcome!")
    score = grade_ave(80,90,85)
    print(score)

#   call main function
main() # will never use any arguments
