# Objective: Copy the example list from the powerpoint. 
# Use a method to display the number of the following items; egg, kale, stamps, carrot and orange juice.

shopping_list = [  # [] used to create lists
    "apple",       # can be entered all on just one line or you can have it structured like this, one each on line.
    "carrot",
    "pizza",
    "carrot",
    "dog_food",
    "orange juice",
    "egg",
    "kale",
    "carrot",
    "kale"
    "orange juice",
    "kale",
    "toilet roll",
    "stamps",
    "noodles",
    "pasta sauce",
    "egg",
    "pasta sauce"
]

#Counting each item manually

egg_count = shopping_list.count("egg")
kale_count = shopping_list.count("kale")
stamps_count = shopping_list.count("stamps")
carrot_count = shopping_list.count("carrot")
orange_juice_count = shopping_list.count("orange juice")

print("There are " + str(egg_count) + " eggs in the shopping list.")
print("There are " + str(kale_count) + " kales in the shopping list.")
print("There are " + str(stamps_count) + " stamps in the shopping list.")
print("There are " + str(carrot_count) + " carrots in the shopping list.")
print("There are " + str(orange_juice_count) + " orange juices in the shopping list.")

# After learning about 'for' loops, I could change everything after the list to this:

#   items_to_check = ["egg","kale","stamps","carrot","orange juice"]

#    for item in items_to_check:
#        quantity = shopping_List.count(item)
#        print(item + ": " + str(quantity))
