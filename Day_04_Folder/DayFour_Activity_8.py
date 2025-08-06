# Objective: Using your dictionary of animals. 
# Create a program which allows a user to sumbit an animal name and baby name.
# If the animal already exists, return the existing baby name.
# If the animal does not exist, add it to the dictionary.

animals = {
    "Lion" : "Cub",
    "Pigeon" : "Squab",
    "Gecko" : "Hatchling",
    "Hedgehog" : "Hoglet",
}

print("Animals on our list: ", list(animals.keys()))

animal_name = input("Please enter the name of the animal you want to add to our dictionary: ").capitalize()
animal_baby = input("Please enter the baby name of the animal you want to add to our dictionary: ").capitalize()

if animal_name in animals:
    print("This animal already exists in our dictionary.")
else:    
    animals.update({animal_name: animal_baby})
    print("Animal added successfully!")
    print()
    print("Updated animal list: ", animals)

# ChatGPT recommended animals[animal_name] = animal_baby
# This would also work instead of animals.update()

