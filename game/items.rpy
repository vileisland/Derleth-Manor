init python:
    import random
    class Inventory():
        def __init__(self, item, no_of_items):
            self.items = item

        def add_item(self, item):
            self.items.append(item)
            item.recieve()

        def remove_item(self, item):
            self.items.remove(item)
            item.use()

    class Item:
        def __init__(self, name, description, image):
            self.name = name
            self.description = description
            self.image = image
            self.transform = characterpos
        ##display name
        def d_name(self):
            narrator(f"{self.name}")
        ##display description
        def d_description(self):
            narrator(f"{self.description}")
        def recieve(self):
            renpy.show(self.image, at_list=[self.transform])
            renpy.say("", what=f"Recieved {self.name}.")
            renpy.hide(self.image)
        def use(self):
            renpy.show(self.image, at_list=[self.transform])
            renpy.text(f"Used {self.name}.")
            renpy.hide(self.image)

    class Heal(Item):
        def __init__(self, name, description, image, healpts):
            super().__init__(name, description, image)
            self.healpts = healpts

        ##display healing points
        def d_heal(self):
            narrator(f"Heals {self.healpts} health.")
        def recieve(self):
            renpy.show(self.image, at_list=[self.transform])
            renpy.say("", what=f"Recieved {self.name}.")
            renpy.hide(self.image)
        ##Use healing item
        def use(self):
            global currentHP
            global baseHP
            currentHP += self.healpts
            if (currentHP > baseHP):
                currentHP = baseHP
            renpy.show(self.image, at_list=[self.transform])
            renpy.say("", what=f"Used {self.name}, it restored your health by {self.healpts}. Your health is now {currentHP}.)
            renpy.hide(self.image)
            inv.items.remove(item)

    class Sanity(Item):
        def __init__(self, name, description, image, sanitypts):
            super().__init__(name, description, image)
            self.sanitypts = sanitypts
        ##display healing points
        def d_sanity(self):
            narrator(f"Heals {self.sanitypts} sanity.")

        ##Use sanity healing item
        def use(self):
            renpy.show(self.image, at_list=[self.transform])
            renpy.say("", what=f"Used {self.name}, it restored your sanity by {self.sanitypts}. Your sanity is now {currentsanity}.")
            currentsanity += self.sanitypts
            if (currentsanity > basesanity):
                currentsanity = basesanity
            renpy.hide(self.image)
            inv.items.remove(item)

    class Weapon(Item):
        def __init__(self, name, description, image, attackpts):
            super().__init__(name, description, image)
            self.attackpts = attackpts
        def d_attack(self):
            narrator(f"Attack strength: {self.attackpts}.")

    class Tool(Item):
        def __init__(self, name, description, image, combine):
            super().__init__(name, description, image)
            self.combine = combine

    ##Food items
    baconcabbagepotatoes = Heal("Bacon, Cabbage, and Potatoes", "A hearty Irish feast.", "baconcabbagepotatoes", 18)
    bangersandmash = Heal("Bangers and Mash", "Delicious British slop.", "bangersandmash", 15)
    beans = Heal("Beans", "A cold cup of Beans.", "beans", 5)
    bread = Heal("Bread slices", "The beginnings of a sandwich.", "bread", 5)
    burger = Heal("Cheeseburger", "A juicy slab of grease.", "burger", 25)
    cannedmeat = Heal("Canned Meat", "A canned delicacy.", "cannedmeat", 8)
    coldcuts = Heal("Cold cuts", "Best eaten with bare hands.", "coldcuts", 10)
    fishandchips = Heal("Fish and chips", "The perfect pair.", "fishandchips", 10)
    hamandcrackers = Heal("Ham and crackers", "A quick snack.", "hamandcrackers", 8)
    jelliedeels = Heal("Jellied Eels", "Looking at it makes you queasy", "jelliedeels", 5)
    meatpie = Heal("Meat pie", "Just like ma used to make.", "meatpie", 12)
    pancakes = Heal("Pancakes", "Stack 'em up.", "pancakes", 12)
    parfait = Heal("Parfait", "A child's treat.", "parfait", 8)
    pierogi = Heal("Pierogi", "Straight from the old country.", "pierogi", 12)
    roastbeef = Heal("Roast Beef", "Rare, just how you like it.", "roastbeef", 25)
    sardines = Heal("Sardines", "Lined up like soldiers.", "sardines", 8)
    spaghetti = Heal("Spaghetti", "That's a spicy meatball!", "spaghetti", 18)
    steak = Heal("Steak", "Perfectly seared.", "steak", 25)
    stickytoffeepudding = Heal("Sticky toffee pudding", "Oh, that's moist!", "stickytoffeepudding", 12)

    ##Alcohol
    absinthe = Sanity("Absinthe", "Popular in paris.", "absinthe", 10)
    bourbon = Sanity("Bourbon", "Southern comfort.", "bourbon", 15)
    gin = Sanity("Gin", "Rich in botanicals.", "gin", 15)

    ##Medicine
    bandage = Heal("Bandage", "Perfect for soaking up blood.", "bandage", 30)
    chewingtobacco = Sanity("Chewing tobacco", "Better get your spitpot ready.", "chewingtobacco", 20)
    laudenum = Sanity("Laudenum", "Better not abuse it.", "laudenum", 25)
    leeches = Heal("Leeches", "Drains you of bad blood", "leeches", 15)
    pills = Sanity("Pills", "A little mystery pill never hurt anybody.", "pills", 20)
    pipe = Sanity("Pipe", "Smoke 'em if you got 'em.", "pipe", 15)
    smellingsalts = Sanity("Smelling Salts", "Not just for fainting dames.", "smellingsalts", 10)

    ##Tools - must add combine later
    bible = Tool("Bible", "Extra thick.", "bible", "")
    bobbypins = Tool("Bobby pins", "A whole box of them!", "bobbypins", "")
    ducttape = Tool("Duct tape", "For fixin' things.", "ducttape", "")
    hammer = Tool("Hammer", "Watch out nails, I'm coming for you.", "hammer", "")
    holywater = Tool("Holy water", "Back, foul demon!", "holywater", "")
    letter = Tool("Letter", "It's a crime to read this.", "letter", "")
    lighter = Tool("Lighter", "Time for arson.", "lighter", "")
    nails = Tool("Nails", "A hammers best friend.", "nails", "")
    ornatekey = Tool("Ornate key", "This must open something specific.", "ornatekey", "")
    key = Tool("Key", "Now all you need to do is find a lock.", "key", "")
    parchment = Tool("Parchment", "Something to write your thoughts down on.", "parchment", "")
    saw = Tool("Saw", "For sawin' stuff.", "saw", "")
    shovel = Tool("Shovel", "Strike the earth!", "shovel", "")
    wrench = Tool("Wrench", "Hey, who needs a plumber?", "wrench", "")

    ##Weapons
    axe = Weapon("Axe", "Looks sturdy", "axe", 5)
    crossbow = Weapon("Crossbow", "Not just for hunting deer.", "crossbow", 12)
    huntingknife = Weapon("Hunting knife", "Lightweight and practical.", "huntingknife", 5)
    mace = Weapon("Mace", "Ornate and heavy", "mace", 8)
    pistol = Weapon("Pistol", "It packs a punch.", "pistol", 12)
    rifle = Weapon("Rifle", "Perfect for long range combat.", "rifle", 15)
    scythe = Weapon("Scythe", "From the gim reaper's arsenal.", "scythe", 8)
    sword = Weapon("Crystal Sword", "It takes a dark soul to wield this.", "sword", 20)

    ##Item lists
    food_list = [baconcabbagepotatoes, bangersandmash, beans, bread, burger, cannedmeat, coldcuts, fishandchips, hamandcrackers, jelliedeels, meatpie, pancakes, parfait, pierogi, 
    roastbeef, sardines, spaghetti, steak, stickytoffeepudding]
    alc_list = [absinthe, bourbon, gin]
    med_list = [bandage, chewingtobacco, laudenum, leeches, pills, pipe, smellingsalts]
    tool_list = [bible, bobbypins, ducttape, hammer, holywater, letter, lighter, nails, ornatekey, key, parchment, saw, shovel, wrench]
    low_tier_weapon = [axe, huntingknife, mace, scythe]
    mid_tier_weapon = [crossbow, pistol, rifle]
    high_tier_weapon = [sword]