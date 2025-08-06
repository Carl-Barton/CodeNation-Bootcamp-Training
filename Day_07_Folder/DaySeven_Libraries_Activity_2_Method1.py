# Objective:
# Create a magic 8 ball program!
# Create two lists – one of “good” results and one of “bad” results.
# Allow your user to input a question. After they ask this question, generate a random number.
# If the number is odd, your user gets a bad fortune. If the number is even, they get a good fortune.
# Use a random method to pick a random fortune from the appropriate list and print it out.
# Use Colorama to display bad fortunes in red text, and good fortunes in green text.

import random
from colorama import Fore # I only want to import 'Fore' as I'm planning to just change the colour of the text. 

# A list of good fortunes
good_fortunes = [                 
    "It is certain",
    "Yes, definitely",
    "Without a doubt",
    "You may rely on it"
]
   
# A list of bad fortunes
bad_fortunes = [
   "Outlook not so good",
   "My reply is no",
   "Very doubtful",
   "Don't count on it"
]

# Computer's Statement
print('\n' + Fore.CYAN + "You can only ask the Magic 8 Ball a yes or no question."+ Fore.RESET + '\n')

# User enters their question
users_question = input("Please enter your question here: ")

# Generate a random number, which will be later used to indicate what type of fortune the user will receive
random_number = random.randint(1,8)

# To pick a random entry from a list
select_fortune = random.randint(0,3)

# To select a fortune based whether it's odd or even
if random_number % 2 == 0:
    print('\n' + Fore.GREEN + good_fortunes[select_fortune] + Fore.RESET +'\n')
else:
    print('\n' + Fore.RED + bad_fortunes[select_fortune] + Fore.RESET +'\n')
