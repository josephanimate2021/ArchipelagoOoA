from ..common.patching.z80asm.Assembler import GameboyAddress

STATIC_ITEM_ROOM_ORDER = [ # This is the list of rooms I put in order inside my itemsTable function of the game.
	0x0005,
	0x0007,
	0x000d,
	0x0032,
	0x0172,
	0x0133,
	0x050a,
	0x0501,
	0x0506,
	0x0504,
	0x0038,
	0x050b,
	0x025e,
	0x0453,
	0x0429,
	0x042a,
	0x0044,
	0x041e,
	0x0509,
	0x0113,
	0x0239,
	0x050d,
	0x032a,
	0x0308,
	0x0507,
	0x0505,
	0x05b2,
	0x05c1,
	0x05c0,
	0x05b8,
	0x0572,
	0x054c,
	0x0548,
	0x0534,
	0x0406,
	0x03af,
	0x0186,
	0x0153,
	0x0138,
	0x0122,
	0x0057,
	0x0011,
	0x0427,
	0x0160
]

REFILL_NPCS = {
    "impa": GameboyAddress(0x09, 0x53ac).address_in_rom(),
    "rosa": GameboyAddress(0x09, 0x4234).address_in_rom()
}

ASM_FILES = [
    "asm/collect.yaml",
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
}


DUNGEON_ENTRANCES = {
    "d0": {
        "addr": 0x13728,
        "map_tile": 0x148,
        "room": 0x48,
        "group": 0x01,
        "position": 0x21,
        "shifted": False,
        "default":"d0"
    },
    "d1": {
        "addr": 0x13718,
        "map_tile": 0x08d,
        "room": 0x8d,
        "group": 0x00,
        "position": 0x26,
        "essence_exit": 0x2874f,
        "shifted": False,
        "default":"d1"
    },
    "d2 past": {
        "addr": 0x1372c,
        "map_tile": 0x183,
        "room": 0x83,
        "group": 0x01,
        "position": 0x25,
        "shifted": False,
        "default":"d2"
    },
    "d2 present": {
        "addr": 0x13000,
        "map_tile": 0x083,
        "room": 0x83,
        "group": 0x00,
        "position": 0x25,
        "shifted": False,
        "default":"N/A"
    },
    "d3": {
        "addr": 0x135c8,
        "map_tile": 0x0ba,
        "room": 0xba,
        "group": 0x00,
        "position": 0x55,
        "shifted": False,
        "default":"d3"
    },
    "d4": {
        "addr": 0x135cc,
        "map_tile": 0x003,
        "room": 0x03,
        "group": 0x00,
        "position": 0x35,
        "shifted": True,
        "default":"d4"
    },
    "d5": {
        "addr": 0x136b0,
        "map_tile": 0x00a,
        "room": 0x0a,
        "group": 0x00,
        "position": 0x17,
        "shifted": False,
        "default":"d5"
    },
    "d6 present": {
        "addr": 0x13748,
        "map_tile": 0x03c,
        "room": 0x0e,
        "group": 0x01,
        "position": 0x16,
        "shifted": False,
        "default":"d6 present"
    },
    "d7": {
        "addr": 0x13874,
        "map_tile": 0x090,
        "room": 0x90,
        "group": 0x02,
        "position": 0x45,
        "shifted": True,
        "default":"d7"
    },
    "d8": {
        "addr": 0x13730,
        "map_tile": 0x15c,
        "room": 0x5c,
        "group": 0x01,
        "position": 0x15,
        "shifted": True,
        "default":"d8"
    },
    "d6 past": {
        "addr": 0x139b4,
        "map_tile": 0x13c,
        "room": 0x0f,
        "group": 0x03,
        "position": 0x16,
        "shifted": False,
        "default":"d6 past"
    },
}

DUNGEON_EXITS = {
    # TODO
    "d0": 0x13aec,
    "d1": 0x13ad0,
    "d2": 0x13ad4,
    "d3": 0x13ad8,
    "d4": 0x13adc,
    "d5": 0x13ae0,
    "d6 present": 0x13c48,
    "d7": 0x13c60,
    "d8": 0x13c74,
    "d6 past": 0x13c54,
}

PALETTE_BYTES = {
    "green": 0x00,
    "blue": 0x01,
    "red": 0x02,
    "orange": 0x03,
}

# TODO: Implement seed tree data once code addresses for the trees are found.