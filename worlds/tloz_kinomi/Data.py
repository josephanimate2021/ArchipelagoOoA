from typing import Dict, List
from BaseClasses import Item
from .data import LOCATIONS_DATA, ITEMS_DATA


from typing import Any


def build_location_name_to_id_dict() -> Dict[str, int]:
    location_name_to_id: Dict[str, int] = {}
    current_index = 27022002000
    for loc_name in LOCATIONS_DATA:
        location_name_to_id[loc_name] = current_index
        current_index += 1
    return location_name_to_id


def build_item_name_to_id_dict() -> dict[str, int]:
    item_name_to_id: dict[str, int] = {}
    for item_name, item in ITEMS_DATA.items():
        index = item["id"] * 0x100 + (item["subid"] if "subid" in item else 0)
        item_name_to_id[item_name] = index
    return item_name_to_id


def build_item_id_to_name_dict() -> dict[int, str]:
    item_id_to_name: dict[int, str] = {}
    for item_name, item in ITEMS_DATA.items():
        index = item["id"] * 0x100 + (item["subid"] if "subid" in item else 0)
        item_id_to_name[index] = item_name
    return item_id_to_name


def get_prices_pool():
    prices_pool = [300]                 # 1%
    prices_pool.extend([200] * 7)       # 8%
    prices_pool.extend([100] * 15)      # 50%
    prices_pool.extend([80] * 15)       # 65%
    prices_pool.extend([60] * 42)       # 80%
    prices_pool.extend([40] * 15)       # 95%
    prices_pool.extend([20] * 4)        # 99%
    prices_pool.append(0)               # 100%
    return prices_pool