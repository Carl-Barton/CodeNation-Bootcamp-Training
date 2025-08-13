# Objective: Using the two lists create a dictionary where country is the key, 
#            and language is the value.

# This bit of the code was already provided:

countries = ["England", "Spain", "Ethiopia", "Iran"]
languages = ["English", "Spanish", "Amharic", "Farsi"]

# The part of the code I added:

country_language_dict = dict(zip(countries, languages))

print(country_language_dict)

# The dict(zip()) function in Python is a convenient way to create a singular dictionary
# from two lists or sequences.
