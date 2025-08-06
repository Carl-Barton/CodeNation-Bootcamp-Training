# Mini Challenges involving 'While' loops:

# Activity 1: Hello World x 13

number13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in number13:  
    print("Hello World!")

# Then converted it into a While Loop

number_13 = 1

while number_13 < 14:
    print("Hello World!")
    number_13 += 1

#####################################################################

# Activity 2: Sum the list

# Outer loop for numbers 1 to 12
for num in range(1, 13):  # Multiplication tables from 1 to 12
    print(f"Multiplication table for {num}:")
    
    # Inner loop for multiplying from 1 to 12
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")
    
    # A blank print() to add a line break after each table
    print()

#####################################################################

# Activity 3: 10 Seconds to Blastoff!

blast_off_count = 10

while blast_off_count > 0:   #It will keep looping round until 0, and when it hits 0, it will jump to the else block
    print(blast_off_count)   
    blast_off_count -= 1
else:                        #When it jump to else, instead of printing 0, it will print "Blast Off!"
    print("Blast Off!") 

#####################################################################

# Activity 4: Dog Imposters

# Initial list with elements as strings
animals = ["cat", "dog", "dog", "bird", "elephant", "Jim", "dog"]

# List to store all the "dog" elements
dogs = []

# Loop through each element in the list
for animal in animals:
    if animal == "dog":  # Check if the element is "dog"
        dogs.append(animal)  # Append "dog" to the new list

# Print the total count of "dogs"
print(f"We have {len(dogs)} dogs at our shelter.")

#####################################################################

#Activty 5 - Going Shopping

# Shopping list and items at the shop
shopping_list = ["cheese", "beans", "crisps", "milk", "apples"]
at_the_shops = ["pears", "jam", "cheese", "apples", "bread", "tuna", "crisps"]

# Loop through each item in your shopping list
for item in shopping_list:
    found = False  # Flag to check if the item is in the shop
    
    # Check each item at the shop
    for shop_item in at_the_shops:
        if item == shop_item:  # If the item is found at the shop
            found = True
            break  # Exit the inner loop as we found the item
    
    # Print the appropriate message
    if found:
        print(f"Yah, they've got {item}!")
    else:
        print(f"Oh no, they've not got {item}!")

# A nested for loop refers to placing one for loop inside another for loop in Python 
# (or other programming languages). Each iteration of the outer loop runs through a sequence of values, 
# and for each value, the inner loop also runs through a sequence of values.

#####################################################################

# Activity 6 - For vs While

# Main objective: Print the numbers from 1 to 10 using a 'For Loop' then a 'While Loop'
# Then answer these questions:
# Question 1: Which Solution has the most lines of code?
# Question 2: Did either require variables; if so, why?
# Question 3: Which solution is more useful and why?

#Using a for loop:
for i in range(1,11):
    print(i)


# Using a while loop:
i = 1
while i <= 10:
    print(i)
    i += 1  # Increment the counter

# Answer To Question 1:
# While loop has more lines of code

# Answer To Question 2:
# Both use a variable but it in slightly different ways. 
# First one uses one vairbale just to create the 'For Loop', while the other is used as a counter to inform the 'While Loop'.

# Answer To Question 3:
# Though 'For Loop' is simpler in terms of the amount of code, the 'While Loop' provides more control and flexibilty for the developer utilise. 
# In addition, it's easier to set up user input if needed. So the 'While Loop' is overall more useful.