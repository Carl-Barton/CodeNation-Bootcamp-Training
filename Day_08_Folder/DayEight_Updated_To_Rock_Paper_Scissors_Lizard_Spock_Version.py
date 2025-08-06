# Ultra Challenge Objective: Can you update your code so it can now play the Rock, Paper,
# Scissors, Lizard, Spock version of the game. A version of the game used to settle a dispute
# between two characters in the show 'The Big Bang Theory'

import random, sys

print('ROCK, PAPER, SCISSORS, LIZARD, SPOCK')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0
playerScore = 0  # Track the player's score for the best out of 5.
computerScore = 0  # Track the computer's score for the best out of 5.

# List of valid moves
valid_moves = ['r', 'p', 's', 'l', 'v']

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('Best Out of 5 Score: Player %d - Computer %d' % (playerScore, computerScore))
    
    if playerScore == 3:
        print("You won the Best Out of 5! Congratulations!")
        break  # End the game if the player wins 3 rounds.
    
    if computerScore == 3:
        print("The computer won the Best Out of 5. Better luck next time!")
        break  # End the game if the computer wins 3 rounds.
    
    while True:  # The player input loop.
        print('Enter your move: (r):Rock (p):Paper (s):Scissors (l):Lizard (v):Spock or (q):Quit')
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove in valid_moves:
            break  # Break out of the player input loop.
        print('Invalid move. Please type one of r, p, s, l, v or q.')

    # Display what the player chose:
    move_names = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS', 'l': 'LIZARD', 'v': 'SPOCK'}
    print(f'You chose: {move_names[playerMove]}')

    # Display what the computer chose:
    computerMove = random.choice(valid_moves)
    print(f'Computer chose: {move_names[computerMove]}')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and (computerMove == 's' or computerMove == 'l'):  # Rock crushes Scissors and Lizard
        print('You win this round!')
        wins += 1
        playerScore += 1  # Player gains a point in the Best Out of 5.
    elif playerMove == 's' and (computerMove == 'p' or computerMove == 'l'):  # Scissors cuts Paper and decapitates Lizard
        print('You win this round!')
        wins += 1
        playerScore += 1  # Player gains a point in the Best Out of 5.
    elif playerMove == 'p' and (computerMove == 'r' or computerMove == 'v'):  # Paper covers Rock and disproves Spock
        print('You win this round!')
        wins += 1
        playerScore += 1  # Player gains a point in the Best Out of 5.
    elif playerMove == 'l' and (computerMove == 'p' or computerMove == 'v'):  # Lizard eats Paper and poisons Spock
        print('You win this round!')
        wins += 1
        playerScore += 1  # Player gains a point in the Best Out of 5.
    elif playerMove == 'v' and (computerMove == 'r' or computerMove == 's'):  # Spock vaporizes Rock and smashes Scissors
        print('You win this round!')
        wins += 1
        playerScore += 1  # Player gains a point in the Best Out of 5.
    else:
        print('You lose this round!')
        losses += 1
        computerScore += 1  # Computer gains a point in the Best Out of 5.
