# Objective: Create a variable called password.
# Check how many letters are in the password, if there are fewer than 8,
# print that the password is too short.
# Otherwise print the password.

password = input("Please enter the password you want to use for this account: ")

if len(password) < 8:
    print("The password is too short to be used here.")
else:
    print(password)

#Can be structured the other way round if needed