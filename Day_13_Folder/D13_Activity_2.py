# Objective: After Day 13 Activity 1, you learned how to use 'Methods', using what you've just learned, 
#            make a similar method for your heroes to introduce themselves.


class HeroUpdated():
    def __init__(self, hero_name, hero_secret, hero_ability, hero_arch):
        self.hero = hero_name
        self.secret = hero_secret
        self.ability = hero_ability
        self.arch = hero_arch

    def introduce(self):
        print(f"Hi, I'm {self.hero}, my secret identity is {self.secret}. Erm... I would say my main power is {self.ability} and my main nemesis is {self.arch}.") 
        #used "return" instead of "print" as print was returning "none" inbetween each line.

boyscout = HeroUpdated("Superman","Clark Kent", "Flight", "Lex Luthor")
princess = HeroUpdated("Wonder Woman", "Diana Prince", "Super Strength", "Circe")
webhead = HeroUpdated("Spider-Man", "Peter B. Parker", "Webswinging", "Green Goblin")
weaponx = HeroUpdated("Wolverine", "Logan", "Healing Factor", "Sabertooth")

print("")
print("DC and Marvel Heroes:")
boyscout.introduce()
princess.introduce()
webhead.introduce()
weaponx.introduce()
print("")


