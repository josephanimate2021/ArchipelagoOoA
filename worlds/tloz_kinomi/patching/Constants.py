from ..common.patching.z80asm.Assembler import GameboyAddress
from typing import Any

# This is the list of rooms I put in order inside my oldManLocationsTable function of the game.
RUPEE_OLD_MAN_ROOM_ORDER = [0x05fe]
RUPEE_OLD_MAN_ROOM_ORDER.extend([i for i in range(0x0506, 0x050c)])
NPC_ITEM_ROOM_ORDER = RUPEE_OLD_MAN_ROOM_ORDER.copy()
NPC_ITEM_ROOM_ORDER.extend([
	0x022e,
	0x020e,
	0x024e,
    0x0426,
    0x041f,
    0x0436,
    0x044e,
    0x0452,
	0x0458,
    0x0516,
    0x0527,
    0x053b,
    0x055d,
    0x056e
])

SHOP_NAMES_IN_ORDER = [ # This array needs to be put together by subid order of INTERAC_SHOP_ITEM. Any name works as long as they match with the location.
    "",
    "Kinomi Town: Shop #3",
    "",
]
SHOP_NAMES_IN_ORDER.extend([f"Kinomi Town: Shop #{i}" for i in range(2, 0, -1)])
SHOP_NAMES_IN_ORDER.extend(["" for _ in range(0x0f - len(SHOP_NAMES_IN_ORDER))])
SHOP_NAMES_IN_ORDER.extend([f"Jiku Clifs (Present): Shop #{i}" for i in range(3, 5)])
SHOP_NAMES_IN_ORDER.extend([f"Jiku Clifs (Present): Shop #{i}" for i in range(2, 0, -1)])
SHOP_NAMES_IN_ORDER.extend([f"Kinomi Town: Hidden Shop #{i}" for i in range(1, 4, 2)])

REFILL_NPCS = {
    "impa": GameboyAddress(0x09, 0x53ac).address_in_rom(),
    "rosa": GameboyAddress(0x09, 0x4234).address_in_rom()
}

ASM_FILES = [
    "asm/file_select_custom_string.yaml"
]

RUPEE_VALUES = {
    0: 0x00,
    1: 0x01,
    2: 0x02,
    5: 0x03,
    10: 0x04,
    20: 0x05,
    40: 0x06,
    30: 0x07,
    60: 0x08,
    70: 0x09,
    25: 0x0a,
    50: 0x0b,
    100: 0x0c,
    200: 0x0d,
    400: 0x0e,
    150: 0x0f,
    300: 0x10,
    500: 0x11,
    900: 0x12,
    80: 0x13,
    999: 0x14,
    777: 0x15,
}

PALETTE_BYTES = {
    "green": 0x00,
    "blue": 0x01,
    "red": 0x02,
    "orange": 0x03,
}

ITEM_SPR_COLORS = {
    "green": 0x00,
    "blue": 0x10,
    "red": 0x20,
    "orange": 0x30,
    "dark blue": 0x40,
    "all red": 0x50
}

ITEM_SIZES = {
    "big": 0x03,
    "big_mirrored": 0x0a,
    "small": 0x00
}

# This dict allows for sprite modification to be done to an item as long as they are in order so that it's modified correctly by the code.
# Please take note that python dicts do not accept the same key for a different value as it will not work during a loop.
# Any parameter you put in dosen't matter unless a spot has the actual item name.
GFX_ITEM_GROUPS: dict[int, dict[Any, Any]] = {
    0x78: {
        # Ignore fairies and a heart.
        "fairy": "small",
        "Heart": "all red@small",
        # Rupees are handled differently.
        "rupee_small": "small",
        "rupee_medium": "small",
        "rupee_large": "big",
        # All other items are handled here.
        "Piece of Heart": "red@big",
        "Bombs (10)": "dark blue@small",
	},
    0x79: {
        "Life Potion": "red@big",
        "Zora's Flippers": "all red@big",
        "": "small",
        "Gasha Seed": "blue@small",
        "Archipelago": "big",
        "half heartpiece": "small",
        "Heart Container": "all red@small@half"
	},
    0x7a: {
        "Dungeon Map": "all red@big",
        "Compass": "dark blue@big",
        "Boss Key": "all red@small",
        "Small Key": "all red@small",
        "Falls Key": "all red@small",
        "Old Mining Key": "all red@small",
        "Witch's Key": "dark blue@small",
        "Old Labyrinth Key": "green@small"
	},
    0x7c: {
        "Seed Satchel": "all red@small"
	},
	0x7d: {
        "Sword": "green@small",
        "dummy1": "small",
        "dummy2": "small",
        "Shield": "green@small",
        "dummy3": "small",
        "dummy4": "small",
        "dummy5": "small",
        "Roc's Cape": "all red@small",
        "Rod of Seasons": "red@small",
        "dummy6": "small",
        "dummy7": "small",
        "Shovel": "blue@small",
        "dummy8": "small",
        "Cane of Somaria": "red@small"
	},
    0x7e: {
        "Bombchus (10)": "all red@small",
        "Biggoron's Sword": "orange@big",
        "Harp": "green@big",
        "dummy1": "big",
        "dummy2": "big",
        "dummy3": "big",
        "dummy4": "big",
        "dummy5": "big",
        "dummy6": "big",
        "Power Glove": "all red@small",
	},
    0x7f: {
        "dummy1": "big",
        "dummy2": "small",
        "dummy3": "small",
        "dummy4": "small",
        "dummy5": "small",
        "dummy6": "big",
        "Eternal Song": "blue@big",
        "Wings of Passion": "orange@small@half"
	},
    0x80: {
        "Wood Clock": "all red@big",
		"Potion": "red@small@half",
        "Ghastly Doll": "green@big",
        "dummy2": "big",
        "dummy3": "big",
        "Mushroom": "all red@big",
        "dummy4": "small",
        "dummy5": "small",
        "Sparring Book": "red@big"
	},
    0x81: {
        "dummy1": "big",
        "dummy2": "big",
        "Broken Sword": "blue@big",
        "Zora's Scale": "blue@big"
	},
    0x82: {
        "Winter Stone": "blue@small",
        "Summer Stone": "red@small",
        "Autumn Stone": "orange@small",
        "Spring Stone": "green@small",
        "dummy1": "big",
        "dummy2": "small",
        "dummy3": "small",
        "dummy4": "small",
        "dummy5": "small",
        "dummy6": "big",
        "Slate": "orange@small",
        "Pearl": "small"
	},
    0x84: {
        "dummy1": "small",
        "dummy2": "small",
        "Bommerang": "dark blue@small"
	}
}

# If you are trying to modify any interactions, list them here in this dict. The order dosen't matter.
APPLY_GFX_CHANGES_TO_INTERACTIONS = {
    0x0358: ["interaction94SubidData", 2],
    "Kinomi Town: Shop #3": ["interaction47SubidData", 1],
    "Kinomi Town: Shop #2": ["interaction47SubidData", 3],
    "Kinomi Town: Shop #1": ["interaction47SubidData", 4],
}

# This array is meant as an incrementer for an interaction that's being modifed to properly display the item sprite.
INTERACTION_LABEL_INDEXES = [
    [], # You don't have to put anything here in index 0. Index 1 and onwards you would have to put the interaction down.
    ["interaction94SubidData"],
]
