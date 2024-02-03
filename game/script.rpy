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

    scene desktopbg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show mainhall at backgroundpos
    
    # These display lines of dialogue.

    cl "You've created a new Ren'Py game."

    show cl at characterpos

    cl "Clairvoyant test"
    hide cl

    show s at characterpos

    s "Scholar test"
    hide s

    show p at characterpos

    p "Priest test"
    hide p

    show i at characterpos

    i "Investigator test"
    hide i

    show ca at characterpos

    ca "Caretaker test"
    hide ca

    show j at characterpos

    j "Journalist test"
    hide j

    # This ends the game.

    return
