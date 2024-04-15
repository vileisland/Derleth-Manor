
#Location images
image bg attic = "/images/locations/attic.png"
image bg ballroom = "/images/locations/ballroom.png"
image bg barroom = "/images/locations/barroom.png"
image bg bathroom = "/images/locations/bathroom.png"
image bg bedroom = "/images/locations/bedroom.png"
image bg diningroom = "/images/locations/diningroom.png"
image bg easthall = "/images/locations/easthall.png"
image bg eastupstairs = "/images/locations/eastupstairs.png"
#image bg front = "/images/locations/front.png"
image bg garden = "/images/locations/garden.png"
image bg graveyard = "/images/locations/graveyard.png"
image bg greenhouse = "/images/locations/greenhouse.png"
image bg kitchen = "/images/locations/kitchen.png"
image maingate = "/images/locations/maingate.png"
image bg mainhall = "/images/locations/mainhall.png"
image bg musicroom = "/images/locations/musicroom.png"
image bg nursery = "/images/locations/nursery.png"
image bg parlor = "/images/locations/parlor.png"
image bg sceanceroom = "/images/locations/sceanceroom.png"
image bg secondbedroom = "/images/locations/secondbedroom.png"
image bg servantsbedroom = "/images/locations/servantsbedroom.png"
image bg servantsquarters = "/images/locations/servantsquarters.png"
image bg shed = "/images/locations/shed.png"
image bg storageroom = "/images/locations/storageroom.png"
image bg study = "/images/locations/study.png"
image bg westhall = "/images/locations/westhall.png"
image bg westupstairs = "/images/locations/westupstairs.png"


define locations = {
    "astronomytower" : {"name":_("Astronomy Tower"), "area":2, "pos":( 0, 0)},

    "attic" : {"name":_("The Attic"), "area":2, "pos":( 0, 0)},

    "ballroom" : {"name":_("The Ballroom"), "area":2, "pos":(412, 225)},

    "barroom" : {"name":_("The Barroom"), "area":1, "pos":(1470, 510)},

    "bathroom" : {"name":_("Bathroom"), "area":1, "pos":(1350, 335)},

    "bedroom" : {"name":_("Bedroom"), "area":2, "pos":(733, 136)},

    "diningroom" : {"name":_("Dining Room"), "area":1, "pos":(910, 350)},

    "easthall" : {"name":_("The Eastern Hall"), "area":1, "pos":(1450, 410)},

    "eastupstairs" : {"name":_("Eastern Upstairs"), "area":2, "pos":(707, 226)},

    "garden" : {"name":_("Garden"), "area":1, "pos":(320, 405)},

    "graveyard" : {"name":_("Graveyard"), "area":1, "pos":(130, 405)},

    "greenhouse" : {"name":_("Greenhouse"), "area":1, "pos":(525, 405)},

    "kitchen" : {"name":_("Kitchen"), "area":1, "pos":(725, 510)},

    "maingate" : {"name":_("The Main Gate"), "area":1, "pos":(500,160)},

    "mainhall" : {"name":_("The Main Hall"), "area":1, "pos":(1110, 470)},

    "musicroom" : {"name":_("Music Room"), "area":2, "pos":(603, 126)},

    "nursery" : {"name":_("Nursery"), "area":2, "pos":(735, 335)},

    "parlor" : {"name":_("The Parlor"), "area":1, "pos":(860, 480)},

    "sceanceroom" : {"name":_("Sceance Room"), "area":2, "pos":(0, 0)},

    "secondbedroom" : {"name":_("Second Bedroom"), "area":2, "pos":(603, 337)},

    "servantsbedroom" : {"name":_("Servant's Bedroom"), "area":1, "pos":(660, 345)},

    "servantsquarters" : {"name":_("Servant's Quarters"), "area":1, "pos":(780, 340)},

    "shed" : {"name":_("The Shed"), "area":1, "pos":(210, 275)},

    "storageroom" : {"name":_("Storage Room"), "area":1, "pos":(655, 260)},

    "study" : {"name":_("Study"), "area":1, "pos":(1550, 350)},

    "westhall" : {"name":_("The West Hall"), "area":1, "pos":(790, 405)},

    "westupstairs" : {"name":_("Western Upstairs"), "area":2, "pos":(189, 222)},
    }



default minimap = True

define map_image_dimension = (1720, 968)
define map_image_path = "map/"
define map_image_type = ".png"

default current_area = 1
default current_location = "maingate"

default area_limit = 2

define minimap_position = (1.0, 0.0)
define minimap_offset = 10

define location_indicator_image = "map/map_indicator.png"

default preferences.show_minimap = True
default preferences.minimap_opacity = 1
default preferences.minimap_size = 0.3

default preferences.minimap_zoom = 2.0

## Character Callback

init python:

    def location(name=None):
        global current_location
        global current_area
        global area_limit
        loc = None
        if 'bg' in renpy.get_showing_tags():
            loc = renpy.get_attributes('bg')[0]
        if name in locations:
            current_location = name
        elif loc in locations:
            current_location = loc
        if locations[current_location]["area"]:
            current_area = locations[current_location]["area"]
            if locations[current_location]["area"] > area_limit:
                area_limit = locations[current_location]["area"]

    def update_location(event, **kwargs):
        location()

define config.all_character_callbacks = [ update_location ]


## Screens

screen status():
    modal True
    tag menu
    on "show" action SetVariable("current_area", locations[current_location]["area"])
    
    #use game_menu(_("Status")):
    frame:
        text locations[current_location]["name"]:
            ypos -70
            xpos 750
        imagebutton idle "closebuttonmap.png":
            ypos -89
            xpos 284
            focus_mask None
            action Play("sound", "click.ogg"), Hide("showMap"), Hide("status"), Show("hud")
        use map

## Minimap

init python:
    config.overlay_screens.append("minimap")

transform minimap_opacity(opac):
    on hover:
        ease 0.3 alpha 1.0 mesh True
    on idle:
        ease 0.3 alpha opac mesh True

screen minimap():

    $ area = locations[current_location]["area"]

    if minimap and preferences.show_minimap and area != None:

        fixed pos minimap_offset,minimap_offset xysize config.screen_width-2*minimap_offset, config.screen_height-2*minimap_offset-gui.textbox_height:
            fixed fit_first True xalign minimap_position[0] yalign minimap_position[1]:
                frame:
                    use map(scale=preferences.minimap_size, minimap=True)
                    at minimap_opacity(preferences.minimap_opacity)

## Map Screen

screen map(scale=1.0, minimap=False):

    if minimap:
        $ area = locations[current_location]["area"]
    else:
        $ area = current_area

    if minimap and preferences.minimap_zoom:
        $ scale = scale * preferences.minimap_zoom

    if area != None:
        fixed fit_first True:
            if not minimap:
                yalign 0.5
                xalign 0.5

                # The map background image
            add map_image_path + str(area) + map_image_type zoom scale:
                if minimap and preferences.minimap_zoom:
                    crop (int(locations[current_location]["pos"][0]-renpy.image_size(map_image_path + str(area) + map_image_type)[0]/(preferences.minimap_zoom*2)), int(locations[current_location]["pos"][1]-renpy.image_size(map_image_path + str(area) + map_image_type)[1]/(preferences.minimap_zoom*2)), int(renpy.image_size(map_image_path + str(area) + map_image_type)[0]/preferences.minimap_zoom), int(renpy.image_size(map_image_path + str(area) + map_image_type)[1]/preferences.minimap_zoom))

            # The location indicator
            if area == locations[current_location]["area"]:
                fixed:
                    if minimap and preferences.minimap_zoom:
                        xpos 0.5 ypos 0.5
                    else:
                        xpos int(locations[current_location]["pos"][0]*scale) ypos int(locations[current_location]["pos"][1]*scale)

                    if location_indicator_image:
                        add location_indicator_image zoom scale
                    else:
                        text "x" size int(gui.interface_text_size*scale)

            # Area view buttons
            if not minimap and area_limit > 1:
                hbox xalign 0.5:
                    textbutton "<" action SetVariable("current_area", If(current_area > 1, current_area-1, 1))
                    text _("Floor")
                    textbutton ">" action SetVariable("current_area", If(current_area < area_limit, current_area+1, area_limit))