from BaseClasses import ItemClassification
from ..patching.Constants import DEFINES

BASE_ITEM_ID = 27022002000

ITEMS_DATA = {
    #   "No Item": {
    #   'classification': ItemClassification.filler,
    #   "",
    #    'id': 0x00,
    #    'subid': 0x00
    #    },
    "Shield": {
        'classification': ItemClassification.progression,
        'id': 0x01
    },
    "Bombs (10)": {
        'classification': ItemClassification.progression,
        'id': 0x03
    },
    "Sword": {
        'classification': ItemClassification.progression,
        'id': 0x05
    },
    "Boomerang": {
        'classification': ItemClassification.progression,
        'id': 0x06,
        'subid': 0x03
    },
    "Rod of Seasons": {
        'classification': ItemClassification.progression,
        'id': 0x07
    },
    "Harp": {
        'classification': ItemClassification.progression,
        'id': 0x25,
        'subid': 0x00                                                                                                           
    },
    "Cane of Somaria": {
        'classification': ItemClassification.progression,
        'id': 0x04
    },
    "Biggoron's Sword": {
        'classification': ItemClassification.progression,
        'id': 0x0c
    },
    "Bombchus (10)": {
        'classification': ItemClassification.progression,
        'id': 0x0d
    },
    "Slingshot": {
        'classification': ItemClassification.progression,
        'id': 0x13
    },
    "Shovel": {
        'classification': ItemClassification.filler,
        'id': 0x15
    },
    "Progressive Bracelet": {
        'classification': ItemClassification.progression,
        'id': 0x16
    },
    "Roc's Cape": {
        'classification': ItemClassification.progression,
        'id': 0x17,
        'subid': 0x04
    },
    "Seed Satchel": {
        'classification': ItemClassification.progression,
        'id': 0x19
    },
    "Progressive Slingshot": {
        'classification': ItemClassification.progression,
        'id': 0x19
    },
    "Ember Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x20
    },
    "Scent Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x21
    },
    "Pegasus Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x22
    },
    "Gale Seeds": {
        'classification': ItemClassification.useful,
        'id': 0x23
    },
    "Mystery Seeds": {
        'classification': ItemClassification.progression,
        'id': 0x24
    },
    "Rupees (1)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x00
    },
    "Rupees (2)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x01
    },
    "Rupees (5)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x02
    },
    "Rupees (10)": {
        'classification': ItemClassification.filler,
        'id': 0x28,
        'subid': 0x03
    },
    "Rupees (20)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x04
    },
    "Rupees (40)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x05
    },
    "Rupees (30)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x06
    },
    "Rupees (60)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x07
    },
    "Rupees (70)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x08
    },
    "Rupees (25)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x09
    },
    "Rupees (50)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x0a
    },
    "Rupees (100)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x0b
    },
    "Rupees (200)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x0c
    },
    "Rupees (400)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x0d
    },
    "Rupees (150)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x0e
    },
    "Rupees (300)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x0f
    },
    "Rupees (500)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x10
    },
    "Rupees (900)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x11
    },
    "Rupees (80)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x12
    },
    "Rupees (999)": {
        'classification': ItemClassification.progression_skip_balancing,
        'id': 0x28,
        'subid': 0x13
    },
    
    "Heart Container": {
        'classification': ItemClassification.useful,
        'id': 0x2a
    },
    "Piece of Heart": {
        'classification': ItemClassification.useful,
        'id': 0x2b,
        'subid': 0x01
    },
    "Zora's Flippers": {
        'classification': ItemClassification.progression,
        'id': 0x2e
    },
    "Potion": {
        'classification': ItemClassification.useful,
        'id': 0x2f,
        'subid': 0x01
    },

    "Small Key (Summer Villa)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Small Key (Spirit's Grotto)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Small Key (Lost Labyrinth (Past))": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Small Key (Four Corners Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Small Key (Seasons Shrine)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Small Key (Lost Labyrinth (Present))": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x0b
    },
    "Small Key (Temple of The Tokay)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x0c
    },
    "Master Key (Summer Villa)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x00
    },
    "Master Key (Spirit's Grotto)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x01
    },
    "Master Key (Lost Labyrinth (Past))": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x02
    },
    "Master Key (Four Corners Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x03
    },
    "Master Key (Seasons Shrine)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x04
    },
    "Master Key (Lost Labyrinth (Present))": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x0b
    },
    "Master Key (Temple of The Tokay)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x0c
    },
    "Boss Key (Summer Villa)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x00
    },
    "Boss Key (Spirit's Grotto)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x01
    },
    "Boss Key (Lost Labyrinth (Past))": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x02
    },
    "Boss Key (Four Corners Cave)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x03
    },
    "Boss Key (Seasons Shrine)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x04
    },
    "Boss Key (Temple of The Tokay)": {
            'classification': ItemClassification.progression,
            'id': 0x31,
            'subid': 0x0c
    },
    "Compass (Summer Villa)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x00
    },
    "Compass (Spirit's Grotto)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x01
    },
    "Compass (Lost Labyrinth (Past))": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x02
    },
    "Compass (Four Corners Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x03
    },
    "Compass (Seasons Shrine)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x04
    },
    "Compass (Lost Labyrinth (Present))": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x0b
        },
    "Compass (Temple of The Tokay)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x0c
    },
    "Dungeon Map (Summer Villa)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x00
    },
    "Dungeon Map (Spirit's Grotto)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x01
    },
    "Dungeon Map (Lost Labyrinth (Past))": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x02
    },
    "Dungeon Map (Four Corners Cave)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x03
    },
    "Dungeon Map (Seasons Shrine)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x04
    },
    "Dungeon Map (Lost Labyrinth (Present))": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x0b
    },
    "Dungeon Map (Temple of The Tokay)": {
        'classification': ItemClassification.useful,
        'id': 0x33,
        'subid': 0x0c
    },

    "Gasha Seed": {
        'classification': ItemClassification.filler,
        'id': 0x34,
        'subid': 0x01
    },
    
    #     "Maku Seed": {
    #           'classification': ItemClassification.progression,
    #         'id': 0x36
    #     },

    "Ghastly Doll": {
        'classification': ItemClassification.progression,
        'id': 0x41
    },
    "Life Potion": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x01
    },
    "Wood Clock": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x02
    },
    "Broken Sword": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x03
    },
    "Sparring Book": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x04
    },
    "Mushroom": {
        'classification': ItemClassification.progression,
        'id': 0x41,
        'subid': 0x05
    },
    
    "Old Mining Key": {
        'classification': ItemClassification.progression,
        'id': 0x43
    },
    "Falls Key": {
        'classification': ItemClassification.progression,
        'id': 0x42,
    },
    "Old Labyrinth Key": {
        'classification': ItemClassification.progression,
        'id': 0x46
    },
    "Witch's Key": {
        'classification': ItemClassification.progression,
        'id': 0x45
    },
    "Slate": {
        'classification': ItemClassification.progression,
        'id': 0x4b
    },
    "Red Pearl": {
        'classification': ItemClassification.filler,
        'id': 0x4f
    },
    "Autumn Stone": {
        'classification': ItemClassification.progression,
        'id': 0x3c
    },
    "Summer Stone": {
        'classification': ItemClassification.progression,
        'id': 0x3b
    },
    "Winter Stone": {
        'classification': ItemClassification.progression,
        'id': 0x3a
    },
    "Spring Stone": {
        'classification': ItemClassification.progression,
        'id': 0x3d
    },
    "Zora Scale": {
        'classification': ItemClassification.filler,
        'id': 0x4e
    },
    "Blue Pearl": {
        'classification': ItemClassification.filler,
        'id': 0x50
    },

    "Friendship Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x04,
        'ring': 'useless'
    },
    "Power Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x05,
        'ring': 'good'
    },
    "Power Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x06,
        'ring': 'good'
    },
    "Power Ring L-3": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x07,
        'ring': 'good'
    },
    "Armor Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x08,
        'ring': 'good'
    },
    "Armor Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x09,
        'ring': 'good'
    },
    "Armor Ring L-3": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0a,
        'ring': 'good'
    },
    "Red Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0b,
        'ring': 'good'
    },
    "Blue Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0c,
        'ring': 'good'
    },
    "Green Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0d,
        'ring': 'good'
    },
    "Cursed Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0e,
        'ring': 'useless'
    },
    "Expert's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x0f,
        'ring': 'good'
    },
    "Blast Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x10,
        'ring': 'good'
    },
    "Rang Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x11,
        'ring': 'good'
    },
    "GBA Time Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x12,
        'ring': 'useless'
    },
    "Maple's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x13,
        'ring': 'good'
    },
    "Steadfast Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x14,
        'ring': 'good'
    },
    "Pegasus Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x15,
        'ring': 'good'
    },
    "Toss Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x16,
        'ring': 'good'
    },
    "Heart Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x17,
        'ring': 'good'
    },
    "Heart Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x18,
        'ring': 'good'
    },
    "Swimmer's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x19,
        'ring': 'good'
    },
    "Charge Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1a,
        'ring': 'good'
    },
    "Light Ring L-1": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1b,
        'ring': 'good'
    },
    "Light Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1c,
        'ring': 'good'
    },
    "Bomber's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1d,
        'ring': 'good'
    },
    "Green Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1e,
        'ring': 'good'
    },
    "Blue Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x1f,
        'ring': 'good'
    },
    "Gold Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x20,
        'ring': 'good'
    },
    "Red Luck Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x21,
        'ring': 'good'
    },
    "Green Holy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x22,
        'ring': 'good'
    },
    "Blue Holy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x23,
        'ring': 'good'
    },
    "Red Holy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x24,
        'ring': 'good'
    },
    "Snowshoe Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x25,
        'ring': 'good'
    },
    "Roc's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x26,
        'ring': 'good'
    },
    "Quicksand Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x27,
        'ring': 'good'
    },
    "Red Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x28,
        'ring': 'good'
    },
    "Blue Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x29,
        'ring': 'good'
    },
    "Gold Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2a,
        'ring': 'good'
    },
    "Green Joy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2b,
        'ring': 'good'
    },
    "Discovery Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2c,
        'ring': 'good'
    },
    "Rang Ring L-2": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2d,
        'ring': 'good'
    },
    "Octo Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2e,
        'ring': 'useless'
    },
    "Moblin Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x2f,
        'ring': 'useless'
    },
    "Like Like Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x30,
        'ring': 'useless'
    },
    "Subrosian Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x31,
        'ring': 'useless'
    },
    "First Gen Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x32,
        'ring': 'useless'
    },
    "Spin Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x33,
        'ring': 'good'
    },
    "Bombproof Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x34,
        'ring': 'good'
    },
    "Energy Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x35,
        'ring': 'good'
    },
    "Dbl. Edge Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x36,
        'ring': 'good'
    },
    "GBA Nature Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x37,
        'ring': 'useless'
    },
    "Slayer's Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x38,
        'ring': 'useless'
    },
    "Rupee Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x39,
        'ring': 'useless'
    },
    "Victory Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3a,
        'ring': 'useless'
    },
    "Sign Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3b,
        'ring': 'useless'
    },
    "100th Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3c,
        'ring': 'useless'
    },
    "Whisp Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3d,
        'ring': 'good'
    },
    "Gasha Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3e,
        'ring': 'good'
    },
    "Peace Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x3f,
        'ring': 'good'
    },
    "Zora Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x40,
        'ring': 'good'
    },
    "Fist Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x41,
        'ring': 'good'
    },
    "Whimsical Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x42,
        'ring': 'good'
    },
    "Protection Ring": {
        'classification': ItemClassification.filler,
        'id': 0x2d,
        'subid': 0x43,
        'ring': 'good'
    },

    "Eternal Song": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x00
    },
    "Wings of Passion": {
        'classification': ItemClassification.progression,
        'id': 0x40,
        'subid': 0x01
    },
}
