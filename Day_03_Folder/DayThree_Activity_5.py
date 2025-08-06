# Objective: Create a variable called 'word' that takes a string.
# Create an if statement that checks if the last letter is the same as the first.
# Bonus Goal: Create an if statement that checks if the whole string is a palindrome

word = input("Enter a word: ").lower()


if word == word[::-1]:   #check if the word is a palindrome
    print("This word is a palindrome!")
elif word[0] == word[-1]:   #Check if the first letter is the same as the last letter                    
    print("The first and last letters are the same!")
else:
    print("The first and last letters are different.")

    
