# Objective: Using the code provided in the presentation, use ChatGPT to expand and complete the program.

# Code provided:
 
    #     import random

    #     def play_game():
    #         score= 0
    #         while True:
    #             input("Press Enter to roll the dice...")

    #     play_game()

# Use this prompt: "I've written this Python code for a user to play a simple dice roll game,
#                   where if they roll a 1 they lose their score, but if they roll any other number they win.
#                   Can you complete it for me"

# Bonus Objective: "Write an approppriate ChatGPT prompt so that it can assist us in adding the functionality where
#                   the player reaches a score of 20?"



# Though this comment above is the prompt I'll start with, I plan to add more features than what is requested in activities.
# Everything without a comment next to it is what ChatGPT sent me in the first response, I'll add comments to each line or above a block of cose which shows the update,
# as we expand and refine the game below:

import random

def play_game():
    while True: #Added a while loop for the entire game so even if you lose you can choose to restart the game    
        #Added on 4th and expand on with 5th request to make sure the user enters their choice with number keys
        while True:
            user_input = input(f"\nEnter your target score, it need to be a minimum of 20: ").strip()

            if user_input.isdigit():
                target = int(user_input)
                if target >= 20:
                    break
                else:
                    print("Target score must be at least 20.")
            elif user_input.isalpha():
                print("Please enter a number using the number keys, not words.")
            else:
                print("Invalid input. Please enter a valid number (e.g., 25).")

        score = 0
        while True:
            print() #Added this myself to create a gap after responding with 'y'
            input("Press the Enter key to roll the dice...") #Changed it from enter to any key
            roll = random.randint(1, 6)
            print(f"\nYou rolled a {roll}!")
            print() #Added this myself to create a gap between your roll and score

            if roll == 1:
                print("Oh no! You rolled a 1. You lose all your points!")
                score = 0
                print("Game Over.") #Moved 'break' futher down as part of the 6th update request

                #Expanded on this if statement to allow the user to restart, something added on the 6th update request.
                while True:
                        restart_choice = input("Do you want to restart the game? (y/n): ").strip().lower()
                        if restart_choice == 'y':
                            print("\nRestarting the game...\n")
                            break  # Breaks out of inner game loop and restarts outer game loop
                        elif restart_choice == 'n':
                            print("Thanks for playing!")
                            return  # Exits the function completely
                        else:
                            print("Invalid input. Please enter 'y' to restart or 'n' to quit.")
                break  # Exit current game loop to restart the game

            else:
                print("You've won this round!") #Line of code added on the 2nd update request
                score += roll
                print(f"Your current score is: {score}\n")
                
                # Added as part of 4th update request
                if score >= target:
                    print(f"Congratulations! You've reached your target of {target}!")
                
                    # Added from 6th update request
                    while True:
                        win_choice = input("Do you want to play again? (y/n): ").strip().lower()
                        if win_choice == 'y':
                            print("\n Restarting the game...\n")
                            break
                        elif win_choice == 'n':
                            print("Thanks for playing!")
                            return 
                        else:
                            print("Invalid input. Please enter 'y' to restart or 'n' to quit.")
                    break

                #This block of code was added on the 2nd update request
            while True:    
                choice = input("Do you want to roll again? (y/n): ").strip().lower()
                if choice == 'y': #Altered as part of 3rd update request, changed != to ==, so the elif part could work
                    break
                #This block of code was added on the 3rd update request
                elif choice == 'n':
                        print("Thanks for playing!")
                        print(f"Game over. Final score: {score}")
                        return  # Exit the function
                else:
                    print("Invalid input. Please enter 'y' to continue or 'n' to quit.")


play_game()