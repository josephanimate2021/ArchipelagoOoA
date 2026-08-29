# warps are in bank 04
WARP_DEST_TABLE = 0x12f5b
WARP_SOURCE_TABLE = 0x1359e

# Reminder for warp destination content (none of this will be touched) :
# byte 0 is the toom index to warp to (the group is implicit from the address)
# byte 1  Y/X position to spawn at.
# byte 2 Parameter. What this does depends on the transition type? (ie. walk in from top or bottom of screen?)
# byte 3 Transition dest type (see constants/transitions.s).

# Reminder for warp source content :
# byte 0 is misc data for the warp (shouldn't be touched ?)
# byte 1 is the room index from where the warp come from (the group is implicit from the address) (shouldn't be touched)
# byte 2 is the Warp dest index of the warp (is modified)
# byte 3 (first halfbyte) is the warp group of destination (is modified)
# byte 3 (second halfbyte) is the transition type (shouldn't be touched ?)

def GetWarpNameFromDungeonNumber(dungeon):
    for warpName, warpData in WARPS_DATA.items():
        if ("dungeon" in warpData and warpData["dungeon"] == dungeon):
            return warpName
    return ""

def GetWarpDataFromDungeonNumber(dungeon):
    return WARPS_DATA[GetWarpNameFromDungeonNumber(dungeon)]

# "outside_warp" : Warp source of the warp from outside to inside (NOTE : This is not the exact address of the warp entry, but the address + 2)
# "inside_warp" : Warp source of the warp from inside to outside
# "custom_map_tile" : By default, map tile use the room and the group to be generated, but if there is a custom_map_tile, it's used instead
# "present" : is the warp in the present (will be used to randomize only entrance in the past with past and vice versa)
# "dungeon" : if set, this is a dungeon entrance, and this is for the dungeon given here
# "is_deadend" : if set, can be paired with entrance that have the "must_lead_to_deadend" tag
# "must_lead_to_deadend" : See above.

# regions from all warps are automatically created from this struct and (if no randomization is done) logic connect outside and inside as a two way connection. 
# On the outside side, the region will be name "outside <NAME>"
# On the inside side, the region will be name "inside <NAME>"

OUTSIDE_TAG = "outside "
INSIDE_TAG = "inside "

WARPS_DATA = {

#PRESENT TIME

    # FOREST OF TIME
    "nayru's house": {
        "outside_warp": 0x7660,
        "inside_warp": 0x7a10,
        "present": True,
    },
    "lower tingle cave": {
        "outside_warp": 0x7644,
        #   "inside_warp": ,
        "present": True,
    },
    "upper tingle stairs": {
        "outside_warp": 0x763c,
        #   "inside_warp": ,
        "present": True,
    },

    # LYNNA CITY
    "vasu's shop": {
        "outside_warp": 0x7628,
        "inside_warp": 0x7948,
        "present": True,
    },
    "lynna city shop": {
        "outside_warp": 0x7714,
        #   "inside_warp": ,
        "present": True,
    },
    "hidden shop": {
        "outside_warp": 0x7710,
        #   "inside_warp": ,
        "present": True,
    },
    "mayor's house": {
        "outside_warp": 0x7624,
        "inside_warp": 0x7a90,
        "present": True,
    },
    # the house where the kid gets frozen in time on the cutscene where veran takes over naryu at the beginning, i dont have a better name for this
    "house left of mayor's house": {
        #   "outside_warp": ,   #room 0 56
        #   "inside_warp": ,
        "present": True,
    },
    "know it all birds house": {
        #   "outside_warp": ,   #room 0 55
        #   "inside_warp": ,
        "present": True,
    },
    "mamamu yan house": {
        #   "outside_warp": ,   #room 0 66
        #   "inside_warp": ,
        "present": True,
    },
    "black tower ruins": {
        #   "outside_warp": ,    #room 0 76
        #   "inside_warp": ,
        "present": True,
        "require_option": "secrets"
    },
    # house in the top left of the city, iirc its troy's house
    "troy's house": {
        #   "outside_warp": ,   #room 0 45
        #   "inside_warp": ,
        "present": True,
    },
    "left bippin blossom door": {
        #   "outside_warp": ,   #room 0 47, t23
        #   "inside_warp": ,
        "present": True,
    },
    "right bippin blossom door": {
        #   "outside_warp": ,   #room 0 47, t25
        #   "inside_warp": ,
        "present": True,
    },
    "maku road front": {
        #   "outside_warp": ,   #room 0 48
        #   "inside_warp": ,
        "present": True,
    },
    "maku road stairs": {
        #   "outside_warp": ,   #room 0 38, t48
        #   "inside_warp": ,
        "present": True,
    },
    "maku tree hole": {
        #   "outside_warp": ,   #room 0 38, t23/24
        #   "inside_warp": ,
        "present": True,
    },
    "happy mask shop": {
        #   "outside_warp": ,   #room 0 53
        #   "inside_warp": ,
        "present": True,
    },

    # YOLL GRAVEYARD
    "cheval grave": {
        #   "outside_warp": ,   #room 0 5B
        #   "inside_warp": ,
        "present": True,
    },
    "syrup shop": {
        #   "outside_warp": ,   #room 0 5D
        #   "inside_warp": ,
        "present": True,
    },
    "grave under the tree": {
        #   "outside_warp": ,   #room 0 8D, t56
        #   "inside_warp": ,
        "present": True,
    },
    "poe grave": {
        #   "outside_warp": ,   #room 0 7c
        #   "inside_warp": ,
        "present": True,
    },
    # NUUN HIGHLANDS
    "nuun fairy cave": {
        #   "outside_warp": ,   #room 0 06
        #   "inside_warp": ,
        "present": True,
    },
    # putting this here to be a completionist but I don't think this one should be randomized
    # since the game already cant tell which cave is supposed to be here
#    "nuun animal cave": {
#           "outside_warp": ,
#           "inside_warp": ,
#        "present": True,
#    },
    # PRESENT SYMMETRY
    "top left symmetry house": {
        #   "outside_warp": ,   #room 2 02
        #   "inside_warp": ,
        "present": True,
    },
    "top right symmetry house": {
        #   "outside_warp": ,   #room 2 04
        #   "inside_warp": ,
        "present": True,
    },
    "bottom left symmetry house": {
        #   "outside_warp": ,   #room 2 12
        #   "inside_warp": ,
        "present": True,
    },
    "bottom right symmetry house": {
        #   "outside_warp": ,   #room 2 14
        #   "inside_warp": ,
        "present": True,
    },

    # WESTERN ROLLING RIDGE
    "west ridge goron city lower": {
        #   "outside_warp": ,   #room 0 28
        #   "inside_warp": ,
        "present": True,
    },
    "west ridge goron city upper": {
        #   "outside_warp": ,   #room 0 18, t4
        #   "inside_warp": ,
        "present": True,
    },
    "west ridge goron city stairs": {
        #   "outside_warp": ,   #room 0 18, t20
        #   "inside_warp": ,
        "present": True,
    },

    "west ridge fairy cave": {
        #   "outside_warp": ,   #room 0 1B
        #   "inside_warp": ,
        "present": True,
    },

    # added to be completionist, not sure what we want to do for these entrances
    # since they're not always accessible
    #potentially keep the keep after beating great moblin,
    #but move the cave to the right and be a locked door while great
    #moblin is unbeaten and the stairs to the left over the ledge
    "moblin keep left door": {
        #   "outside_warp": ,   #room 0 09, t40
        #   "inside_warp": ,
        "present": True,
    },
    "moblin keep right door": {
        #   "outside_warp": ,   #room 0 09, t42
        #   "inside_warp": ,
        "present": True,
    },

    "moblin keep sewer stairs": {
        #   "outside_warp": ,   #room 2 09, t40
        #   "inside_warp": ,
        "present": True,
    },
    "moblin keep sewer exit": {
        #   "outside_warp": ,   #room 0 0A, t12
        #   "inside_warp": ,
        "present": True,
    },
    #the cave directly behind moblin keep
    "cave behind moblin keep front": {
        #   "outside_warp": ,   #room 2 09, t34
        #   "inside_warp": ,
        "present": True,
    },
    #the side of the moblin keep connector that takes you to crown dungeon ledge
    "cave behind moblin keep back": {
        #   "outside_warp": ,   #room 0 0B
        #   "inside_warp": ,
        "present": True,
    },
    # the connector that takes you from crown dungeon ledge to east ridge
    "west to east ridge cave front": {
        #   "outside_warp": ,   #room 0 0B
        #   "inside_warp": ,
        "present": True,
    },
    # the connector that takes you from east ridge to crown dungeon ledge
    "west to east ridge cave back": {
        #   "outside_warp": ,   #room 0 1B
        #   "inside_warp": ,
        "present": True,
    },

    # EASTERN ROLLING RIDGE
    # the cave that becomes treasure hunting goron in the past
    "empty cave by echoes portal": {
        #   "outside_warp": ,   #room 0 0B
        #   "inside_warp": ,
        "present": True,
    },
    # the connector that takes you to the base of east ridge from the top
    "east ridge upper to lower cave front": {
        #   "outside_warp": ,   #room 0 0C
        #   "inside_warp": ,
        "present": True,
    },
    # the connector that takes you to the top of east ridge from the base
    "east ridge upper to lower cave back": {
        #   "outside_warp": ,   #room 0 2B
        #   "inside_warp": ,
        "present": True,
    },
    #where the dance hall ends up at the very top
    "northeast cave left": {
        #   "outside_warp": ,   #room 0 0D
        #   "inside_warp": ,
        "present": True,
    },

    # needs tune of currents to access, it's inside warp is a one way
    "northeast cave right entrance": {
        #   "outside_warp": ,   #room 0 0D
        #   "inside_warp": ,
        "present": True,
    },
    "goron dance hall entrance": {
        #   "outside_warp": ,   #room 0 3D
        #   "inside_warp": ,
        "present": True,
    },
    "goron dance hall middle": {
        #   "outside_warp": ,   #room 0 1C
        #   "inside_warp": ,
        "present": True,
    },
    "ridge base fairy cave": {
        #   "outside_warp": ,   #room 0 3D
        #   "inside_warp": ,
        "present": True,
    },
    "mermaid cave front porch": {
        #   "outside_warp": ,   #room 0 3C
        #   "inside_warp": ,
        "present": True,
    },
    "greedy old man bush": {
        #   "outside_warp": ,   #room 0 4D
        #   "inside_warp": ,
        "present": True,
    },
    "empty cave next to target carts": {
        #   "outside_warp": ,   #room 0 1C
        #   "inside_warp": ,
        "present": True,
    },
    "middle ridge fairy cave": {
        #   "outside_warp": ,   #room 0 1D
        #   "inside_warp": ,
        "present": True,
    },
    "target carts": {
        #   "outside_warp": ,   #room 0 1D
        #   "inside_warp": ,
        "present": True,
    },

    # LYNNA SEAS
    "underwater sea of storms cave": {
        #   "outside_warp": ,   #room 2 B7
        #   "inside_warp": ,
        "present": True,
        "is_underwater": True,
        "require_option": "secrets"
    },
    "present drifting island house": {
        #   "outside_warp": ,   #room 0 C5
        #   "inside_warp": ,
        "present": True,
    },
    "present underwater zora duplex left door": {
        #   "outside_warp": ,   #room 2 D0
        #   "inside_warp": ,
        "present": True,
        "is_underwater": True,
    },
    "present underwater zora duplex right door": {
        #   "outside_warp": ,   #room 2 D0
        #   "inside_warp": ,
        "present": True,
        "is_underwater": True,
    },
    "present underwater zora house": {
        #   "outside_warp": ,   #room 2 C1
        #   "inside_warp": ,
        "present": True,
        "is_underwater": True,
    },
    "present zora palace": {
        #   "outside_warp": ,   #room 2 A1
        #   "inside_warp": ,
        "present": True,
        "is_underwater": True,
    },
    #bombable cave in the top left of zora village above water
    "zora crypt cave": {
        #   "outside_warp": ,   #room 0 A0
        #   "inside_warp": ,
        "present": True,
    },
    "present fairy queen cave": {
        #   "outside_warp": ,   #room 0 A3
        #   "inside_warp": ,
        "present": True,
    },
    "present library": {
        #   "outside_warp": ,   #room 0 A5
        #   "inside_warp": ,
        "present": True,
    },
#PRESENT CRESCENT
    "southern fairy cave": {
        #   "outside_warp": ,   #room 0 DA
        #   "inside_warp": ,
        "present": True,
    },
    "wild tokay museum": {
        #   "outside_warp": ,   #room 0 BD
        #   "inside_warp": ,
        "present": True,
    },
    "upper tokay house": {
        #   "outside_warp": ,   #room 0 CD
        #   "inside_warp": ,
        "present": True,
    },
    "tokay chef house": {
        #   "outside_warp": , #room 0 DD
        #   "inside_warp": ,
        "present": True,
    },
    "underwater maze cave": {
        #   "outside_warp": ,   #room 2 BA
        #   "inside_warp": ,
        "present": True,
        "is_underwater": True,
    },
#PAST ENTRANCES
#LYNNA VILLAGE
    "Rafton's House Left": {
        "outside_warp": 0x785c,
        "inside_warp": 0x7880,
        "present": False,
    },
    "Rafton's House Right": {
        "outside_warp": 0x7860,
        "inside_warp": 0x7884,
        "present": False,
    },
    "shooting gallery": {
        #   "outside_warp": ,   #room 1 58, t30
        #   "inside_warp": ,
        "present": False,
    },
    "advance shop": {
        #   "outside_warp": ,   #room 1 58, t33
        #   "inside_warp": ,
        "present": False,
        "require_option": "advance_shop"
    },
    "postman house": {
        #   "outside_warp": ,   #room 1 57
        #   "inside_warp": ,
        "present": False,
    },
    "": {
        #   "outside_warp": ,
        #   "inside_warp": ,
        "present": False,
    },

    # DUNGEONS
    "d0": {
        "outside_warp": 0x7728,
        "inside_warp": 0x7aec,
        "custom_txt_id": 0xe9,
        "present": False,
        "dungeon": 0,
    },
    "d1": {
        "outside_warp": 0x7718,
        "inside_warp": 0x7ad0,
        "present": True,
        "dungeon": 1,
    },
    "d2": {
        "outside_warp": 0x772c,
        "inside_warp": 0x7ad4,
        "present": False,
        "dungeon": 2,
    },
    "d3": {
        "outside_warp": 0x75c8,
        "inside_warp": 0x7ad8,
        "present": True,
        "dungeon": 3,
    },
    "d4": {
        "outside_warp": 0x75cc,
        "inside_warp": 0x7adc,
        "present": True,
        "dungeon": 4,
    },
    "d5": {
        "outside_warp": 0x76b0,
        "inside_warp": 0x7ae0,
        "present": True,
        "dungeon": 5,
    },
    "d6 present": {
        "outside_warp": 0x7748,
        "inside_warp": 0x7c48,
        "custom_map_tile": 0x03c,
        "present": True,
        "dungeon": 6,
    },
    "d7": {
        "outside_warp": 0x7874,
        "inside_warp": 0x7c60,
        "custom_map_tile": 0x090,
        "present": True,
        "dungeon": 7,
        "is_underwater": True,
    },
    "d8": {
        "outside_warp": 0x7730,
        "inside_warp": 0x7c74,
        "present": False,
        "dungeon": 8,
    },
    "d11": {
        "outside_warp": 0x770c,
        "inside_warp": 0x7ae4,
        "present": True,
        "dungeon": 11,
        "require_option": "linked_heros_cave"
    },
    "d6 past": {
        "outside_warp": 0x79b4,
        "inside_warp": 0x7c54,
        "custom_map_tile": 0x13c,
        "custom_txt_id": 0xe1,
        "present": False,
        "dungeon": 9,
    }
}