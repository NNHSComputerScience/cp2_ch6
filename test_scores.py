# Test Scores Program
# test_scores_finished.py
# This program with calculate the average from a series of test scores.

# define functions
def inputs():
    scores_list = []
    score = float(input("What is the first test score? "))
    scores_list.append(score)
    while score != "e":
        score = input("What is the next test score? (press 'e' to exit) ")
        if score != "e":
            scores_list.append(float(score))
    return scores_list

def calculations(scores):
    total = 0
    for i in scores:
        total += i
    total /= len(scores)
    return total

def display(test_scores, avg):
    for i in test_scores:
        print("Test score #" + str(test_scores.index(i)+1), i)
    print("The average of all scores is:", avg)
           
# main
def main():
    print("Welcome to the Test Scores program!")
    more = "y"

    while more == "y":
        grades_list = inputs()
        average_grade = calculations(grades_list)
        display(grades_list, average_grade)
        more = input("Are there any more students to enter? (y or n): ").lower()

    input("Press enter to exit.")

main()




