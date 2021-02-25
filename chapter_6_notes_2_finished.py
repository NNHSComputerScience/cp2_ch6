# Chapter 6 notes #2

# SCOPE defines the accessibility of separate parts of a program. Functions
#       have a local scope by default, which means variables (including parameters)
#       initialized within a function are LOCAL VARIBALES, and only exist within that particular function.

def demo_local(param1, param2):
    """function to demonstrate local variables"""
    local1 = "toast"
    print("Local parameter 1:", param1)
    print("Local parameter 2:", param2)
    print("Local variable 1:", local1)
    return (param1, param2, local1)

demo_local("butter", "jelly")
#print(local1) # variables are not defined outside the function (i.e. they don't exist!)
#print(param1)
#print(param2)

# if you need to access information from within a function, you are in need of an output, or return value.
v1, v2, v3 = demo_local("butter", "jelly")
print("Returned values from the 'demo_local' function:", v1, v2, v3)

# GLOBAL vs. LOCAL SCOPE
#       GLOBAL VARIABLES initialized outside of functions are accessible throughout 
#       a program, and therefore have a global scope.
 
# Global Reach Example - demonstrates global variable access
# INSTRUCTOR NOTE: write the main and function headers first and then implement the functions

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

# INSTRUCTOR NOTE: Peer Instruction Questions #5 & #6
    
# main program 
value = 10 # value is a global variable because we're in the global scope here
print("In the global scope, value has been set to:", value, "\n")

read_global() #prints the global variable
print("Back in the global scope, value is still:", value, "\n")

shadow_global() #creates and prints the local variable 'value' with a value of -10
print("Back in the global scope, value is still:", value, "\n")

change_global() # changes the global variable to -10 and prints it
print("Back in the global scope, value has now changed to:", value)

# ENCAPSULATION - Keeps code logically independent by ‘hiding’ information from other parts of a program.
#  Functions should be written to leverage encapsulation and therefore only rely on local variables (if possible).

input("Press enter to continue.")

# MAIN FUNCTION
#   encapsulates main program

#   define functions first
def grade_ave(scores):
    """Calculates the average from a list of grades"""
    total = 0
    for grade in scores:
        total += grade
    return total / len(scores)

#   define main function next
def main(): # will never have any parameters
    """Runs main program"""
    print("Welcome!")
    ave_score = grade_ave([80,90,85])
    print(ave_score)

#   call main function last
main() # will never use any arguments

# INSTRUCTOR NOTE:  Run in Python Visualizer - http://pythontutor.com/visualize.html
#                   Peer Instruction Questions #7 & #8

