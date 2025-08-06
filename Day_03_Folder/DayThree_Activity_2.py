# Objective: Create a variable called num. Check if the variable is divisible by 3 or 5.
# If it is print "This number is divisible by 3 or 5" to the terminal.
# Otherwise print "This number is not divisible by 3 or 5".

num = int(input("Enter a number: "))             #int() changes string to a integer so it can be use in maths

if num % 3 == 0 or num % 5 == 0:     
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")   