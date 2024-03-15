screen hud():
    modal False

    imagebutton idle "characterstats.png":
        focus_mask None
        pos (10, 100)
        action Show("stats")

    imagebutton idle "map.png":
        focus_mask None
        pos(10, 261)
        action Show("status"), Hide("hud")

    imagebutton idle "inventory.png":
        focus_mask None
        pos (10, 422)
        action Show("inventory")


screen inventory():
    modal True
    add "nvl.png"

    vbox:
        pos 0.2, 0.10
        for item in inv.items:
            #text "[item.name] - [item.description]"
            textbutton ("[item.name] - [item.description]"):
                action Hide("inventory"), Call("use_item", item)
        

    imagebutton idle "closebutton.png":
        focus_mask None
        action Hide("inventory"), Show("hud")

screen stats():
    modal True
    add "nvl.png"

    vbox:
        pos 0.2, 0.10
        text "[charclass]"
        image "images/cportraits/[charclass]por.png"
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
        action Hide("stats"), Show("hud")