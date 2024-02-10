﻿
image desktopbg = "desktopbackground.png"

#Location images
image mainhallway = "locations/mainhall.png"

label splashscreen:
    scene black
    show screen crtoverlay
    
    with Pause(1)

    play sound "fishcough.mp3"

    show splashlogo at truecenter with dissolve
    show text "Smoking Fish Productions" at splash_text

    with Pause(3)

    scene black with dissolve
    with Pause(1)

    return

# The game starts here.

label start:
    #This stops the main menu music from playing indefinitely
    stop music
    #This displays the crt effect as a screen overlay, this must be added to each scene (!!!)
    show screen crtoverlay
    #scene should always be desktopbg
    scene desktopbg

    #This shows a background image, it must be at background pos to align correctly
    show maingate at backgroundpos
    with dissolve
    "You stand before the iron gates of Derleth Manor, a gloomy mansion hidden in the woods near Arkham, Massachusetts. You have been hired to solve the mystery of what happened to August Derleth, the famous explorer who vanished without a trace."
    "A week ago, a mysterious man who called himself Sinclair Lewis approached you with an urgent plea for your assistance regarding Derleth. Lewis claimed to have learned of your expertise in dealing with occult phenomena, thanks to your reputation as a..."
    menu:
        "...respected scholar of the occult":
            $ charclass = "scholar"
            $ strg = s_str
            $ dex = s_dex
            $ cha = s_cha
            $ per = s_per
            $ luck = s_luck
            $ HP = s_HP
            jump sinclair_conversation
        "...renowned clairvoyant with the gift of second sight":
            $ charclass = "clairvoyant"
            $ strg = cl_str
            $ dex = cl_dex
            $ cha = cl_cha
            $ per = cl_per
            $ luck = cl_luck
            $ HP = cl_HP
            jump sinclair_conversation    
        "...famed exorcist of the Arkham diocese":
            $ charclass = "priest"
            $ strg = p_str
            $ dex = p_dex
            $ cha = p_cha
            $ per = p_per
            $ luck = p_luck
            $ HP = p_HP
            jump sinclair_conversation                
        "...esteemed investigator of the paranormal":
            $ charclass = "investigator"
            $ strg = i_str
            $ dex = i_dex
            $ cha = i_cha
            $ per = i_per
            $ luck = i_luck
            $ HP = i_HP
            jump sinclair_conversation    
        "...fearless investigative journalist":
            $ charclass = "journalist"
            $ strg = j_str
            $ dex = j_dex
            $ cha = j_cha
            $ per = j_per
            $ luck = j_luck
            $ HP = j_HP
            jump sinclair_conversation    

label sinclair_conversation:
    show screen crtoverlay
    scene desktopbg
    show sinclairoffice at backgroundpos
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
            $ HP - 2
            $ renpy.notify("Lost 2 HP.")
            $ gate_fail = True
            jump maingate
        "...to ram the gate down!" if (ram_fail == False and strg >= 7):
            "You slam your powerful form against the gate, sending it crashing to the ground. You dust yourself off and head towards the manor. Are you proud of yourself?"
            $ agression + 2
            jump front
        "... to ram the gate down!" if (ram_fail == False and strg < 7):
            "You hurl yourself at the gate with full confidence in your ability to bring it down. Guess what? This isn't an action game, all you manage to do is bruise your ribs."
            $ HP - 5
            $ renpy.notify("Lost 5 HP.")
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

    "As you approach the grand manor, you notice an eerie sight: every window glows with an unnatural light. The closer you step, the more the air thickens, and a primal fear creeps up your spine. You dismiss it as mere imagination and push open the creaking front door."
    jump mainhall

label mainhall:
    default first_mainhall_visit = True
    default flee_attempt = False
    show screen crtoverlay
    scene desktopbg
    show mainhall at backgroundpos
    with dissolve
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
            $ flee_attempt = True
            jump mainhall


##West Wing Hall Locations
label westhall:
    show screen crtoverlay
    scene desktopbg
    show westhall at backgroundpos
    with dissolve

    "You are in the west hallway. There are two doors to your left, two to your right, and on down the hall."
    menu:
        "Go to the kitchen":
            jump kitchen
        "Enter the parlor.":
            jump parlor
        "Search the dining room.":
            jump diningroom
        "Visit the servants quarters.":
            jump servantsquarters
        "Go to the greenhouse.":
            jump greenhouse
        "Return to the main hall.":
            jump mainhall

label kitchen:
    show screen crtoverlay
    scene desktopbg
    show kitchen at backgroundpos
    with dissolve

    "This is the kitchen. The fridge is wide open."
    jump westhall

label parlor:
    show screen crtoverlay
    scene desktopbg
    show parlor at backgroundpos
    with dissolve

    "You are in the parlor. It's a mess."
    jump westhall

label diningroom:
    show screen crtoverlay
    scene desktopbg
    show diningroom at backgroundpos
    with dissolve

    "You are in the dining room."
    jump westhall

label servantsquarters:
    show screen crtoverlay
    scene desktopbg
    show servantsquarters at backgroundpos
    with dissolve

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
    show servantsbedroom at backgroundpos
    with dissolve

    "You are in the servants bedroom. There is strange writing on the walls."
    jump servantsquarters

label storageroom:
    show screen crtoverlay
    scene desktopbg
    show storageroom at backgroundpos
    with dissolve

    "You are in the storage room."
    jump servantsquarters

label greenhouse:
    show screen crtoverlay
    scene desktopbg
    show greenhouse at backgroundpos
    with dissolve

    "You are in the greenhouse."
    menu:
        "Venture outside.":
            jump garden
        "Return to the west hallway.":
            jump westhall

label garden:
    show screen crtoverlay
    scene desktopbg
    show garden at backgroundpos
    with dissolve

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
    show shed at backgroundpos
    with dissolve

    "This is the shed."
    jump garden

label graveyard:
    show screen crtoverlay
    scene desktopbg
    show graveyard at backgroundpos
    with dissolve

    "You are in the graveyard. Spoooky!"
    jump garden

## East Wing Hall Locations
label easthall:
    show screen crtoverlay
    scene desktopbg
    show easthall at backgroundpos
    with dissolve

    "This is the east hallway. There are two doors to your left and one to your right. There is a staircase leading upstairs at the ened of the hall."
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
    show bathroom at backgroundpos
    with dissolve

    "This is the bathroom"
    jump easthall

label study:
    show screen crtoverlay
    scene desktopbg
    show study at backgroundpos
    with dissolve

    "This is the study."
    jump easthall

label barroom:
    show screen crtoverlay
    scene desktopbg
    show barroom at backgroundpos
    with dissolve

    "This is the bar room."
    jump easthall

#East upstairs hallway locations
label eastupstairs:
    show screen crtoverlay
    scene desktopbg
    show eastupstairs at backgroundpos
    with dissolve

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

label bedroom:
    show screen crtoverlay
    scene desktopbg
    show bedroom at backgroundpos
    with dissolve

    "The master bedroom."
    jump eastupstairs

label nursery:
    show screen crtoverlay
    scene desktopbg
    show nursery at backgroundpos
    with dissolve

    "This is the nursery."
    jump eastupstairs

label secondbedroom:
    show screen crtoverlay
    scene desktopbg
    show secondbedroom at backgroundpos
    with dissolve

    "This is the guest room."
    jump eastupstairs

label musicroom:
    show screen crtoverlay
    scene desktopbg
    show musicroom at backgroundpos
    with dissolve

    "This is the music room."
    jump eastupstairs

label ballroom:
    show screen crtoverlay
    scene desktopbg
    show ballroom at backgroundpos
    with dissolve

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
    show westupstairs at backgroundpos
    with dissolve

    "There are two doors here. I haven't thought of any locations for them. Ignore them. There is a ladder to the attic ahead of you."
    menu:
        "Go to the attic.":
            jump attic
        "Return to the ballroom.":
            jump ballroom

label attic:
    show screen crtoverlay
    scene desktopbg
    show attic at backgroundpos
    with dissolve

    "You are in the attic. There is a door in front of you."
    menu:
        "Enter the door.":
            jump sceanceroom
        "Return to the West upstairs hall.":
            jump westupstairs

label sceanceroom:
    show screen crtoverlay
    scene desktopbg
    show sceanceroom at backgroundpos
    with dissolve

    "This is the sceance room."
    jump attic