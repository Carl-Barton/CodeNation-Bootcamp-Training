#Objective: Create a program which asks a user how many apples they want to buy
#Display the total cost of the apples in both pence, and pounds and pence
#Make sure it's formatted to have two decimal places for pounds and pence

#Apples cost 25p each

apple_price = 0.25

print()
print("An Apple costs 25p, how many would you like today?")
selected_amount = int(input("Please enter number of the amount: "))
total_cost = apple_price * selected_amount
print(f"The total cost of your purchase is {int(total_cost * 100)}p, so £{total_cost:.2f}")
print()