# Objective: Create a new class to build superheroes from. Each Superhero will have:
#            - A superhero name
#            - A secret identity
#            - A superpower
#            - An arch enemy.

# Create 4 superheroes from your class and use their properties to write a string about each.

class Superhero():
    def __init__(self, superhero_name, secret_identity, main_superpower, arch_enemy):
        self.hero = superhero_name
        self.secret = secret_identity
        self.power = main_superpower
        self.arch = arch_enemy

boyscout = Superhero("Superman", "Clark Kent", "Flight" , "Lex Luthor")
princess = Superhero("WonderWoman", "Diana Prince", "Super Strength", "Circe" )
webhead = Superhero("Spider-Man", "Peter B. Parker", "Webswinging", "Green Goblin")
weaponx = Superhero("Wolverine", "Logan", "Healing Factor", "Sabertooth")

print()
print(f"One of DC's main hero's, part of the core Trinity is {boyscout.hero}, his secret identity is {boyscout.secret} who grew up on a farm. One of his main abilities is {boyscout.power}, which helps cross vast distances. Which is useful against his main arch villain, {boyscout.arch}.")
print()
print(f"Another core hero of DC is {princess.hero}, who at times has adopted the alias of {princess.secret}, when she needs be undercover. One of her main abilities is {princess.power}, which has used against God villains such as {princess.arch}.")
print()
print(f"Marvel's most famous hero is {webhead.hero}, who's secret identity is {webhead.secret}. His main abilities is {webhead.power} which is really useful when chasing down his rogue's gallery. The villain which arguably has hurt Spider-Man the most is {webhead.arch}.")
print()
print(f"Another famous Marvel character is {weaponx.hero}, who goes by the name {weaponx.secret}, though that's not his birthname. His main ability is his {weaponx.power} which has allowed him to not only live longer than the average human, but also help him survived some of his most brutal fights with {weaponx.arch}.")
print()
