# Objective: The factorial of a number is the product of all positive integers less than or equal to that number.
#            It is written as n! For example, 4! is 4x3x2x1. The following slide's code should calculate factorial,
#            but it is broken. Can you fix it?

# The broken code:

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
# print(f"The factorial of {num} is {factorial_result})



def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1): #So n is 5 you need the plus 1 to make it stop on 5 but not before 5 = 1,2,3,4,5 otherwise it would be 1, 2,3,4,(5)
            result *= i # result "times" i, then save to result
        return result

num = int(input("Enter a number: "))
factorial_result = factorial(num)
print(f"The factorial of {num} is: {factorial_result}")
