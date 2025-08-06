#Objective: Correct the code below so it functions as expected.
#Can you use anything to make sure "London" and "london" are accepted as correct answers?

# Broken Code (copied exactly):

# print("What is the captial of England?")

# answer = input(Type your answer here >> )

# if answer = "London":
#  print("Correct! The answer is {answer}")
# else:
#  prnt("Incorrect, the answer is 'London', not {answer}")

print("What is the capital of England?")

answer = input("Type you answer here >> ").capitalize()

if answer == "London":
    print(f"Correct! The answer is {answer}.")
else:
    print(f"Incorrect, the anser is 'London', not {answer}.")