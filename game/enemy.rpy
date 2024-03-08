init python:
    import random
    class Enemy:
        def __init__(self, name, image, HP):
            self.name = name
            self.image = image
            self.transform = characterpos
            self.HP = HP
            self.transform = characterpos
        def show_image(self):
            renpy.show(self.image, at_list=[self.transform])
        def hide_image(self):
            renpy.hide(self.image)

    tonysoprano = Enemy("Tony Soprano", "tonysoprano", 50)