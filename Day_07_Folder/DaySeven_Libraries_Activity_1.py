# Objective:
# Create a program which calculates how many days you've been alive for.
# Hints: Look into the datetime library, and don't use input!

# My Hard Code Version  

from datetime import datetime

def calculate_days_alive(birth_date):
    # Convert the string to a datetime object
    birth_date_converted = datetime.strptime(birth_date, "%Y%m%d")
    # Get the current date
    today = datetime.now()
    # Calculate the difference in days
    return (today - birth_date_converted).days

# Example birth date (hardcoded)
birth_date = "20000101"  # January 1, 2000 as an example
days_alive = calculate_days_alive(birth_date)

print(f"You have been alive for {days_alive} days.")

##############

# When revisting this programme I found out I could've done it in a simpler way:
# (I've commented it out, so I don't get doubles in the terminal)

#     from datetime import datetime

#     birth_date = datetime(2000, 1, 1)
#     today = datetime.now()
#     days_alive = (today - birth_date).days
#     print(f"You have been alive for {days_alive} days.")