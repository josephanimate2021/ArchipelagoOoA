from .Constants import *

BASE_LOCATION_ID = 27022002000

LOCATIONS_DATA = {
    "Kinomi Town: Ghost's House": {
        "region_id": "ghost's house",
        "vanilla_item": "Falls Key",
        "flag_byte": 0xc70e,
        "room": 0x020e,
        "collect": COLLECT_TOUCH
    },
    "Kinomi Town: Librarian": {
        "region_id": "old man's library",
        "vanilla_item": "Old Labyrinth Key",
        "flag_byte": 0xc70e,
        "room": 0x020e,
        "collect": COLLECT_TOUCH
    },
    "Kinomi Town: Library Employee": {
        "region_id": "library employee",
        "vanilla_item": "Potion",
        "flag_byte": 0xc70e,
        "room": 0x020e,
        "collect": COLLECT_TOUCH
    },
    "Kinomi Town: Heart Piece at Link's House": {
        "region_id": "link's house heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc808,
        "room": 0x0308,
        "collect": COLLECT_TOUCH
    },
    # -----
    "Kinomi Town: Shop #1": {
        "region_id": "kinomi shop",
        "vanilla_item": "Shield",
        "flag_byte": 0xc643,
        "room": 0x025e,
        "map_tile": 0x13,
        "bit_mask": 0x20,
        "scouting_byte": 0xc75e,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "kinomiShop1",
    },
    "Kinomi Town: Shop #2": {
        "region_id": "kinomi shop",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xc643,
        "room": 0x025e,
        "map_tile": 0x13,
        "bit_mask": 0x40,
        "scouting_byte": 0xc75e,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "kinomiShop2",
    },
    "Kinomi Town: Shop #3": {
        "region_id": "kinomi shop",
        "vanilla_item": "Biggoron's Sword",
        "flag_byte": 0xc643,
        "room": 0x025e,
        "map_tile": 0x13,
        "bit_mask": 0x80,
        "scouting_byte": 0xc75e,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "kinomiShop3",
    },
    # -----
    "Kinomi Town: Hidden Shop #1": {
        "region_id": "hidden shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xc642,
        "room": 0x027e,
        "bit_mask": 0x01,
        "scouting_byte": 0xc77e,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "hiddenShop1",
    },
    "Kinomi Town: Hidden Shop #2": {
        "region_id": "hidden shop",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc642,
        "room": 0x027e,
        "bit_mask": 0x02,
        "scouting_byte": 0xc77e,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "hiddenShop2",
    },
    "Kinomi Town: Hidden Shop #3": {
        "region_id": "hidden shop",
        "vanilla_item": "Gasha Seed", # That's not the Ring box you're looking for.
        "flag_byte": 0xc642,
        "room": 0x027e,
        "bit_mask": 0x08,
        "scouting_byte": 0xc77e,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "hiddenShop3",
    },
    ##########################################
    "Forever Falls: Enemy Kill Heartpiece": {
        "region_id": "forever falls enemy kill",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc711,
        "room": 0x0011,
        "collect": COLLECT_TOUCH
    },
    "Forever Falls: Kill Enemies inside Cave": {
        "region_id": "forever falls cave",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc739,
        "room": 0x0239,
        "collect": COLLECT_TOUCH
    },
    "Forever Falls: Old Man": {
        "region_id": "forever falls old man",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xc74e,
        "room": 0x024e,
        "collect": COLLECT_TOUCH
    },
    ##########################################
    "Daichi Plain: Bomb Storehouse": {
        "region_id": "weird guy's house",
        "vanilla_item": "Bombs (10)",
        "flag_byte": 0xc818,
        "room": 0x0318,
        "collect": COLLECT_TOUCH
    },
    "Daichi Plain: Gravesite Basement": {
        "region_id": "daichi plain gravesite basement",
        "vanilla_item": "Shovel",
        "flag_byte": 0xc80d,
        "room": 0x030d,
        "collect": COLLECT_CHEST
    },
    "Daichi Plain: Old Man": {
        "region_id": "daichi plain old man",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xca06,
        "room": 0x0506,
        "collect": COLLECT_CHEST
    },
    "Daichi Plain: Old Man (Summer)": {
        "region_id": "daichi plain summer old man",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xca09,
        "room": 0x0509,
        "collect": COLLECT_CHEST
    },
    "Daichi Plain: Gravesite Heart Piece": {
        "region_id": "daichi plain gravesite heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc705,
        "room": 0x0005,
        "collect": COLLECT_TOUCH
    },
    "Daichi Plain: Gift Under Mushroom": {
        "region_id": "daichi plain gift under mushroom",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xc707,
        "room": 0x0007,
        "collect": COLLECT_TOUCH
    },
    "Daichi Plain: Chest": {
        "region_id": "daichi plain chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xc727,
        "room": 0x0027,
        "collect": COLLECT_TOUCH
    },
    "Daichi Plain: Fall Stone Reward": {
        "region_id": "fall stone reward",
        "vanilla_item": "Autumn Stone",
        "flag_byte": 0xca0c,
        "room": 0x070c,
        "collect": COLLECT_TOUCH
    },
    "Daichi Plain: Underwater Gift": {
        "region_id": "daichi plain underwater heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xca0d,
        "room": 0x070d,
        "collect": COLLECT_TOUCH
    },
    ##########################################
    "Lake of Memories: Old Man": {
        "region_id": "lake of memories old man",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xcafe,
        "room": 0x05fe,
        "bit_mask": 0x40,
        "collect": COLLECT_TOUCH
    },
    "Lake of Memories: Old Man's Chest": {
        "region_id": "lake of memories old man's chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xcafe,
        "room": 0x05fe,
        "collect": COLLECT_CHEST
    },
    "Lake of Memories: Underwater Cave": {
        "region_id": "lake of memories scrapped chest",
        "vanilla_item": "Toss Ring",
        "flag_byte": 0xc80e,
        "room": 0x030e,
        "collect": COLLECT_CHEST,
    },
    "Lake of Memories: Scrapped Chest": {
        "region_id": "lake of memories scrapped chest",
        "vanilla_item": "Rupees (5)",
        "flag_byte": 0xc848,
        "room": 0x0348,
        "collect": COLLECT_CHEST,
    },
    "Lake of Memories: Blocked Cave": {
        "region_id": "summer stone check",
        "vanilla_item": "Summer Stone",
        "flag_byte": 0xcafd,
        "room": 0x05fd,
        "collect": COLLECT_CHEST,
    },
    ##########################################
    "Hedge Maze: Old Man 2": {
        "region_id": "hedge maze old man 2",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xca0a,
        "room": 0x050a,
        "collect": COLLECT_TOUCH
    },
    "Hedge Maze: Old Man 1": {
        "region_id": "hedge maze old man 1",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xca08,
        "room": 0x0508,
        "bit_mask": 0x40,
        "collect": COLLECT_TOUCH
    },
    "Hedge Maze: Old Man's Chest": {
        "region_id": "hedge maze old man 1's chest",
        "vanilla_item": "Rupees (20)",
        "flag_byte": 0xca08,
        "room": 0x0508,
        "collect": COLLECT_CHEST
    },
    "Hedge Maze: Defeat Enemies for Stone": {
        "region_id": "hedge maze stone",
        "vanilla_item": "Spring Stone",
        "flag_byte": 0xcaf7,
        "room": 0x05f7,
        "collect": COLLECT_TOUCH
    },
    ##########################################
    "Deeper Woods: Old Man 1": {
        "region_id": "deeper woods old man 1",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xca0a,
        "room": 0x050a,
        "collect": COLLECT_TOUCH
    },
    "Deeper Woods: Old Man 2": {
        "region_id": "deeper woods old man 2",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xca0b,
        "room": 0x050b,
        "collect": COLLECT_TOUCH
    },
    "Deeper Woods: Underground Heart Piece": {
        "region_id": "deeper woods underground heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xca05,
        "room": 0x0705,
        "collect": COLLECT_TOUCH
    },
    "Deeper Woods: Cave Heart Piece": {
        "region_id": "deeper woods chest",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xcafc,
        "room": 0x07fc,
        "collect": COLLECT_CHEST
    },
    "Deeper Woods: Spool Swamp Gift": {
        "region_id": "familar swamp gift",
        "vanilla_item": "Zora's Flippers",
        "flag_byte": 0xc708,
        "room": 0x0008,
        "collect": COLLECT_CHEST
    },
    "Deeper Woods: Subrosia Dance": {
        "region_id": "subrosia dance",
        "vanilla_item": "Red Pearl",
        "flag_byte": 0xc88a,
        "room": 0x038a,
        "collect": COLLECT_TOUCH
    },
    "Deeper Woods: Happy Mask Salesman Trade": {
        "region_id": "deeper woods swordsman trade",
        "vanilla_item": "Sparring Book",
        "flag_byte": 0xc80a,
        "room": 0x030a,
        "collect": COLLECT_TOUCH
    },
    ##########################################
    "Jiku Clifs (Present): Life Potion Trade": {
        "region_id": "old lady trade",
        "vanilla_item": "Wood Clock",
        "flag_byte": 0xc728,
        "room": 0x0228,
        "collect": COLLECT_TOUCH,
    },
    "Jiku Clifs (Present): Rupee Chest Outside Lost Labyrinth": {
        "region_id": "chest inside cave outside lost labyrinth present entrance",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xc8be,
        "room": 0x02be,
        "collect": COLLECT_CHEST,
    },
    "Jiku Clifs (Present): Heart Piece Outside Lost Labyrinth": {
        "region_id": "heartpiece inside cave outside lost labyrinth present entrance",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xca04,
        "room": 0x0704,
        "collect": COLLECT_TOUCH,
    },
    # -----
    "Jiku Clifs (Present): Shop #1": {
        "region_id": "jiku clifs shop",
        "vanilla_item": "Potion",
        "flag_byte": 0xc643,
        "room": 0x03fe,
        "bit_mask": 0x80,
        "scouting_byte": 0xc8fe,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "seaShop1",
    },
    "Jiku Clifs (Present): Shop #2": {
        "region_id": "jiku clifs shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xc643,
        "room": 0x03ed,
        "bit_mask": 0x20,
        "scouting_byte": 0xc8fe,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "seaShop2",
    },
    "Maple Trade": {
        "region_id": "maple trade",
        "vanilla_item": "Life Potion",
        "flag_byte": 0xc6d2,
        "room": 0x0300,
        "bit_mask": 0x80,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "mapleTrade",
    },
    "Jiku Clifs (Present): Shop #3": {
        "region_id": "jiku clifs shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xc643,
        "room": 0x03ed,
        "bit_mask": 0x40,
        "scouting_byte": 0xc8fe,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "seaShop3",
    },
    "Jiku Clifs (Present): Shop #4": {
        "region_id": "jiku clifs shop",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xc643,
        "room": 0x03ed,
        "bit_mask": 0x60,
        "scouting_byte": 0xc8fe,
        "scouting_mask": 0x10,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "seaShop4",
    },
    ##########################################
    "Summer Villa (1F): Four Pillars Chest": {
        "region_id": "d0 map chest",
        "vanilla_item": "Dungeon Map (Summer Villa)",
        "flag_byte": 0xcad4,
        "room": 0x05d4,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (2F): Three Pillars Chest": {
        "region_id": "d0 compass chest",
        "vanilla_item": "Compass (Summer Villa)",
        "flag_byte": 0xcabc,
        "room": 0x05bc,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (1F): Small Key Chest": {
        "region_id": "d0 small key chest 1f",
        "vanilla_item": "Small Key (Summer Villa)",
        "flag_byte": 0xcab0,
        "room": 0x05b0,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (1F): Boss Key Chest": {
        "region_id": "d0 boss key chest",
        "vanilla_item": "Boss Key (Summer Villa)",
        "flag_byte": 0xcab9,
        "room": 0x05b9,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (B1F): Sword Chest": {
        "region_id": "d0 sword chest",
        "vanilla_item": "Sword",
        "flag_byte": 0xcab7,
        "room": 0x05b7,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (B1F): Shield Chest": {
        "region_id": "d0 shield chest",
        "vanilla_item": "Shield",
        "flag_byte": 0xcab5,
        "room": 0x05b5,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (B1F): Small Key Chest": {
        "region_id": "d0 small key chest b1f",
        "vanilla_item": "Small Key (Summer Villa)",
        "flag_byte": 0xcabd,
        "room": 0x05bd,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    "Summer Villa (2F): Small Key Chest": {
        "region_id": "d0 small key chest 2f",
        "vanilla_item": "Small Key (Summer Villa)",
        "flag_byte": 0xcabe,
        "room": 0x05be,
        "collect": COLLECT_CHEST,
        "dungeon": 0
    },
    ##########################################
    "Spirit's Grotto: Pots Chest": {
        "region_id": "d1 pots chest",
        "vanilla_item": "Dungeon Map (Spirit's Grotto)",
        "flag_byte": 0xc920,
        "room": 0x0420,
        "collect": COLLECT_CHEST,
        "dungeon": 1
    },
    "Spirit's Grotto: Chest on Platform": {
        "region_id": "d1 platform chest",
        "vanilla_item": "Small Key (Spirit's Grotto)",
        "flag_byte": 0xc923,
        "room": 0x0423,
        "collect": COLLECT_CHEST,
        "dungeon": 1
    },
    "Spirit's Grotto: Small Key Drop": {
        "region_id": "d1 small key drop",
        "vanilla_item": "Small Key (Spirit's Grotto)",
        "flag_byte": 0xc91f,
        "room": 0x041f,
        "collect": COLLECT_TOUCH,
        "dungeon": 1
    },
    "Spirit's Grotto: Heart Piece": {
        "region_id": "d1 heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc91b,
        "room": 0x041b,
        "dungeon": 1,
        "collect": COLLECT_CHEST,
    },
    "Spirit's Grotto: Compass Chest": {
        "region_id": "d1 compass chest",
        "vanilla_item": "Compass (Spirit's Grotto)",
        "flag_byte": 0xc915,
        "room": 0x0415,
        "dungeon": 1,
        "collect": COLLECT_CHEST,
    },
    "Spirit's Grotto: Hit Blocks with Sword": {
        "region_id": "d1 hit blocks",
        "vanilla_item": "Small Key (Spirit's Grotto)",
        "flag_byte": 0xc916,
        "room": 0x0416,
        "dungeon": 1,
        "collect": COLLECT_CHEST,
    },
    "Spirit's Grotto: Heart Piece at Colored Tiles": {
        "region_id": "d1 colored tiles heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc92a,
        "room": 0x042a,
        "dungeon": 1,
        "collect": COLLECT_TOUCH,
    },
    "Spirit's Grotto: Miniboss": {
        "region_id": "d1 miniboss arena",
        "vanilla_item": "Gasha Seed",
        "flag_byte": 0xc918,
        "room": 0x0418,
        "dungeon": 1,
        "collect": COLLECT_TOUCH,
    },
    "Spirit's Grotto: Bracelet": {
        "region_id": "d1 bracelet",
        "vanilla_item": "Progressive Bracelet",
        "flag_byte": 0xca10,
        "room": 0x0610,
        "dungeon": 1,
        "collect": COLLECT_TOUCH,
    },
    "Spirit's Grotto: Hit Color Block": {
        "region_id": "d1 hit color block",
        "vanilla_item": "Small Key (Spirit's Grotto)",
        "flag_byte": 0xc926,
        "room": 0x0426,
        "dungeon": 1,
        "collect": COLLECT_TOUCH,
    },
    "Spirit's Grotto: RNG puzzle": {
        "region_id": "d1 pully puzzle",
        "vanilla_item": "Small Key (Spirit's Grotto)",
        "flag_byte": 0xc922,
        "room": 0x0422,
        "dungeon": 1,
        "collect": COLLECT_CHEST,
    },
    "Spirit's Grotto: Rupee Under Pot": {
        "region_id": "d1 rupee under pot",
        "vanilla_item": "Rupees (200)",
        "flag_byte": 0xc91e,
        "room": 0x041e,
        "dungeon": 1,
        "collect": COLLECT_TOUCH,
    },
    "Spirit's Grotto: Boss Key Chest": {
        "region_id": "d1 boss key chest",
        "vanilla_item": "Boss Key (Spirit's Grotto)",
        "flag_byte": 0xc91d,
        "room": 0x041d,
        "dungeon": 1,
        "collect": COLLECT_CHEST,
    },
    "Spirit's Grotto: Boss": {
        "region_id": "d1 boss",
        "vanilla_item": "Heart Container",
        "flag_byte": 0xc913,
        "room": 0x0413,
        "dungeon": 1,
        "collect": COLLECT_TOUCH,
    },
    "Spirit's Grotto: Final Gift": {
        "region_id": "d1 final gift",
        "vanilla_item": "Ghastly Doll",
        "flag_byte": 0xc911,
        "room": 0x0411,
        "dungeon": 1,
        "collect": COLLECT_CHEST,
    },
    ##########################################
    "Lost Labyrinth (Present): Heart Piece": {
        "region_id": "lost labyrinth present heartpiece",
        "vanilla_item": "Piece of Heart",
        "flag_byte": 0xc97e, 
        "room": 0x047e,
        "map_tile": 0x33,
        "collect": COLLECT_TOUCH,
    },
    "Lost Labyrinth (Present): Nayru's House": {
        "region_id": "nayru's house",
        "vanilla_item": "Harp",
        "flag_byte": 0xc8ae, 
        "room": 0x03ae,
        "map_tile": 0x3a,
        "collect": COLLECT_TOUCH,
        "symbolic_name": "nayruHouse",
    },
}