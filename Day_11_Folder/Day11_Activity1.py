# Objective: Write a list of your favourite books. Create a program which allows a user to type in their favourite book.
#            If their favourite book matches one of your favourite books print "<bookname> is one of my favourite books too."
#            Else, print "I haven't read that book."
#            Ensure the user gives you information, a blank string should not be accepted!

# I decide to with comicbooks instead of novels, since I found it easier to pick my favourites of that medium. 


# List of my favorite books
my_comic_books = [
    "Batman: The Long Halloween",
    "Civil War: A Marvel Comics Event ",
    "Batman: Prey",
    "Amazing Fantasy 15",
    "Hellboy: Seed of Destruction "
]

# Function to interact with the user
def favorite_book_check():
    while True:
        # Prompt the user for their favorite book
        user_book = input("Enter your favorite comic book (or type 'quit' to exit): ").strip()

        # Check if the user wants to quit
        if user_book.lower() == 'quit':
            print("Goodbye!")
            break

        # Ensure the user gives valid input
        if not user_book:
            print("Please enter a valid comic book name.")
            continue

        # Check if the book matches one of my favorites
        if user_book in my_comic_books:
            print(f"{user_book} is one of my favorite comic books too.")
        else:
            print("I haven't read that comic book.")

# Run the function
if __name__ == "__main__":
    favorite_book_check()