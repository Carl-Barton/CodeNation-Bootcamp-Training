#Objective: Create a program which accepts two inputs from a user (num1 and num2)
#Use these inputs with each operator(+,-,/,*,**,%)
#Print the equations and the output

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f'{num1} * {num2} = {num1 * num2}')
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} % {num2} = {num1 % num2}")
