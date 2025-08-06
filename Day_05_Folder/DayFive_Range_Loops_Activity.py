# Mini Challenges involving 'range' loops:

# Range Loop Challenge 1: Printing numbers from 1 to 10:

for i in range(1, 11):
    print(i)

###########################################################################

# Range Loop Challenge 2: Printing even numbers from 1 to 20

for i in range(2, 21, 2):
    print(i)

###########################################################################

# Range Loop Challenge 3: Printing numbers in reverse from 10 to 1

for i in range(10, 0, -1):
    print(i)

###########################################################################

# Range Loop Challenge 4: Sum of even numbers

# Initialize the total sum
total_sum = 0

# Use a for loop to iterate through numbers from 1 to 50
for i in range(2, 51, 2):  # Start at 2, go to 50, step by 2
    total_sum += i  # Add the even number to the total sum

# Print the result
print(f"The sum of all even numbers between 1 and 50 is {total_sum}")

###########################################################################

# Range Loop Challenge 5: Muplication table

# Get the number from the user
num = int(input("Enter a number to generate its multiplication table: "))

# Generate the multiplication table
print(f"Multiplication table for {num}:")

for i in range(1, 13):  # Loop from 1 to 12
    print(f"{num} x {i} = {num * i}")