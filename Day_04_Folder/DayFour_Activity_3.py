# Objective: To create a drinks menu that demonstartes methods previously learned and one 'for' loop.
# Methods to include; .remove(), .reverse(), .sort() , .count(), .extend()

hotDrinks = [
    "Hot Chocolate",
    "Earl Grey Tea", 
    "Green Tea",
    "Peppermint Tea", #This will be the one I'll be removing
    "Tea", 
    "Tea Latte", 
    "Cafe Latte",
    "Espresso",
    "Americano"]

hotDrinks.remove("Peppermint Tea") #Remove singular item command - not sure if it can do multiple removals

hotDrinks.extend(["Pumpkin Spiced Latte","Traditional Kompot","Hot Apple Cider"]) #This is add new options to the drink list

#Print Options for the App/ User
print("Please choose one of the following options:")
print("Option 1: Print menu options.")
print("Option 2: Print menu options in reverse.")
print("Option 3: Print Menu options in alphabetical order.")
print("Option 4: Count how many types of types of Tea on the menu")
print("Option 5: End Program.")

#User input regarding option choice - variable created
choice = input("Enter your choice (1, 2, 3, 4 or 5 please.)")

#Contidions based on user's choice / so I need user input for this too work
if choice == "1":
    print("\nMenu Options:")
    for drink in hotDrinks:                                  #'for' and 'drink' help create aloop and 'drink' is the variable for said loop
        print(drink)
elif choice == "2":
    hotDrinks.reverse()                                      #Using .reverse() method/command - will reverse the entire list if selected
    print("\nMenu Options in Reverse:")
    for drink in hotDrinks:
        print(drink)
elif choice == "3":
    hotDrinks.sort()                                         #Using sort to reorder the entire list, in this case to A-Z
    print("\nMenu Options in Alphabetical Order:")
    for drink in hotDrinks:
        print(drink)
elif choice == "4":
    tea_types = ["Earl Grey Tea", "Green Tea", "Tea", "Tea Latte"]
    tea_count = 0

    #Count the amount of tea types
    for tea in tea_types:
        tea_count += hotDrinks.count(tea)

    print("Total number tea options on the menu: " + str(tea_count))    

elif choice == "5":
    print("Ending Program. Goodbye!")
else:
    print("Invalid Option. Please choose 1, 2, 3, 4 or 5.")