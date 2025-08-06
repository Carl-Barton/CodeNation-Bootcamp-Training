# Objective: Your Task is to create a Python Console app version of the 'Rock Paper Scissors' game.
# The user will be playing against the computer which will randomly share one of the three outcomes
# after the user has entered their choice.
# The round will then end, and the result shown to the user.
# Bonus Goals: Best out of 3,5 or 7 (I choose to do it ' best out of 5' in this version)


import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0
player_score = 0  # Track the player's score for the best out of 5.
computer_score = 0  # Track the computer's score for the best out of 5.

while True:  # The main game loop.
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    print(f'Best Out of 5 Score: Player {player_score} - Computer {computer_score}')
    if player_score == 3:
        print("You won the Best Out of 5! Congratulations!")
        break  # End the game if the player wins 3 rounds.
    
    elif computer_score == 3:
        print("The computer won the Best Out of 5. Better luck next time!")
        break  # End the game if the computer wins 3 rounds.
    
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()  # Quit the program.
        elif player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Break out of the player input loop.
        else:
            print('Type one of r, p, s or q.')

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK Versus...')
    elif player_move == 'p':
        print('PAPER Versus...')
    else:
        print('SCISSORS Versus...')

    # Display what the computer chose:
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('Rock')
    elif random_number == 2:
        computer_move = 'p'
        print('Paper')
    else:
        computer_move = 's'
        print('Scissors')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win this round!')
        wins = wins + 1
        player_score += 1  # Player gains a point in the Best Out of 5.
    elif player_move == 'p' and computer_move == 'r':
        print('You win this round!')
        wins = wins + 1
        player_score += 1  # Player gains a point in the Best Out of 5.
    elif player_move == 's' and computer_move == 'p':
        print('You win this round!')
        wins = wins + 1
        player_score += 1  # Player gains a point in the Best Out of 5.
    elif player_move == 'r' and computer_move == 'p':
        print('You lose this round!')
        losses = losses + 1
        computer_score += 1  # Computer gains a point in the Best Out of 5.
    elif player_move == 'p' and computer_move == 's':
        print('You lose this round!')
        losses = losses + 1
        computer_score += 1  # Computer gains a point in the Best Out of 5.
    else:
        print('You lose this round!')
        losses = losses + 1
        computer_score += 1  # Computer gains a point in the Best Out of 5.