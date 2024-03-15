init python:
    import random
    class Enemy:
        def __init__(self, name, image, HP, attackModifier, specialAttack1, sp1dmg, sp1text, specialAttack2, sp2dmg, sp2text, healingMove):
            self.name = name
            self.image = image
            self.transform = characterpos
            self.HP = HP
            self.attackModifier = attackModifier
            self.specialAttack1 = specialAttack1
            self.sp1dmg = sp1dmg
            self.sp1text = sp1text
            self.specialAttack2 = specialAttack2
            self.sp2dmg = sp2dmg
            self.sp2text = sp2text
            self.healingMove = healingMove
            self.transform = characterpos
        def show_image(self):
            renpy.show(self.image, at_list=[self.transform])
        def hide_image(self):
            renpy.hide(self.image)

    tonysoprano = Enemy("Tony Soprano", "tonysoprano", 50, 2, "Bada Bing Blitz", 25, "Tony Soprano lunges at you with flurry of punches and kicks.", "Gabagool Gut Punch", 15, "Tony Soprano focuses his energy into his fist and unleashes a devastating right hook to your abdomen.", "Therapy Breakthrough")
    owlman = Enemy("Owl Man", "owlman", 40, 3, "Peck", 10, "Ryan add something here.", "Moon Shatter", 10, "Ryan add something here.", "Starry Appeal")