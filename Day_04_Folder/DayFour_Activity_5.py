# Objective: Create a dictionary of five favourite songs (the key is the artist).
# Using any method, add two new items to your dictionary.

favourite_songs = {
    "Huey Lewis & The News" : "Back In Time",
    "Goo Goo Dolls" : "Iris",
    "Aerosmith" : "Dream On",
    "Imagine Dragons" : "I'm So Sorry",
    "Skillet" : "Finish Line",
}

favourite_songs.update({"Linkin Park" : "New Divide" , "Barns Courtney" : "Champion"}) 
#Could have used .setdefault if the key hasn't already been used, but I would have add each one as separately.

print(favourite_songs)