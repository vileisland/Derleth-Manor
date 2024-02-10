init:
    init python: 
        class Item:
            def __init__(self, name, description):
                self.name = name
                self.description = description
                self.amount = 0
            ##display name
            def d_name(self):
                renpy.say(f"{self.name}")
            ##display description
            def d_description(self):
                renpy.say(f"{self.description}")
            ##display amount
            def d_amount(self):
                renpy.say(f"{self.amount} remaining.")

        class Heal(Item):
            def __init__(self, name, description, healpts):
                super().__init__(name, description)
                self.healpts = healpts
            ##display healing points
            def d_heal(self):
                renpy.say(f"Heals {self.healpts} health.")

        class Sanity(Item):
            def __init__(self, name, description, healpts):
                super().__init__(name, description)
                self.sanitypts = healpts
            ##display healing points
            def d_sanity(self):
                renpy.say(f"Heals {self.sanitypts} sanity.")

        class Weapon(Item):
            def __init__(self, name, description, attackpts):
                super().__init__(name, description)
                self.attackpts = attackpts
            def d_attack(self):
                renpy.say(f"Attack strength: {self.attackpts}.")

        class Tool(Item):
            def __init__(self, name, description, combine):
                super().__init__(name, description)
                self.combine = combine


        eels = Heal("Jellied Eels", "A plate of jellied eels. Looking at it makes you queasy", 5)