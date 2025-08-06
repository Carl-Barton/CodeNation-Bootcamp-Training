# Objective Using the two lists, create a dictionary where country is the key, and language is the value.

# The example I need to use:

countries = ["England", "Spain", "Ethiopia", "Iran"]

language = ["English", "Spanish", "Amharic", "Farsi"]

# Could code manually, which is alright if the list in each stays short.
# Howver, there ia a simpler method if each list is long and you want to save time:

country_language_dict = dict(zip(countries,language))

print(country_language_dict)

# 'zip' pairs them up based on their positions, then 'dict' converts the sequence into a dictionary.
