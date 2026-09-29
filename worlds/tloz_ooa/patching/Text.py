import json
from pathlib import Path

from typing import Any

import Utils
from ..common.patching.RomData import RomData
from ..common.patching.Util import simple_hex
from ..common.patching.data_manager.text import get_text_data
from ..common.patching.text import normalize_text


def load_modded_ages_text_data() -> None | tuple[dict[str, str], dict[str, str]]:
    from .. import OracleOfAgesWorld
    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    dict_file = text_dir.joinpath("ages_dict.json")
    if not dict_file.is_file():
        return None

    text_file = text_dir.joinpath(f"ages_texts.json")
    if text_file.is_file():
        texts: dict[str, Any] = json.load(open(text_file, encoding="utf-8"))
        version = texts.pop("version")
        if version == OracleOfAgesWorld.version():
            return json.load(open(dict_file, encoding="utf-8")), texts

    vanilla_text_file = text_dir.joinpath(f"ages_texts_vanilla.json")
    if not vanilla_text_file.is_file():
        return None
    texts = json.load(open(vanilla_text_file, encoding="utf-8"))
    apply_text_edits(texts)
    save_ages_edited_text_data(texts)
    return json.load(open(dict_file, encoding="utf-8")), texts

def save_ages_edited_text_data(texts: dict[str, str]) -> None:
    from .. import OracleOfAgesWorld
    texts["version"] = OracleOfAgesWorld.version()

    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    text_file = text_dir.joinpath(f"ages_texts.json")

    with text_file.open("w", encoding="utf-8") as f:
        json.dump(texts, f, ensure_ascii=False)

    del texts["version"]

def apply_text_edits(texts: dict[str, str]) -> None:
    texts["TX_2d11"] = "" # Symmetry Sister Ramble about the black tower
    texts["TX_301a"] = "" # One of Vasu snake text
    texts["TX_3026"] = "" # More of Vasu snake text
    texts["TX_5809"] = "  \\opt()Yes \\opt()No" # Patch ceremony Explanation...
    
    # impa refill
    item_text = "Let me refill\nyour supplies."
    texts["TX_0122"] = item_text

    # Archipelago Item
    item_text = "You found 🟥an\nitem for another\nworld⬜!"
    texts["TX_0057"] = item_text

    # Zora Potion
    item_text = "You got\n🟥King Zora's\nMagic Potion⬜!"
    texts["TX_0045"] = item_text

    # Ring Appraisal
    item_text = "You got the\n🟥\\call(fd)⬜!"
    texts["TX_301c"] = item_text
    return

def get_modded_ages_text_data(rom_data: RomData) -> tuple[dict[str, str], dict[str, str]]:
    #result = load_modded_ages_text_data()
    #if result is not None:
    #    return result

    dictionary, texts = get_text_data(rom_data, True, False)
    apply_text_edits(texts)
    save_ages_edited_text_data(texts)
    return dictionary, texts
