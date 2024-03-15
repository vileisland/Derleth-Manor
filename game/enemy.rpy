init python:
    import random
    class Enemy:
        def __init__(self, name, image, HP, attackModifier, specialAttack1, specialAttack2, healingMove):
            self.name = name
            self.image = image
            self.transform = characterpos
            self.HP = HP
            self.attackModifier = attackModifier
            self.specialAttack1 = specialAttack1
            self.specialAttack2 = specialAttack2
            self.healingMove = healingMove
            self.transform = characterpos
        def show_image(self):
            renpy.show(self.image, at_list=[self.transform])
        def hide_image(self):
            renpy.hide(self.image)

    tonysoprano = Enemy("Tony Soprano", "tonysoprano", 50, 2, "Bada Bing Blitz", "Gabagool Gut Punch", "Therapy Breakthrough")
    owlman = Enemy("Owl Man", "owlman", 40, 3, "Peck", "Moon Shatter", "Starry Appeal")