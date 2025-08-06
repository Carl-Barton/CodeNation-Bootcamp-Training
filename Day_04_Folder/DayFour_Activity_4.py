# Testing out Dictionaries

animals = {
    "Lion" : "Cub",
    "Pigeon" : "Squab",
    "Gecko" : "Baby Gecko", # Baby Gecko is just a place holder
    "Hedgehog" : "Hoglet",    
}

print(animals["Gecko"])

animals["Gecko"] = "Hatchling" 

print(animals["Gecko"])

#Result: Hatchling

print(animals.keys()) # Just prints the dict_keys

print(animals.values()) # Just prints the dict_values

print(animals.items()) # Prints both dict_keys and dict_values

print(animals.get())


