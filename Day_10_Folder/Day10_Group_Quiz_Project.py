# Objective: To build a quiz game
# You'll be working in teams of 2 or 3 (or in our case it was 4)
# Consist of at least 5 questions
# Be multiple choice a, b, c etc
# Award a user 5 points for every correct answer, remove 2 points for every incorrect answer
# Show the total at the end with a relevant message

# Bonus Goals:
# Utilise Colorama Library
# Giving questions in a random order
# Allowing the user to play again at the end to see if they beat their last score

import random # random library
from colorama import Fore, Style # colour library

def questions():
    global score # can be accessed and moidfied across functions
    score = 0
    # list of questions and answers
    questions_and_answers = [
        ("How many dots appear on a pair of dice?\nA: 45\nB: 42\nC: 39", "b"),
        ("What is the tallest type?\nA: Oakwoods\nB: Sprucewood\nC: Redwoods","c"),
        ("What is acrophobia a fear of?\nA: Speeds\nB: Heights\nC: Spiders", "b"),
        ("Which year did the Titanic sink in the Atlantic Ocean?\nA: 1912\nB: 1909\nC: 1920", "a"),
        ("Which was Disney's first movie?\nA: Cinderella\nB: Tangled\nC: Snow White", "c"),
        ("Which alien creature in film has acid for blood?\nA: E.T\nB: Xenomorph\nC: Predator","b"),
        ("What is the chemical element with the symbol Fe?\nA: Zinc\nB: Copper\nC: Iron","c"),
        ("What is the national sport of Japan?\nA: Karate\nB: Sumo Wrestling\nC: Samurai","a"),
        ("What animal had the most powerful bite in the world?\nA: Nile Crocodile\nB: Freshwater Crocodile\nC: Salwater Crocodile","a"),
        ("Which State in America is the biggest?\nA: Alaska\nB: New York\nC: Texas","a")
        ]
    random.shuffle(questions_and_answers) # shuffles the list of questions and randomizes it
    for q, correct_answers in questions_and_answers: # loop
        # keeps asking the question until there is a valid answer
        while True:
            print (q)
            answer = input("Choose A, B or C: ").lower()
            if answer not in ["a", "b", "c"]:
                print ("-- PLEASE ANSWER A, B OR C! --")
            else:
                break

        # checks that the answer is correct or wrong and adds score
        if answer == correct_answers:
            score += 5
            print (Fore.GREEN + f"-- CONGRATUALTIONS YOUR SCORE IS NOW {score}! --" + Style.RESET_ALL) # GREEN
        else:
            score -= 2
            print(Fore.RED + f"-- INCORRECT YOUR SCORE IS NOW {score} --" + Style.RESET_ALL) # RED
    
    # shows final score and replay option
    while True:
        print(Fore.BLUE + f"Your final score is {score}" + Style.RESET_ALL) # BLUE
        retry = input("Would you like to try again? Y/N\n").lower() # replay option
        if retry == "y":
            questions()
        elif retry == "n":
            print("Thank you for playing!")
            break # ends loop
        else:
            print("Please pick an option.")

questions() # quiz starter