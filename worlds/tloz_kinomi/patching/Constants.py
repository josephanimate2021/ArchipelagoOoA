from ..common.patching.z80asm.Assembler import GameboyAddress

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

# TODO: Implement seed tree data once code addresses for the trees are found.
