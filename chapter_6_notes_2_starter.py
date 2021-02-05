# Chapter 6 guided notes #2

# ENCAPSULATION
#   Helps keep code independent by hiding (or encapsulating) the
#   details. Variables(including parameters) created inside a
#   function cannot be directly accessed outside the function.

# 1: GLOBAL vs. LOCAL SCOPE
#   Scope defines the accessibility of separate parts of a program. Functions
#       have a local scope by default, which means variables (including parameters)
#       initialized within a function only exist within that particular function. 
#       Global variables initialized outside of functions are accessible throughout 
#       a program, and therefore have a global scope.
 
# Global Reach Example - demonstrates local and global variables

#   define functions

#   main program

input("\nPress the enter key to continue.")

# CHALLENGE: create a new function called make_omelette() that prints the ingredients
#   for an omelette. Pass in the ingredient(s) as a paramenter (local variable) and use a 
#   global ingredient (eggs) to make at least 2 different omelettes.



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
#print("Welcome!")
#score = grade_ave(80,90,85)
#print(score)

#   call main function

input("Press enter to continue.")

# 3: unlimited number of arguments
#   Certain functions(like print()) need to handle any number of arguments.
#   Use asterisk before parameter name; turns parameter into tuple of X length.

# CHALLENGE: Update the grade_ave() function to only have one
#   parameter so it can take in any number of student grades and return the 
#   average grade.


