# Activity 1 Objective: 
# On the following slide is an example of a function that includes a parameter already.
# Parameters are responsible for functions being able to work on different data inputs.
# Edit the snippet on the following slide to include another two or more parameters for another topping and size.

# Code to alter:

# def take_order(topping):
#     print("Pizza with {}".format(topping)) 

# take_order("chesse")

# New Version:

def take_order(size,topping,topping2):
    print("I want a {} Pizza with {} and {}".format(size,topping,topping2)) #First time using .format

take_order("large","cheese","pepperoni")

##############################################################################

# Activity 2 Objective:
# The factorial of a number is the product of all positive integers less than or equal to that number.
# It is written as n! For example, 4! is 4x 3 x 2 x1. The following slide’s code should calculate factorial, but it is broken.
# Can you fix it?

# Code to fix:

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range():
#             result * i
#         return
# 
# num = int(input("Enter a number: "))
# factorial_result = factorial() 
# print(f"The factorial of {num} is: {factorial_result}"")

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1): # So if n is 5 you need the plus 1 to make it stop on 5 but not before 5, so its 1,2,3,4,5 and not 1,2,3,4.
            result *= i # result "times" i, then save to result
        return result

num = int(input("Enter a number: "))
factorial_result = factorial(num)
print(f"The factorial of {num} is: {factorial_result}")