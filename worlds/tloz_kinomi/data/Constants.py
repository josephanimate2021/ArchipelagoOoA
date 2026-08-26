VERSION = "0.4.3"
RETRO_COMPAT_VERSION = ["0.4.3", "0.4.2", "0.4.1", "0.4.0"]

COMPANIONS = [
    "Ricky",
    "Dimitri",
    "Moosh"
]

DIRECTIONS = [
    "up",
    "right",
    "down",
    "left"
]

SEED_ITEMS = [
    "Ember Seeds",
    "Scent Seeds",
    "Pegasus Seeds",
    "Gale Seeds",
    "Mystery Seeds"
]

TREES_TABLE = [
    "Lynna City: Seed Tree",
    "Ambi's Palace: Seed Tree",
    "Deku Forest: Seed Tree",
    "Crescent Island: Seed Tree",
    "Symmetry city: Seed Tree",
    "Rolling Ridge West: Seed Tree",
    "Rolling Ridge East: Seed Tree",
    "Zora Village: Seed Tree",
]


DUNGEON_NAMES = [
    "Summer Villa",
    "Spirit's Grotto",
    "Lost Labyrinth (Past)",
    "Four Corners Cave",
    "Seasons Shrine",
    "Lost Labyrinth (Present)",
    "Temple of The Tokay",
    # "Old Crown Dungeon"
]

REGIONS_CONVERSION_TABLE = {
    # TODO OTHERS
    "LYNNA_VILLAGE": "Lynna village",
}

GIFTS = [
    "Eternal Song",
    "Wings of Passion"
]

VALID_RUPEE_VALUES = [
    0, 1, 2, 5, 10, 20, 25, 30, 40, 50, 60, 70, 80, 100, 200, 300, 400, 500, 900, 999
]

DAMAGE_MODIFIER_VALUES = {
    "peaceful": -4,
    "easier": -2,
    "vanilla": 0,
    "harder": 2,
    "insane": 4,
}

DUNGEON_ENTRANCES = {
    "summer villa entrance": "enter summer villa",
    "spirit's grotto entrance": "enter spirit's grotto",
    "lost labyrinth entrance": "enter lost labyrinth",
    "four corners cave entrance": "enter four corners cave",
    "seasons shrine entrance": "enter seasons shrine",
    #"old crown dungeon entrance": "enter old crown dungeon",
    #"d6 entrance": "enter d6",
    #"d7 entrance": "enter d7"
}

SHOP_PRICES_DIVIDERS = {
    "kinomiShop1": 1,
    "kinomiShop2": 1,
    "kinomiShop3": 1,
    "hiddenShop1": 1,
    "hiddenShop2": 1,
    "hiddenShop3": 1,
    "seaShop1": 1,
    "seaShop2": 1,
    "seaShop3": 1,
    "seaShop4": 1
}

ITEM_GROUPS = {
    "Small Keys": [
        "Small Key (Summer Villa)",
        "Small Key (Spirit's Grotto)",
        "Small Key (Lost Labyrinth (Past))",
        "Small Key (Four Corners Cave)",
        "Small Key (Seasons Shrine)",
        "Small Key (Lost Labyrinth (Present))",
        "Small Key (Temple of The Tokay)"
    ],
    "Boss Keys": [
        "Boss Key (Summer Villa)",
        "Boss Key (Spirit's Grotto)",
        "Boss Key (Lost Labyrinth (Past))",
        "Boss Key (Four Corners Cave)",
        "Boss Key (Seasons Shrine)",
        "",
        "Boss Key (Temple of The Tokay)"
    ],
    "Compasses": [
        "Compass (Summer Villa)",
        "Compass (Spirit's Grotto)",
        "Compass (Lost Labyrinth (Past))",
        "Compass (Four Corners Cave)",
        "Compass (Seasons Shrine)",
        "Compass (Lost Labyrinth (Present))",
        "Compass (Temple of The Tokay)"
    ],
    "Dungeon Maps": [
        "Dungeon Map (Summer Villa)",
        "Dungeon Map (Spirit's Grotto)",
        "Dungeon Map (Lost Labyrinth (Past))",
        "Dungeon Map (Four Corners Cave)",
        "Dungeon Map (Seasons Shrine)",
        "Dungeon Map (Lost Labyrinth (Present))",
        "Dungeon Map (Temple of The Tokay)"
    ],
    "Master Keys": [
        "Master Key (Summer Villa)",
        "Master Key (Spirit's Grotto)",
        "Master Key (Lost Labyrinth (Past))",
        "Master Key (Four Corners Cave)",
        "Master Key (Seasons Shrine)",
        "Master Key (Lost Labyrinth (Present))",
        "Master Key (Temple of The Tokay)"
    ],
}

TREASURE_SPAWN_INSTANT = 0x00
TREASURE_SPAWN_POOF = 0x10
TREASURE_SPAWN_DROP = 0x20
TREASURE_SPAWN_CHEST = 0x30
TREASURE_SPAWN_DIVE = 0x40
TREASURE_SPAWN_DIG = 0x50
TREASURE_SPAWN_DELAYED_CHEST = 0x60

TREASURE_GRAB_INSTANT = 0x00
TREASURE_GRAB_ONE_HAND = 0x01
TREASURE_GRAB_TWO_HANDS = 0x02
TREASURE_GRAB_SPIN_SLASH = 0x03

TREASURE_SET_ITEM_ROOM_FLAG = 0x08

COLLECT_TOUCH = TREASURE_SPAWN_INSTANT | TREASURE_GRAB_TWO_HANDS | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_POOF = TREASURE_SPAWN_POOF | TREASURE_GRAB_TWO_HANDS | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DROP = TREASURE_SPAWN_DROP | TREASURE_GRAB_ONE_HAND | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_CHEST = TREASURE_SPAWN_CHEST | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DIVE = TREASURE_SPAWN_DIVE | TREASURE_GRAB_ONE_HAND | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DIG = TREASURE_SPAWN_DIG | TREASURE_GRAB_TWO_HANDS | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_DELAYED_CHEST = TREASURE_SPAWN_DELAYED_CHEST | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_SPINSLASH = TREASURE_SPAWN_INSTANT | TREASURE_GRAB_SPIN_SLASH
COLLECT_FAKE_POOF = TREASURE_SPAWN_POOF | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_KEYDROP = TREASURE_SPAWN_DROP | TREASURE_GRAB_INSTANT | TREASURE_SET_ITEM_ROOM_FLAG
COLLECT_MAKU_TREE = 0x80
COLLECT_TARGET_CART = 0x81
COLLECT_BIGBANG = 0x82
COLLECT_GORON_BUSH_ROOM = 0x83