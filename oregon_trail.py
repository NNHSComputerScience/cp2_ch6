"""
Partner 1:
Partner 2:
Title: Oregon Trail
Description: Recreation of the aventure simulation game of traveling out west in 1800's.
"""
import random

# -----------------------------------------------------------
# Help Text -- global variables that contain helper text to display in game (don't edit)
# -----------------------------------------------------------
welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel (t) - moves you randomly between 30-60 miles and takes 3-7 days (random).
  rest   (r) - increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
  hunt   (h) - adds 100 lbs of food and takes 2-5 days (random).

You can also enter one of these commands without using up your turn:

  status (s) - lists food, health, distance traveled, and day.
  help   (?) - lists all the commands.
  quit   (q) - will end the game.
"""

good_luck_text = "\nGood luck, and see you in Oregon!"

# -----------------------------------------------------------
# FUNCTION DEFINITIONS -- beginning of function definitions; see comments explaining each function above each function header
# -----------------------------------------------------------
# first function is done for you!
def handle_invalid_input(response):
    """Displays a helpful response if the player inputs an invalid command."""
    print("'{0}' is not a valid command. Try again.".format(response))

# Converts a numeric date into a string.
# inputs: a month in the range 1-12 and a day in the range 1-31
# output: a string like "December 24".
# Note: this function does not enforce calendar rules. It's happy to output impossible strings like "June 95" or "February 31"
def date_as_string(m, d):
	"""converts a numeric date to a string"""
	date_string = NAME_OF_MONTH[m] + " " + str(d)
	return date_string

# output: miles remaining until Oregon
# hint: What global variables could you use to help achieve this?
def miles_remaining():
    pass # Enter your code here

# print a player's current status on the journey, including food remaining, health level, distance traveled, distance remaining, and date
def handle_status():
	pass

# prints the help text
def handle_help():
    pass

# enforces what happens when a player decides to quit in the middle of a game
def handle_quit():
    pass

# Returns the number of days in the month (28, 30, or 31).
# input: an integer from 1 to 12. 1=January, 2=February, etc.
# output: the number of days in the month. If the input is not in the required range, returns 0.
def days_in_month(m):
	pass

# Repairs problematic values in the global (month, day) model where the day is larger than the number of days in the month. If this happens, advances to the next month and knocks the day value down to 1 accordingly. Knows that different months have different numbers of days. Return True if the global month/day values were altered, else return False.
def maybe_rollover_month():
	pass

# decreases the food for 1 elapsed day
def consume_food():
	pass

# enforces rules for what happens when a sickness occurs
def handle_sickness():
	pass

# enforces the game rules for what happens if a player decides to hunt
def handle_hunt():
	pass

# Calculates whether a sickess occurs on the current day based on how many days remain in the month and how many sick days have already occured this month. If there are N days left in the month, then the chance of a sick day is either 0, 1 out of N, or 2 out of N, depending on whether there have been 2 sick days so far, 1 sick day so far, or no sick days so far.
# This system guarantees that there will be exactly 2 sick days each month, and incidentally that every day of the month is equally likely to be a sick day
def random_sickness_occurs():
	pass

# Causes a certain number of days to elapse. The days pass one at a time, and each day brings with it a random chance of sickness. The sickness rules are quirky: player is guaranteed to fall ill a certain number of times each month, so illness needs to keep track of month changes.
# input: an integer number of days that elapse.
def advance_game_clock():
	pass

# enforces the game rules for what happens if a player decides to travel
def handle_travel():
	pass

# enforces the game rules for what happens if a player decides to rest
def handle_rest():
    pass

# returns True if the player wins, otherwise returns False
def player_wins():
    pass

# returns True if the game is over, otherwise returns False
def game_is_over():
    pass

# ---------------------------------------------------------
# Game Constants -- global variable constants that define the rules of the game, and which don't change.
# ---------------------------------------------------------
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_MISSOURI_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
    'fake', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]

# -----------------------------------------------------------
# Game State -- global variables that collectively represent the state of the game
# -----------------------------------------------------------
miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
sicknesses_suffered_this_month = 0
player_name = None

# -----------------------------------------------------------
# UNIT TESTS -- Write any unit tests here (for testing purposes only).
#	Call the unit test function from the top of the main function 
#	if you want to test, otherwise comment out the call to the tests.
#	This is not required, but a good idea.
# -----------------------------------------------------------
def unit_tests():
	"""Function to write unit tests for testing other functions"""
	pass

# -----------------------------------------------------------
# MAIN GAME -- beginning of the main game code
#		You should not change any global variables in this function.
# -----------------------------------------------------------
def main():
	global player_name
	#unit_tests()  # uncomment when testing your unit test(s)
	playing = True

	print(welcome_text + help_text + good_luck_text)
	player_name = input("\nWhat is your name, player? ").title()

	handle_status()
	while playing:
		print()
		action = input("\nChoose an action, {0} --> ".format(player_name))
		if action == "travel" or action == "t":
			if food_remaining <= 49:
				print("You have", food_remaining, "food remaining. You must hunt for food before travelling any further.")
			else:
				handle_travel()
		elif action == "rest" or action == "r":
			if health_level > 4:
				print("You have", health_level, "health remaining out of", MAX_HEALTH, "possible. Choose another option.")
			else:
				handle_rest()
		elif action == "hunt" or action == "h":
			handle_hunt()
		elif action == "quit" or action == "q":
			handle_quit()
		elif action == "help" or action == "?":
			handle_help()
		elif action == "status" or action == "s":
			handle_status()
		else:
			handle_invalid_input(action)

		if game_is_over():
			playing = False

	if player_wins():
		print("\n\nCongratulations you made it to Oregon alive!\n")
		handle_status()
		print("""\n
			__   __              _    _  _         _ 
			\ \ / /             | |  | |(_)       | |
			 \ V / ___   _   _  | |  | | _  _ __  | |
			  \ / / _ \ | | | | | |/\| || || '_ \ | |
			  | || (_) || |_| | \  /\  /| || | | ||_|
			  \_/ \___/  \__,_|  \/  \/ |_||_| |_|(_)
			""")

	else:
		print("\n\nAlas, you lose...\n")
		handle_status()
		print("""\n
			 _____                        _____                
			|  __ \                      |  _  |               
			| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
			| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
			| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
			 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
			""")
#main()
