from typing import Any, cast

from ..common.patching.text import normalize_text
from ..common.patching.Util import simple_hex
from ..common.patching.z80asm.Assembler import Z80Assembler
from ..data.Constants import SEED_ITEMS
from ..data.Locations import LOCATIONS_DATA
from ..data.Hints import *
import random

# -----------------------------------------------------------------------------------------------------
def process_item_name_for_shop_text(item: str) -> str:
    item_name = "🟥"
    item_name += item
    item_name = normalize_text(item_name)
    item_name += "⬜\\stop\n"
    return item_name

# -----------------------------------------------------------------------------------------------------
def mahe_shop_text(text: dict[str, str], patch_data: dict[str, Any]):
    overworld_shops = [
        "Lynna City: Shop",
        "Lynna City: Hidden Shop",
        "Yoll Graveyard: Syrup Shop",
        "Lynna Village: Advance Shop",
    ]
    
    shop_tx_indices = {
        "lynnaShop1":"TX_0101",
        "lynnaShop2":"TX_0102",
        "lynnaShop3":"TX_0103",
        "advanceShop1":"TX_0113",
        "advanceShop2":"TX_0118",
        "advanceShop3":"TX_0e24",
        "syrupShop1":"TX_0114",
        "syrupShop2":"TX_0117",
        "syrupShop3":"TX_0125",
        "hiddenShop1":"TX_0e09",
        "hiddenShop2":"TX_012a",
        "hiddenShop3":"TX_0131",

        "tokayMarket1":"TX_0a2a",
        "tokayMarket2":"TX_0a31",
    }

    #General Shops
    for shop_name in overworld_shops:
        for i in range(1, 4):
            location_name = f"{shop_name} Item #{i}"
            symbolic_name = LOCATIONS_DATA[location_name]["symbolic_name"]
            if location_name not in patch_data["locations"]:
                continue
            item_text = process_item_name_for_shop_text(patch_data["locations"][location_name])
            item_text += " \\num1 Rupees\n  \\optOK \\optNo thanks\\cmd(0f)"
            text[shop_tx_indices[symbolic_name]] = item_text

    #Tokay Market
    shop_name = "Crescent Island (Past): Market"
    for i in range(1, 3):
        location_name = f"{shop_name} Item #{i}"
        symbolic_name = LOCATIONS_DATA[location_name]["symbolic_name"]
        text_bytes = []
        if location_name not in patch_data["locations"]:
            continue
        item_text = process_item_name_for_shop_text(patch_data["locations"][location_name])
        if i == 1:
            item_text += " 10 Mystery Seed\n  \\optOK \\optNo thanks\\cmd(0f)"
        else:
            item_text += " 10 Scent Seed\n  \\optOK \\optNo thanks\\cmd(0f)"
        text[shop_tx_indices[symbolic_name]] = item_text

# ====================================================================================================
def get_region_hint_text(region_name: str, region_category: str) -> str:
    region_name = f"🟦{region_name}⬜"
    hint_text = "Did you know? "
    if region_category == "Foolish":
        hint_text += f"It is foolish to search {region_name}."
    elif region_category == "Golden":
        hint_text += f"Everything in {region_name} is precious!"
    else:
        hint_text += f"There are 🟩{region_category}⬜ precious treasures in {region_name}."
    return normalize_text(hint_text)

# -----------------------------------------------------------------------------------------------------
def get_random_joke_text(owl_id: int) -> tuple[str, str]:
    match random.randrange(6):
        case 0:
            location = [
                "Crown Dungeon",
                "Wing Dungeon",
                "Ancient Tomb",
                "Wing Dungeon",
                "Talus Peak",
                "Deku Forest",
                "Wing Dungeon",
                "Mermaid's Cave",
                "Mermaid's Cave",
                "Ancient Tomb",
                "Mermaid's Cave",
                "Moonlit Grotto",
                "Moonlit Grotto",
                #"Black Tower"
                "Western Rolling Ridge",
                "Jabu-Jabu's Belly",
                "Jabu-Jabu's Belly",
                "Jabu-Jabu's Belly",
            ][owl_id]
            return "\\link_name", location
        case 1:
            return "Ganon", "The Island of Koridai"
        case 2:
            return "Princess Zelda", "Another Castle"
        case 3:
            return "Maku Tree", "Lynna City"
        case 4:
            return "Ralph", "a hurry"
        case _:
            return "Maple", "the airs"

# -----------------------------------------------------------------------------------------------------
def make_hint_texts(texts: dict[str, str], patch_data) -> None:
    region_hints = patch_data["region_hints"]
    if len(region_hints):
        i = 0
        for region, category in region_hints:
            texts[KNOW_IT_ALL_BIRDS_TX[i]] = get_region_hint_text(region, category)
            i += 1

    item_hints = patch_data["item_hints"]
    if len(item_hints):
        for i in range(0x00, 0x1c):
            texts[f"TX_39{simple_hex(i)}"] = ""

        i = 0
        for hint in item_hints:
            if hint is None:
                item, location = get_random_joke_text(i)
            else:
                item, location, player = hint
                if player:
                    location = f"{player}'s {location}"
            text = f"They say that 🟥{item}⬜ can be found in 🟦{location}"
            text = normalize_text(text)

            texts[OWL_STATUE_TX[i]] = text
            i += 1

# ====================================================================================================
def make_dungeon_item_texts(texts: dict[str, str], patch_data) -> None:
    return
 
# ====================================================================================================
def make_entrance_blocker_texts(texts: dict[str, str], patch_data) -> None:
    return

# ====================================================================================================
def make_text_data(assembler: Z80Assembler, text: dict[str, str], patch_data: dict[str, Any]) -> None:
    mahe_shop_text(text, patch_data)
    make_hint_texts(text, patch_data)

    # impa refill
    item_text = "Let me refill\nyour supplies."
    text["TX_0122"] = item_text

    # Archipelago Item
    item_text = "You found 🟥an\nitem for another\nworld⬜!"
    text["TX_0057"] = item_text

    # Zora Potion
    item_text = "You got\n🟥King Zora's\nMagic Potion⬜!"
    text["TX_0045"] = item_text

    # Maku road Sign Replacement
    options = patch_data["options"]
    requiredEssences = options["required_essences"]
    requiredSlates = options["required_slates"]

    item_text = f"You need 🟩{requiredEssences}⬜\nessences to get\nthe Maku Seed\\stop\n"
    item_text += f"You need 🟩{requiredSlates}⬜\nslates to open\nD8 basement"
    text["TX_0564"] = item_text

    
