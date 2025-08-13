# Activity 3 Objective: Make a method for your superheroes called transform,
#                       which prints out a message saying your superhero has transformed
#                       from their real-life persona to their hero persona.
# 
#    


# Activity 4 Objective: Writer a setter to give your superhero a secret lair and
#                       set a lair for all four of your heroe using the setter



class HeroUpdated():
    def __init__(self, hero_name, hero_secret, hero_ability, hero_arch):
        self.hero = hero_name
        self.secret = hero_secret
        self.ability = hero_ability
        self.arch = hero_arch

    def transform(self):
        print(f"{self.secret} has transformed into the hero {self.hero}.")

    def set_lair(self,lair):
        self.lair = lair
        print(f"{self.hero}'s lair has been set to {self.lair}.")    

boyscout = HeroUpdated("Superman","Clark Kent", "Flight", "Lex Luthor")
princess = HeroUpdated("Wonder Woman", "Diana Prince", "Super Strength", "Circe")
webhead = HeroUpdated("Spider-Man", "Peter B. Parker", "Webswinging", "Green Goblin")
weaponx = HeroUpdated("Wolverine", "Logan", "Healing Factor", "Sabertooth")        

boyscout.transform()
princess.transform()
webhead.transform()
weaponx.transform()

boyscout.set_lair("Fortress of Solitude")
princess.set_lair("The Hall Of Justice")
webhead.set_lair("His Apartment In Queens, New York")
weaponx.set_lair("X-Mansion")

