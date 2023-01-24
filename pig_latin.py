
# pig-latin generator
# pig_latin.py
# Gets a list of words from the user, converts them all to pig-latin, and print them out in
#   alphabetical order and in columns.

def inputs():
    """Generates a list of words to and returns it"""
    words = [] # initialize list
    word = input("\nEnter a word (leave blank to end): ").lower()
    while word: # keep getting new words and adding to list if user enters a word
        words.append(word)
        word = input("Enter a word (leave blank to end): ").lower()
    return words # return list of words

# ----------------------------------------------------------------------

def translate(orig_list): # takes in an original list of words
    """Takes in a list of words and returns a list of the words in pig-latin"""
    pig_list = [] # list of pig-latin translations
    for i in orig_list: # loop through original list, translate each word, & add to pig list
        letter = i[0]
        new_word = i[1:] + letter
        pig_list.append(new_word)
    return pig_list # return new list of pig-latin words

# ----------------------------------------------------------------------
                
def display(list1, list2): # takes in original list and pig-latin list
    """Prints the original words next to the pig-latin words"""
    print("\nOrig Word\tPig-Latin")
    for i in range(len(list1)): # prints two list in columns
        print(list1[i], "\t\t", list2[i])

# ----------------------------------------------------------------------

def main():
    """Runs main program"""
    input("Welcome to the pig-latin word generator.  Press enter to begin. ")
    again = "y"
    while again == "y":
        orig_list = inputs() # gets and stores list of original words
        orig_list.sort()    # sorts original list into alphabetical order
        new_list = translate(orig_list) # traslates original list and stores new pig-latin list
        display(orig_list, new_list) # prints 2 lists in columns
        again = input("\nWould you like to try again? (y or n) ").lower()
    input("\nPress enter to exit.")

# ----------------------------------------------------------------------

main()
Displaying pig_latin.py (with comments).
