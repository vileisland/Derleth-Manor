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
    angel = Enemy("Angel", "angel", 35, 2, "Heavenly Judgement", 15, "The Angel channels divine energy. Celestial arrows buffet you.", "Wings of Retribution", 20, "The Angel slams into you with it's razor sharp wings.", "Ethereal Choir")
    banshee = Enemy("Banshee", "banshee", 55, 5, "Wail", 15, "The banshee let's out a haunting scream. It pierces your ears.", "Withering Touch", 20, "The Banshee reachs out with it's spectral hand, You can feel your life force drain away.", "Sidhe's Embrace")
    carniverous = Enemy("Carniverous", "carniverous", 60, 5, "Vine Whip", 10, "Carniverous lashes out with it's sinewy vines.", "Root Surge", 15, "Roots erupt from the earth, knocking you down.", "Photosynthesis Overdrive")
    cultleader = Enemy("Cult Leader", "cultleader", 35, 5, "Eldritch Invocation", 15, "The cult leader channels forbidden knowledge, calling forth a writhing mass of tentacles to strike at you.", "Cursed Glyph", 18, "The cult leader summons a glyph beneath your feet, it erupts with dark energy.", "Resonant Chant")
    eldritch = Enemy("Eldritch", "eldritch", 70, 8, "Abyssal Tempest", 18, "The Eldritch conjures a swirling vortext of dark energy.", "Cosmic Nova", 12, "Primordial energy tears through you.", "Apocalyptic Rebirth")
    hauntedportrait = Enemy("Haunted Portrait", "hauntedportrait", 20, 4, "Frame Fracture", 25, "The Portrait's glass shatters, barraging you with shards of broken glass.", "Canvas Catastrophe", 25, "The Portrait charges at you, knocking you over.", "Restorative Reverie")
    imp = Enemy("Imp", "imp", 30, 2, "Sneaky Stab", 8, "The Imp swiftly lunges at you with dagger in hand.", "Shadow Step", 12, "The Imp vanishes into the shadows, reappearing behind you to deliver a nasty blow.", "Fiendish Renewal")
    mindflayer = Enemy("Mindflayer", "mindflayer", 80, 8, "Mind Blast", 25, "The Mindflayer emits a powerful psychic shockwave.", "Psychic Assault", 27, "The Mindflayer unleashes a barrage of telekinetic energy.", "Telepathic Recovery")
    mummy = Enemy("Mummy", "mummy", 35, 3, "Sarcophagus Slam", 15, "The mummy summons a spectral sarcophagus, slamming it down onto you.", "Plague of Locusts", 12, "The mummy calls forth a swarn of locusts that gnaw at you from every angle.", "Sands of Renewal")
    oldone = Enemy("Old One", "oldone", 100, 10, "Primordial Roar", 20, "The Old One lets out a maddening roar, rupturing your ear drums.", "Apocalyptic Annihilation", 30, "The Old One unleashes a cataclysmic surge of eldritch power.", "Void's Blessing")

    easyenemies = [angel, cultleader, imp, mummy]