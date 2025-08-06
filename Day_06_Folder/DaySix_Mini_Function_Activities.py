# Activity 1 Objective: Multiplying Numbers:
# Write a funcion called multiply_numbers(a,b) thats takes two numbers as input, 
# multiples them together, and prints the result. 

def multiply_numbers(a,b):
    answer = a * b
    print(f"{a} times {b} equals {answer}")

multiply_numbers(3,5)
# First number is assign to "a" and the second number is assigned to "b".

##############################################

# Activity 2 Objective: Checking Even or Odd:
# Define a function named check_even_odd(num) that takes a number as input 
# and prints whether it's even or odd.

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

check_even_odd(7)

# The % operator is called the modulus operator, and it tells us the remainder when one number is divided by another.

##############################################

# Activity 3 Objective: Printing a List:
# Create a function called print_list(my_list) that takes a list as input
# and prints each element of the list on a separate line.

def print_list(my_list):
    for element in my_list:
        print(element)

print_list(["apple", "banana", "cherry"])

#############################################

# Activity 4 Objective: Counting Vowels:
# Define a function called count_vowels(word) that takes a word as input 
# and prints the count of vowels (a,e,i,o,u) in the word.

def count_vowels(word):
    vowels = "aeiouAEIOU"  # A string containing all vowels (both lowercase and uppercase)
    count = 0  # Initialize a counter to 0
    
    for char in word:  # Loop through each character in the word
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment the counter if it's a vowel
    
    print(f"The word '{word}' contains {count} vowels.")

count_vowels("hello")
count_vowels("Prohramming")
count_vowels("AEIOU")
