# The script of the game goes in this file.

# Splash Screen
image splash = "splashlogo.png"
image desktopbg = "desktopbackground.png"

#Location images
image mainhallway = "locations/mainhall.png"

label splashscreen:
    scene black
    show screen crtoverlay
    
    with Pause(1)

    play sound "fishcough.mp3"

    show splash at truecenter with dissolve
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
    "On that day, Lewis had barged into your office, and began to plead with you."
    show sinclair at characterpos
    "Sinclair" "Please, you have to help me find my friend. He's not himself anymore."
    "Sinclair" "Ever since he brought back that accursed thing from the mountains, he's been acting strange. I fear for his sanity, and his life!"
    hide sinclair
    "After his outburst, he shoved a thick envelope into your hands. Upon opening it, you gasped at the amount of money inside. It was an advance for your services, far too tempting to refuse. Your curiousity was aroused, and you decided to hear the old man out."
    show sinclair at characterpos
    "Sinclair" "My good friend August was an avid explorer who had dreamed of visiting the Himalayas for years. He finally made the journey and returned with a mysterious artifact that he found in a vast cave system on the mountain side. He called it the Shining Trapezohedron, a name that sent shivers down my spine."
    "Sinclair" "The artifact had a hold on him ever since he brought it home. He devoted all his time and energy to studying it, forsaking his sleep and well-being. A month ago his wife Evelyn wrote to me, alarmed by his increasingly erratic behaviour. Since then, I've heard no correspondence from either one of them."
    "Sinclair" "I dispatched one of my loyal servants to investigate. He returned with a grim report: the place was utterly deserted, as if the Derleths had vanished into thin air."
    "Sinclair" "However, after stopping by the local pub he heard all manner of rumors from the townsfolk. Reports of blood-curdling screams in the night, sinister figures lurking in the windows, and a palpable feeling of dread, chilling the bones of anyone who dared to come near."
    "Sinclair" "Ever since that dreadful day, my servant has been tormented by nightmares and panic. I am powerless to help the Derleths, you are the only one who can. You must go in my place and search for August. Find him and rescue him, before it is too late."
    hide sinclair
    "You agreed to take on the perilous mission, tempted by the hefty reward that Sinclair offered. He wasted no time in leaving you alone, as if he wanted to distance himself from matters at hand. You quickly packed your essentials and prepared to face the unknown horrors that awaited you at Derleth Manor."
    jump maingate

label maingate:
    show screen crtoverlay
    scene desktopbg
    show maingate at backgroundpos
    "You are a [charclass], your strength stat is [strg], your dex stat is [dex], your charisma stat is [cha], your perception stat is [per], your luck stat is [luck], your HP is [HP]."

    return
