# Mini Challenges involving 'for' loops:

# For Loop Challenge 1 - Printing Numbers from 1 to 10

start = 1 #Initialise a starting number

for i in [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: #Ten iterations
    print(start)
    start += 1 # Increments

# A Range loop would be better to use instead of this method, but we'll cover that later

####################################################################################################

# For Loop Challenge 2 - Printing Even Numbers from 2 - 20    

startV2 = 2

for i in [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    print(startV2)
    startV2 += 2 # Increments of 2

####################################################################################################

# For Loop Challenge 3 - Sum Of Numbers from 1 to 100

# Initialize the starting number and total sum
number = 1 #start with the first number
total_sum = 0

for i in [0] * 100:  # Instead of typing out a hundred zeroes.
    total_sum += number  # Add the current number to the total sum
    number += 1  # Increment the number

# Print the result
print(f"The sum of all numbers from 1 to 100 is {total_sum}")

####################################################################################################

# For Loop Challenge 4 - Counting Vowels

user_input = input("Enter a string: ") # Get a string from the user

vowel_count = 0 # Initialize a counter for vowels

vowels = "aeiouAEIOU" # Define the set of vowels

# Loop through each character in the string
for char in user_input:
    if char in vowels:  # Check if the character is a vowel
        vowel_count += 1

# Print the result
print(f"The number of vowels in the string is {vowel_count}")

####################################################################################################

# For Loop Challenge 5 - Multiplication Table of number selected by user

num = int(input("Enter a number: ")) # Get the number from the user

multiplier = 1 # Initialize a counter

# Use a for loop with a custom sequence to iterate 12 times
for i in [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:  # Twelve iterations
    print(f"{num} x {multiplier} = {num * multiplier}")
    multiplier += 1  # Increment the multiplier
