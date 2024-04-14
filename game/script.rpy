init python:

    config.underlay.append(
        renpy.Keymap(
            mousedown_1 = lambda: renpy.run( renpy.play("click.ogg"))
        )
    )

image desktopbg = "desktopbackground.png"
image splash = "splashlogo.png"
image fmv = Movie(play="fmv.mpeg")

label splashscreen:
    scene black
    show screen crtoverlay
    
    with Pause(1)

    play sound "fishcough.mp3"

    show splash at truecenter with dissolve
    show text "{color=#fff}Smoking Fish Productions" at splash_text with dissolve

    with Pause(3)

    scene black with dissolve
    with Pause(1)

    show fmv at truecenter:
        zoom 1.5
    with Pause(14.5)

    return

# The game starts here.
$ minimap = False
label start:
    #This stops the main menu music from playing indefinitely
    stop music
    #This displays the crt effect as a screen overlay, this must be added to each scene (!!!)
    show screen crtoverlay
    #scene should always be desktopbg
    scene desktopbg
    $ minimap = False
    #This shows a background image, it must be at background pos to align correctly
    show maingate at backgroundpos
    with dissolve
    $ inv = Inventory([], 0)
    show screen hud
    "You stand before the iron gates of Derleth Manor, a gloomy mansion hidden in the woods near Arkham, Massachusetts. You have been hired to solve the mystery of what happened to August Derleth, the famous explorer who vanished without a trace."
    "A week ago, a mysterious man who called himself Sinclair Lewis approached you with an urgent plea for your assistance regarding Derleth. Lewis claimed to have learned of your expertise in dealing with occult phenomena, thanks to your reputation as a..."
    menu:
        "...respected scholar of the occult":
            $ charclass = "Scholar"
            $ strg = s_str
            $ dex = s_dex
            $ cha = s_cha
            $ per = s_per
            $ luck = s_luck
            $ baseHP = s_HP
            $ currentHP = s_HP
            jump sinclair_conversation
        "...renowned clairvoyant with the gift of second sight":
            $ charclass = "Clairvoyant"
            $ strg = cl_str
            $ dex = cl_dex
            $ cha = cl_cha
            $ per = cl_per
            $ luck = cl_luck
            $ baseHP = cl_HP
            $ currentHP = cl_HP
            jump sinclair_conversation    
        "...famed exorcist of the Arkham diocese":
            $ charclass = "Priest"
            $ strg = p_str
            $ dex = p_dex
            $ cha = p_cha
            $ per = p_per
            $ luck = p_luck
            $ baseHP = p_HP
            $ currentHP = p_HP
            jump sinclair_conversation                
        "...esteemed investigator of the paranormal":
            $ charclass = "Investigator"
            $ strg = i_str
            $ dex = i_dex
            $ cha = i_cha
            $ per = i_per
            $ luck = i_luck
            $ baseHP = i_HP
            $ currentHP = i_HP
            jump sinclair_conversation    
        "...fearless investigative journalist":
            $ charclass = "Journalist"
            $ strg = j_str
            $ dex = j_dex
            $ cha = j_cha
            $ per = j_per
            $ luck = j_luck
            $ baseHP = j_HP
            $ currentHP = j_HP
            jump sinclair_conversation    

label sinclair_conversation:
    show screen crtoverlay
    scene desktopbg
    show sinclairoffice at backgroundpos
    $ minimap = False
    with dissolve
    "On that day, Lewis had barged into your office, and began to plead with you."
    show sinclair at characterpos
    with dissolve
    "Sinclair" "Please, you have to help me find my friend. He's not himself anymore."
    "Sinclair" "Ever since he brought back that accursed thing from the mountains, he's been acting strange. I fear for his sanity, and his life!"
    hide sinclair
    with dissolve
    "After his outburst, he shoved a thick envelope into your hands. Upon opening it, you gasped at the amount of money inside. It was an advance for your services, far too tempting to refuse. Your curiousity was aroused, and you decided to hear the old man out."
    show sinclair at characterpos
    with dissolve
    "Sinclair" "My good friend August was an avid explorer who had dreamed of visiting the Himalayas for years. He finally made the journey and returned with a mysterious artifact that he found in a vast cave system on the mountain side. He called it the Shining Trapezohedron, a name that sent shivers down my spine."
    "Sinclair" "The artifact had a hold on him ever since he brought it home. He devoted all his time and energy to studying it, forsaking his sleep and well-being. A month ago his wife Evelyn wrote to me, alarmed by his increasingly erratic behaviour. Since then, I've heard no correspondence from either one of them."
    "Sinclair" "I dispatched one of my loyal servants to investigate. He returned with a grim report: the place was utterly deserted, as if the Derleths had vanished into thin air."
    "Sinclair" "However, after stopping by the local pub he heard all manner of rumors from the townsfolk. Reports of blood-curdling screams in the night, sinister figures lurking in the windows, and a palpable feeling of dread, chilling the bones of anyone who dared to come near."
    "Sinclair" "Ever since that dreadful day, my servant has been tormented by nightmares and panic. I am powerless to help the Derleths, you are the only one who can. You must go in my place and search for August. Find him and rescue him, before it is too late."
    hide sinclair
    with dissolve
    "You agreed to take on the perilous mission, tempted by the hefty reward that Sinclair offered. He wasted no time in leaving you alone, as if he wanted to distance himself from matters at hand. You quickly packed your essentials and prepared to face the unknown horrors that awaited you at Derleth Manor."
    if (charclass == "Priest"):
        $ inv.add_item(bible)
        $ inv.add_item(holywater)
        $ inv.add_item(bandage)
        $ inv.add_item(baconcabbagepotatoes)
        $ inv.add_item(beans)
    if (charclass == "Clairvoyant"):
        $ inv.add_item(bobbypins)
        $ inv.add_item(bandage)
        $ inv.add_item(meatpie)
        $ inv.add_item(sardines)
    if (charclass == "Journalist"):
        $ inv.add_item(parchment)
        $ inv.add_item(bandage)
        $ inv.add_item(bourbon)
        $ inv.add_item(cannedmeat)
    if (charclass == "Investigator"):
        $ inv.add_item(pistol)
        $ inv.add_item(lighter)
        $ inv.add_item(bandage)
        $ inv.add_item(bangersandmash)
        $ inv.add_item(bread)
    if (charclass == "Scholar"):
        $ inv.add_item(bobbypins)
        $ inv.add_item(bandage)
        $ inv.add_item(pills)
        $ inv.add_item(cannedmeat)
        $ inv.add_item(sardines)
    jump maingate


default slip_fail = False
default gate_fail = False
default ram_fail = False
default search_fail = False
label maingate:
    show screen crtoverlay
    scene desktopbg
    show maingate at backgroundpos
    with dissolve
    $ minimap = False

    #Precautionary failstate, as is no characters can fail this scene
    if (slip_fail == True and gate_fail == True and gate_fail == True and search_fail == True):
        "With all avenues exhausted, you decide to return home with your tail between your legs. Ho boy, Sinclair isn't going to be happy about this."
        return
    "You stand before the imposing main gate, its iron bars locked tight. You decide the smartest course of action is..."
    menu:
        "...to slip through the iron bars." if (slip_fail == False and dex > 5):
            "You effortless slip through the iron bars. Feeling proud of yourself, you head towards the manor with a skip in your step."
            jump front
        "...to slip through the iron bars." if (slip_fail == False and dex <= 5):
            "Your size makes it impossible to squeeze through the iron bars. You hold back the tears and put on a brave face."
            $ slip_fail = True
            jump maingate
        "...to climb the gate." if (gate_fail == False and strg > 5):
            "You hoist yourself over the gate and jog towards the manor."
            jump front
        "...to climb the gate." if (gate_fail == False and strg <= 5):
            "Right when you think you're on the verge of clearing the gate, you tumble down with a resounding thud."
            $ currentHP - 2
            $ renpy.notify("Lost 2 HP.")
            $ gate_fail = True
            jump maingate
        "...to ram the gate down!" if (ram_fail == False and strg >= 7):
            "You slam your powerful form against the gate, sending it crashing to the ground. You dust yourself off and head towards the manor. Are you proud of yourself?"
            $ aggression + 2
            jump front
        "... to ram the gate down!" if (ram_fail == False and strg < 7):
            "You hurl yourself at the gate with full confidence in your ability to bring it down. Guess what? This isn't an action game, all you manage to do is bruise your ribs."
            $ currentHP - 5
            $ renpy.notify("Lost 5 HP.")
            $ ram_fail = True
            jump maingate
        "...to look for an alternate route." if (search_fail == False and per > 5):
            "You discover a narrow opening in the bushes, guiding you to a large gap in the fence. You crawl through it, albeit at the expense of your dignity"
            jump front
        "...to look for an alternate route." if (search_fail == False and per <= 5):
            "Despite your efforts, you find no other methods of entry."
            jump maingate



label front:
    show screen crtoverlay
    scene desktopbg
    show front at backgroundpos
    with dissolve
    $ minimap = False

    "As you approach the grand manor, you notice an eerie sight: every window glows with an unnatural light. The closer you step, the more the air thickens, and a primal fear creeps up your spine. You dismiss it as mere imagination and push open the creaking front door."
    jump mainhall

label mainhall:
    default first_mainhall_visit = True
    default flee_attempt = False
    show screen crtoverlay
    scene desktopbg
    show bg mainhall at backgroundpos
    with dissolve
    $ minimap = True
    if (first_mainhall_visit == True):
        "As you step through the threshold, the door slams shut behind you."
    "This is the main hall. You can go to the west hallway, or the east hallway."
    $ first_mainhall_visit = False
    menu:
        "West Hallway":
            jump westhall
        "East Hallway":
            jump easthall
        "Flee in terror" if (flee_attempt == False):
            "You try with all your strength, but the door is locked tight. You're trapped in here."
            $ currentsanity -= 10
            $ renpy.notify("Lost 10 Sanity.")
            $ flee_attempt = True
            jump mainhall


##West Wing Hall Locations
label westhall:
    show screen crtoverlay
    scene desktopbg
    show bg westhall at backgroundpos
    with dissolve
    $ minimap = True
    call dice_roll
    if (d20 > 16):
        call battle(renpy.random.choice(easyenemies))

    "You are in the west hallway. There are two doors to your left, two to your right, and on down the hall."
    menu:
        "Go to the kitchen":
            jump kitchen
        "Enter the parlor." if (ornatekeyparlor in inv.items):
            jump parlor
        "Enter the parlor." if (ornatekeyparlor not in inv.items):
            "The parlor is locked tight."
            jump westhall
        "Search the dining room.":
            jump diningroom
        "Visit the servants quarters.":
            jump servantsquarters
        "Go to the greenhouse.":
            jump greenhouse
        "Return to the main hall.":
            jump mainhall

## Kitchen Variables
default tony_defeated = False
default fridge_empty = False
default inspect_sink = False
default sink_searched = False
default cupboard_searched = False

label kitchen:
    play sound "click.wav"
    show screen crtoverlay
    scene desktopbg
    show bg kitchen at backgroundpos
    with dissolve
    $ minimap = True
    call dice_roll
    if (d20 > 15 and tony_defeated == False):
        "You see a dark figure rustling through the fridge!"
        show tonysoprano at characterpos
        "Tony" "So you've come to take my gabagool, huh? You think you can just walk in here and help yourself? I don't think so, pal. That's mine, capisce? You want a taste, you gotta go through me. This ain't no free buffet!"
        call battle(tonysoprano)
        "With Tony disposed of, you gleefully pick up your hard earned coldcuts."
        $ inv.add_item(coldcuts)
        $ tony_defeated = True
    
    "This is the kitchen. The fridge is wide open. The sink is full of dirty water."
    menu:
        "Search the fridge.":
            if fridge_empty == False:
                "Mysteriously the fridge is packed with fresh food."
                $ inv.add_item(renpy.random.choice(food_list))
                $ inv.add_item(renpy.random.choice(food_list))
                $ inv.add_item(renpy.random.choice(alc_list))
                $ fridge_empty = True
                jump kitchen
            else:
                "You've already plundered the fridge."
                jump kitchen
        "Search the cupboards.":
            if per > 6 and cupboard_searched == False:
                "You find a roll of bandages behind an empty box of cornflakes."
                $ inv.add_item(bandage)
                $ cupboard_searched = True
                jump kitchen
            else:
                "You find nothing useful."
                jump kitchen
        "Inspect sink." if (inspect_sink == False):
            if per > 6:
                "You look into the dirty water and notice something glistening at the bottom of the sink."
                $ inspect_sink = True
                jump kitchen
            else:
                "It's full of dirty sink water. Big whoop!"
                jump kitchen
        "Search the sink." if (inspect_sink == True and sink_searched == False):
            "You plunge your hand into the disgusting water. Yuck, something slimey touched your hand. You resist the urge to scream and suddenly you feel something metal. You grasp your prize and pull out an old key."
            $ sink_searched = True
            $ inv.add_item(ornatekeyparlor)
            jump kitchen
        "Return to the West Hall.":
            jump westhall

default fireplace_inspected = False
default parlor_cabinet_inspected = False

label parlor:
    show screen crtoverlay
    scene desktopbg
    show bg parlor at backgroundpos
    with dissolve
    $ minimap = True

    "You are in the parlor. The walls are adorned with unsettling paintings, and you can feel a slight draft coming from the fireplace."
    menu:
        "Inspect the paintings.":
            call dice_roll
            if d4 == 1:
                show strangepainting at characterpos
                "The painting depicts a man surrounded by otherworldly monstrosities. Why anyone would want this on display is utterly beyond you."
                $ renpy.notify("Lost 5 sanity.")
                $ currentsanity -= 5
                jump parlor
            if d4 == 2:
                show menacingpainting at characterpos
                "A family portrait. One of their faces is contorted into a ghastly grimace. Something isn't right."
                $ renpy.notify("Lost 5 sanity.")
                $ currentsanity -= 5
                jump parlor
            if d4 == 3:
                show derlethpainting at characterpos
                "A painting of August and Evelyn Derleth. Finally, a face to put to the name."
                jump parlor
            if d4 == 4:
                call battle(hauntedportrait)
                jump parlor
        "Inspect the fireplace." if fireplace_inspected == False:
            "The draft emanating from the fireplace chills your very bones."
            if per > 5:
                "You spy a gap between the ornate woodwork of the fireplace's mantle. You slide your fingers across the mantle and feel a raised button in the center of a carving of a rose. You hear a loud click as you press it down and a hidden compartment opens."
                $ inv.add_item(evelyn_letter)
                $ fireplace_inspected = True
                jump parlor
            else:
                "You notice nothing out of the ordinary about the fireplace."
                $ fireplace_inspected = True
                jump parlor
        "Inspect the cabinet.":
            "You search through the cabinet."
            $ inv.add_item(renpy.random.choice(alc_list))
            $ inv.add_item(renpy.random.choice(med_list))
            jump parlor
        "Return to the West Hall.":
            jump westhall

label diningroom:
    show screen crtoverlay
    scene desktopbg
    show bg diningroom at backgroundpos
    with dissolve
    $ minimap = True

    "You are in the dining room."
    jump westhall

label servantsquarters:
    show screen crtoverlay
    scene desktopbg
    show bg servantsquarters at backgroundpos
    with dissolve
    $ minimap = True


    "You are in the servants quarters. There are two doors that lead off to the side."
    menu:
        "Go to the servant's bedroom.":
            jump servantsbedroom
        "Go to the storage room.":
            jump storageroom
        "Return to the west hallway.":
            jump westhall

label servantsbedroom:
    show screen crtoverlay
    scene desktopbg
    show bg servantsbedroom at backgroundpos
    with dissolve
    $ minimap = True

    "You are in the servants bedroom. There is strange writing on the walls."
    jump servantsquarters

label storageroom:
    show screen crtoverlay
    scene desktopbg
    show bg storageroom at backgroundpos
    with dissolve
    $ minimap = True

    "You are in the storage room."
    jump servantsquarters

label greenhouse:
    show screen crtoverlay
    scene desktopbg
    show bg greenhouse at backgroundpos
    with dissolve
    $ minimap = True

    "You are in the greenhouse."
    call dice_roll
    if (d20 > 16):
        call battle(renpy.random.choice(easyenemies))
    menu:
        "Venture outside.":
            jump garden
        "Return to the west hallway.":
            jump westhall

label garden:
    show screen crtoverlay
    scene desktopbg
    show bg garden at backgroundpos
    with dissolve
    $ minimap = True

    "You reach the garden."
    menu:
        "Search the shed.":
            jump shed
        "Pass through the gate.":
            jump graveyard
        "Return to the greenhouse.":
            jump greenhouse

label shed:
    show screen crtoverlay
    scene desktopbg
    show bg shed at backgroundpos
    with dissolve
    $ minimap = True

    "This is the shed."
    jump garden

label graveyard:
    show screen crtoverlay
    scene desktopbg
    show bg graveyard at backgroundpos
    with dissolve
    $ minimap = True

    "You are in the graveyard. Spoooky!"
    jump garden

## East Wing Hall Locations
label easthall:
    show screen crtoverlay
    scene desktopbg
    show bg easthall at backgroundpos
    with dissolve
    $ minimap = True

    call dice_roll
    if (d20 > 16):
        call battle(renpy.random.choice(easyenemies))
    "This is the east hallway. There are two doors to your left and one to your right. There is a staircase leading upstairs at the end of the hall."
    menu:
        "Go to the bathroom.":
            jump bathroom
        "Go to the study.":
            jump study
        "Go to the billiards room.":
            jump barroom
        "Climb the stairs.":
            jump eastupstairs
        "Return to the main hall.":
            jump mainhall

label bathroom:
    show screen crtoverlay
    scene desktopbg
    show bg bathroom at backgroundpos
    with dissolve
    $ minimap = True

    "This is the bathroom"
    jump easthall

label study:
    show screen crtoverlay
    scene desktopbg
    show bg study at backgroundpos
    with dissolve
    $ minimap = True

    "This is the study."
    jump easthall

label barroom:
    show screen crtoverlay
    scene desktopbg
    show bg barroom at backgroundpos
    with dissolve
    $ minimap = True

    "This is the bar room."
    jump easthall

#East upstairs hallway locations
label eastupstairs:
    show screen crtoverlay
    scene desktopbg
    show bg eastupstairs at backgroundpos
    with dissolve
    $ minimap = True

    call dice_roll
    if (d20 > 16):
        call battle(renpy.random.choice(easyenemies))
    "You are in the upstairs east hallway. There are two doors on each side of you and a door in front of you."
    menu:
        "Go to the master bedroom":
            jump bedroom
        "Go to the nursery":
            jump nursery
        "Go to the guest bedroom":
            jump secondbedroom
        "Go to the music room":
            jump musicroom
        "Go to the ballroom":
            jump ballroom
        "Return to the first floor":
            jump easthall

label bedroom:
    show screen crtoverlay
    scene desktopbg
    show bg bedroom at backgroundpos
    with dissolve
    $ minimap = True

    "The master bedroom."
    jump eastupstairs

label nursery:
    show screen crtoverlay
    scene desktopbg
    show bg nursery at backgroundpos
    with dissolve
    $ minimap = True

    "This is the nursery."
    jump eastupstairs

label secondbedroom:
    show screen crtoverlay
    scene desktopbg
    show bg secondbedroom at backgroundpos
    with dissolve
    $ minimap = True

    "This is the guest room."
    jump eastupstairs

label musicroom:
    show screen crtoverlay
    scene desktopbg
    show bg musicroom at backgroundpos
    with dissolve
    $ minimap = True

    "This is the music room."
    jump eastupstairs

label ballroom:
    show screen crtoverlay
    scene desktopbg
    show bg ballroom at backgroundpos
    with dissolve
    $ minimap = True

    "This is the ballroom."
    menu:
        "Go through the door.":
            jump westupstairs
        "Return to the east upstairs hall.":
            jump eastupstairs

#West Upstairs Locations
label westupstairs:
    show screen crtoverlay
    scene desktopbg
    show bg westupstairs at backgroundpos
    with dissolve
    $ minimap = True

    call dice_roll
    if (d20 > 16):
        call battle(renpy.random.choice(easyenemies))
    "There is a door to the Astronomy tower, a ladder to the attic ahead of you and a door to your right."
    menu:
        "Enter the Astronomy Tower.":
            jump astronomy
        "Go to the attic.":
            jump attic
        "Return to the ballroom.":
            jump ballroom

#astronomy tower variables
default owlman_defeated = False
default inspect_telescope = False
default telescope_fail = False
default telescope_success = False
default telescope_searched = False

label astronomy:
    show screen crtoverlay
    scene desktopbg
    show bg astronomytower at backgroundpos
    with dissolve
    $ minimap = True

    "This is the astronomy tower. There is a large telescope in the center of the room."
    menu:
        "Look through the telescope":
            if inspect_telescope == False:
                "You approach the telescope"
                call dice_roll
                if(d20 > 5 and owlman_defeated == False):
                    #Take sanity damage
                    "As you look through the telescope you do not see stars, but rather strange creatures and shapes flitting against a dark void."
                    "You feel a sense of primal revulsion, and are left with a feeling that you saw something you were not meant to see."
                    "As you process what you've just experienced, you hear an odd noise behind you."
                    show owlman at characterpos
                    "This being does not open its mouth to speak.  Its words rattle through your head, yet it speaks in a language unknown to you."
                    call battle(owlman)
                    "The odd creature disappears in a flash of light that leaves you momentarily stunned. When you regain your senses it's gone."
                    $ owlman_defeated = True
                    $ inspect_telescope = True
                    jump astronomy
                elif(d20 <= 5 and owlman_defeated == False):
                    "As you look through the telescope you feel a sense of wonder and euphoria rush over you.  A sense of discovery and fulfillment you have not felt in some time.  You feel yourself transported across the great expanse of the void, taking in the experiences and comforts of a thousand lifetimes."
                    "When you pull your head away from the telescope you feel a precense in the room with you."
                    show owlman at characterpos
                    "The odd creature before you nods its head towards you.  A gesture of friendship, perhaps?  It disappears in a flash of bright light, leaving you temporarily blinded."  "
                    When you regain your senses, however; you feel a sense of ease wash over you.  You look around the room and notice an item that was not there before."  
                    #restore sanity
                    $ inv.add_item(renpy.random.choice(mid_tier_weapon))
                    "A gift from the strange creature. perhaps?"
                    $ owlman_defeated = True
                    $ inspect_telescope = True
                    jump astronomy
            else: 
                "You already inspected the telescope."
                jump astronomy

        "Search the shelves.":
            call dice_roll
            if (d20 >= 10):
                "You find a few helpful goods"
                $ inv.add_item(renpy.random.choice(tool_list))
                $ inv.add_item(renpy.random.choice(tool_list))
                #$ inv.add_item(bandages)
                jump astronomy
            else:
                "You find a few rotted scrolls and books, but nothing else of note."
                jump astronomy
        "Leave the room":
            jump westupstairs

label attic:
    show screen crtoverlay
    scene desktopbg
    show bg attic at backgroundpos
    with dissolve
    $ minimap = True

    call dice_roll
    if (d20 > 16):
        call battle(renpy.random.choice(easyenemies))
    "You are in the attic. There is a door in front of you."
    menu:
        "Enter the door.":
            jump sceanceroom
        "Return to the West upstairs hall.":
            jump westupstairs

label sceanceroom:
    show screen crtoverlay
    scene desktopbg
    show bg sceanceroom at backgroundpos
    with dissolve
    $ minimap = True

    "This is the sceance room."
    jump attic

label use_item(item):
    $ item.use()
    if currentHP > 24:
        hide screen healthoverlay
    return

##Battle labels - Marlene

label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

init: 
    $ combat_start = renpy.random.choice (["lunges at", "stomps over to", "crawls toward", "runs at", "stares menacingly at", "ambushes", "corners", "attacks", "preys on", "strikes", "schemes against"])

label battle(enemy):
    $ player_attack = 0
    $ enemyHP = enemy.HP
    $ enemyMaxHP = enemy.HP
    $ enemyHasHealed = False
    $ enemy.show_image()
    "Surprise attack!"
    "[enemy.name] [combat_start] you."
    show screen hp_bars_1v1

    while currentHP > 0 and enemyHP > 0:
        call dice_roll
        menu:
            "Light Attack":
                if d10 >= 7:
                    $ player_attack = d4 + d6 + dex + dmgmod
                    $ enemyHP -= player_attack
                    "Critical Hit! [player_attack] damage to [enemy.name]!"
                else:
                    $ player_attack = d4 + dex + dmgmod
                    $ enemyHP -= player_attack
                    "[player_attack] damage dealt."
            "Heavy Attack":
                if d10 >= 8:
                    $ player_attack = d6 + d4 + strg + dmgmod
                    $ enemyHP -= player_attack
                    "Massive Damage! [player_attack] damage. [enemy.name] looks dazed."
                elif d10 >= 5:
                    $ player_attack = d6 + 2 + strg + dmgmod
                    $ enemyHP -= player_attack
                    "Critical Hit! [player_attack] damage to [enemy.name]!"
                else:
                    "[enemy.name] dodges the attack."

        if enemyHP <= 0:
            "[enemy.name] defeated!"
            $ enemy.hide_image() 
            hide screen hp_bars_1v1
            return

        call dice_roll
               
        if not (enemyHP > 0 and enemyHP < 20) or enemyHasHealed is True:
            if d20 >= 19:
                $ enemyCrit = d6 * enemy.attackModifier 
                $ currentHP -= enemyCrit
                "[enemy.name] makes a wild attack for [enemyCrit] damage!"
            elif d20 >=16:
                $ add_or_sub = renpy.random.randint(0,1)
                if add_or_sub == 0:
                    $ sp1dmg = enemy.sp1dmg + d4
                else: 
                    $ sp1dmg = enemy.sp1dmg - d6
                $ currentHP -= sp1dmg
                "[enemy.sp1text] It hits for [sp1dmg]." 
            elif d20 >=12:
                $ add_or_sub = renpy.random.randint(0,1)
                if add_or_sub == 0:
                    $ sp2dmg = enemy.sp2dmg + d4
                else: 
                    $ sp2dmg = enemy.sp2dmg - d6
                $ currentHP -= sp2dmg
                "[enemy.sp2text] It hits for [sp2dmg]." 
            else:
                $ enemyAttack = d6 + enemy.attackModifier
                $ currentHP -= enemyAttack
                "[enemy.name] attacks for [enemyAttack] damage."
        else:
                "[enemy.name] healed themselves using [enemy.healingMove]!"
                $ enemyHP += 10
                $ enemyHasHealed = True
        if currentHP < 25:
            show screen healthoverlay
    ## while loop exit, game over
    "Your vision goes black, your body feels cold. This is where your journey ends."
    hide screen hp_bars_1v1
    scene black with fade
    $ MainMenu(confirm=False)()






