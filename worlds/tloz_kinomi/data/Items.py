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
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x04
    },
    "Rupees (40)": {
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x05
    },
    "Rupees (30)": {
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x06
    },
    "Rupees (60)": {
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x07
    },
    "Rupees (70)": {
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x08
    },
    "Rupees (25)": {
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x09
    },
    "Rupees (50)": {
        'classification': ItemClassification.useful,
        'id': 0x28,
        'subid': 0x0a
    },
    "Rupees (100)": {
        'classification': ItemClassification.useful,
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
        'classification': ItemClassification.useful,
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
        'classification': ItemClassification.filler,
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
    "Small Key (Crown Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
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
    "Master Key (Crown Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x30,
        'subid': 0x05
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
    "Boss Key (Crown Dungeon)": {
        'classification': ItemClassification.progression,
        'id': 0x31,
        'subid': 0x05
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
    "Compass (Crown Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x32,
        'subid': 0x05
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
    "Dungeon Map (Crown Dungeon)": {
        'classification': ItemClassification.useful,
        'id': 0x30,
        'subid': 0x05
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
        'classification': ItemClassification.useful,
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
