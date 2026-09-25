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
	0x0160,
    0x020a
]

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
}

# Format is [(group or label), lineNumber] (found in the warpSources.s after you begin with the label and count down the line (line count starts 1 down after the label)).
# or [] if you don't want anything modified in that index. 
# This also has to be in dungeon order.
DUNGEON_WARPS = [
    {
        "entrance": [0, 35],
        "exit": [5, 76]
    },
    {
        "entrance": [0, 42],
        "exit": [5, 0]
    },
    #{},
    {
        "entrance": [0, 68],
        "exit": [5, 78]
    },
    {
        "entrance": [0, 62],
        "exit": [5, 70]
    },
]

PALETTE_BYTES = {
    "green": 0x00,
    "blue": 0x01,
    "red": 0x02,
    "orange": 0x03,
}

# TODO: Implement seed tree data once code addresses for the trees are found.