# This is the first version of the Magic 8 Ball I created, but then adapted this one to fit the criteria of activity 2 

import random
from colorama import Fore

def get_answer(answer_number):
    if answer_number == 1:
        return Fore.GREEN + "It is certain" + Fore.RESET  # Positive (Green)
    elif answer_number == 2:
        return Fore.RED + "Outlook not so good" + Fore.RESET  # Negative (Red)
    elif answer_number == 3:
        return Fore.GREEN + "Yes, definitely" + Fore.RESET  # Positive (Green)
    elif answer_number == 4:
        return Fore.RED + "My reply is no" + Fore.RESET  # Negative (Red)
    elif answer_number == 5:
        return Fore.GREEN + "Without a doubt" + Fore.RESET  # Positive (Green)
    elif answer_number == 6:
        return Fore.RED + "Very doubtful" + Fore.RESET  # Negative (Red)
    elif answer_number == 7:
        return Fore.GREEN + "You may rely on it" + Fore.RESET  # Positive (Green)
    elif answer_number == 8:
        return Fore.RED + "Don't count on it" + Fore.RESET  # Negative (Red)

# Generate a random number between 1 and 8
r = random.randint(1, 8)
fortune = get_answer(r)

my_question= input()
print(fortune)

