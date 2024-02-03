# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Clairvoyant", image="cportrait/clairvoyant.png")

# Splash Screen
image splash = "splashlogo.png"
image desktopbg = "desktopbackground.png"

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

    show clairvoyant at topmiddle

    # These display lines of dialogue.

    c "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
