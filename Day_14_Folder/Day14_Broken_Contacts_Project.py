# Objective: A programming contractor was asked to write a simple Python program which allowed a user to manage their contacts.
#            However, the contractor became ill and did not complete the program, and some the code written contains errors. 
#            Your task is to fix and complete the Contacts Python Program.
# 
# Your program should allow a user to ADD a new contact, UPDATE and existing contact, DISPLAY all contacts,
# SEARCH for a contact and DELETE an existing contact. You must use class structure to organise your code.
# Two contacts must be initialised when the program starts
# 
# Bonus Goals:
# Ultilising the Colorama library for more customisation
# No duplicate contacts allowed
# Include a 'Sort Contacts' functionality for the user.                         


from colorama import Fore, Style

class Contact:                                                       
    def __init__(self, person_name, phone_number, email_address):
        self.name = person_name
        self.phone = phone_number
        self.email = email_address

class ContactBook:                                                  
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    def add_contact(self, person_name, phone_number, email_address): #Function created to add new contacts to the list of contacts within th contact book
        # Checking for dupilcates before adding a new contact
        for contact in self.contacts:
            if contact.name == person_name and contact.phone == phone_number and contact.email == email_address:
                print("This contact already exists in your contact book.")
                return #Leaving this menu without adding the contact.

       ##################

       #Before adding this from Chat about duplicates, I pasted over what I've would've done, according to Chat, I wasn't far off.
       #It's just the logic needed slight adjustments. I thought I needed to create a kind of if statement, something on these lines:

       # if self.contacts.append(Contact(person_name, phone_number, email_address) == Contact(person_name, phone_number, email_address): #don't add contact
       # print("This contact already exists within your contact book")

       #################

        #This section with run if no duplicates were found
        self.contacts.append(Contact(person_name, phone_number, email_address))  #Change it from an ".add" to ".append" like you would normally use in lists - ChatGpt Reminded Me of this  
                                                                                 #Plus add the Main "Contact" Class to inform the computer which layout it's using, originally I thought I would need to use ".extend". 
        print(Fore.GREEN + f"Contact {person_name} added successfully." + Style.RESET_ALL)  #Make sure the variables match when you want to use them.

    def display_all_contacts(self): #Function created to display all the contacts it currently as stored
        if self.contacts:
            print("All Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n") #You use contact.name, contact.phone, and contact.email to access the attributes of the Contact object directly, because contact represents that specific instance. T
                                                                                                 #This way, you can access the details (name, phone, email) stored in each Contact object.
        else:                                                                                    #If there is no list this option is excuted.
            print(Fore.RED + "No contacts found." + Style.RESET_ALL)

    def search_contact(self, search_term): #Created function that allows the user to search the data using stored values and user input
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone or search_term.lower() in contact.email.lower():
                found_contacts.append(contact)
            
        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n")
        else:
            print(Fore.RED + "No contacts found matching your search." + Style.RESET_ALL)           
    
    def update_contact(self,name_to_update): #This be another set of If statements like in the main() text below
        for contact in self.contacts:
            if contact.name.lower() == name_to_update.lower():
                print(Fore.GREEN + "Contact found." + Style.RESET_ALL + "What would you like to update?")
                print("1. Name")
                print("2. Phone Number")
                print("3. Email")
                choice = input("Enter your choice (1|2|3): ")

                if choice == "1":                             #This if statements use the same structure of creating a new variable then that variable gets add as the stored data in contacts.
                    new_name = input("Enter the new name: ")
                    contact.name = new_name
                    print(Fore.GREEN + "Name updated successfully." + Style.RESET_ALL)
                elif choice == "2":
                    new_phone = input("Enter the new phone number: ")
                    contact.phone = new_phone
                    print(Fore.GREEN + "Phone number updated successfully." + Style.RESET_ALL)
                elif choice == "3":
                    new_email = input("Enter the new email: ")
                    contact.email = new_email
                    print(Fore.GREEN + "Email updated successfully." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Invalid choice. No updates made." + Style.RESET_ALL)
                return

        print(Fore.RED + f"Contact {name_to_update} not found." + Style.RESET_ALL) #Again if there are no matches in contacts.                     
 
    def remove_contact(self, person_name):
        for contact in self.contacts:
            if contact.name.lower() == person_name.lower(): #put everything in lower case
                self.contacts.remove(contact) #Remove someone from the contacts
                print(Fore.GREEN + f"Contact {person_name} removed successfully." + Style.RESET_ALL)
                return
            print(Fore.RED + f"Contact {person_name} not found." + Style.RESET_ALL) #If this person doesnt currently exist in the list contacts, this message will appear.

    def sort_contacts(self, choice = 1): 
        print(Fore.BLUE + "\n--- Sort Contacts Menu ---\n" + Style.RESET_ALL)
        print(Fore.BLUE + "1." + Style.RESET_ALL + "Sort A-Z")                   #Giving your user options within separate menu
        print(Fore.BLUE + "2." + Style.RESET_ALL + "Sort Z-A")
        print()
    
        choice = input("Enter your choice: ")
    
        if choice == "1":
            self.contacts.sort(key=lambda contact: contact.name.lower())
            print("Contacts sorted in ascending (A-Z) order.")
        elif choice == "2":
            self.contacts.sort(key=lambda contact: contact.name.lower(), reverse=True)
            print("Contacts sorted in descending (Z-A) order.")
        else:
            print(Fore.RED + "Invalid choice. Please select 1 or 2." + Style.RESET_ALL)
           
def main():
    contact_book = ContactBook()

    while True:
        print(Fore.BLUE + "\n--- Contact Book Menu ---\n" + Style.RESET_ALL)
        print(Fore.BLUE + "1." + Style.RESET_ALL + " Add New Contact.")
        print(Fore.BLUE + "2." + Style.RESET_ALL + " Display All Contacts.")
        print(Fore.BLUE + "3." + Style.RESET_ALL + " Sort Contacts.")
        print(Fore.BLUE + "4." + Style.RESET_ALL + " Search Contacts.")
        print(Fore.BLUE + "5." + Style.RESET_ALL + " Update Contacts.")
        print(Fore.BLUE + "6." + Style.RESET_ALL + " Remove Contact.")        
        print(Fore.BLUE + "0." + Style.RESET_ALL + " Exit")
        print()
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)

        elif choice == "2":
            contact_book.display_all_contacts() #Simply calling the function we've created line 19 in connection line 41
        
        elif choice == "3":
            contact_book.sort_contacts()

        elif choice == "4":
            search_term = input("Enter name, phone number, or email to search: ")
            contact_book.search_contact(search_term)

        elif choice == "5":
            name_to_update = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name_to_update)

        elif choice == "6":
            name_to_remove = input("Please enter the name of the contact you would like to remove: ")
            contact_book.remove_contact(name_to_remove)

        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option from the menu (0-6)." + Style.RESET_ALL)
            print("")

if __name__ == "__main__":
    main()