screen hud():
    modal False

    imagebutton idle "characterstats.png":
        focus_mask None
        pos (10, 100)
        action Play("sound", "click.ogg"), Show("stats")

    imagebutton idle "map.png":
        focus_mask None
        pos(10, 261)
        action Play("sound", "click.ogg"), Show("status"), Hide("hud")

    imagebutton idle "inventory.png":
        focus_mask None
        pos (10, 422)
        action Play("sound", "click.ogg"), Show("inventory")


screen inventory():
    modal True
    add "nvl.png"

    vbox:
        pos 0.2, 0.10
        text "Key Items:"
        text " "
        for item in inv.items:
            if isinstance(item, (Tool)):
                text " [item.name] - [item.description]"
        text " "
        text "Useables:"
        text " "
        for item in inv.items:
            if isinstance(item, (Heal, Sanity, Weapon, Letter)):
                textbutton ("[item.name] - [item.description]"):
                    action Play('sound', 'click.ogg'), Hide("inventory"), Call("use_item", item, from_current=True)
        

    imagebutton idle "closebutton.png":
        focus_mask None
        action Play("sound", "click.ogg"), Hide("inventory"), Show("hud")

screen stats():
    modal True
    add "nvl.png"

    vbox:
        pos 0.2, 0.10
        text "[charclass]"
        text " "
        image "images/cportraits/[charclass]por.png"
        text " "
        text "Health: [currentHP]/[baseHP]"
        text "Sanity: [currentsanity]/[basesanity]"
        text "Strength: [strg]"
        text "Dexterity: [dex]"
        text "Charisma: [cha]"
        text "Perception: [per]"
        text "Luck: [luck]"
        text "Weapon equipped: [weapon]"
        text "Weapon damage: [dmgmod]"
        

    imagebutton idle "closebutton.png":
        focus_mask None
        action Play("sound", "click.ogg"), Hide("stats"), Show("hud")