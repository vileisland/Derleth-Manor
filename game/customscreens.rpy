screen hud():
    modal False

    imagebutton idle "characterstats.png":
        focus_mask None
        pos (10, 100)
        action Show("stats")

    imagebutton idle "map.png":
        focus_mask None
        pos(10, 261)
        action Show("map")

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