# Objective: Using your dictionary of animals. 
# Create a program which allows a user to search for an animal to see the corresponding young name.
# If the animal does not exist in the dictionary, return a suitable message.

animals = {
    "Lion" : "Cub",
    "Pigeon" : "Squab",
    "Gecko" : "Hatchling",
    "Hedgehog" : "Hoglet",
}

print("Animals on our list: ", list(animals.keys()))

user_selected = input("Select the animal your want to search: ").capitalize()

young_name = animals.get(user_selected, "Invalid") # Normally you would the second part as a custom message to the user, 
                                                   # but here I'm using as marker to check whether their choice exists on my list.
if young_name == "Invalid":
    print("This animal, " + user_selected + " , does not exist on our list." ) # This is what the user will see instead of the custom error message within .get()
else:
    print("The young of this animal is called a " + young_name + ".")

# 'input()' allowing the user to interact in the terminal

# Added .capitalize() just in case they don't type it with a capital letter. 
# Without it, if I typed 'lion' it would come up with None.

# Using .get() has the bonus of stopping an code-stopping error, if something else is entered by the user, which isn't a key.