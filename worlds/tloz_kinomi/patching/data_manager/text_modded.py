import json
from pathlib import Path

from typing import Any

import Utils
from ...common.patching.RomData import RomData
from ...common.patching.Util import simple_hex
from .text import get_text_data
from ...common.patching.text import normalize_text
from ..sym import sym


def load_modded_text_data() -> None | tuple[dict[str, str], dict[str, str]]:
    from ...world import GiftsOfKinomiWorld
    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    dict_file = text_dir.joinpath(f"{GiftsOfKinomiWorld.game_nickname}_dict.json")
    if not dict_file.is_file():
        return None

    text_file = text_dir.joinpath(f"{GiftsOfKinomiWorld.game_nickname}_texts.json")
    if text_file.is_file():
        texts: dict[str, Any] = json.load(open(text_file, encoding="utf-8"))
        version = texts.pop("version")
        if version == GiftsOfKinomiWorld.version():
            return json.load(open(dict_file, encoding="utf-8")), texts

    vanilla_text_file = text_dir.joinpath(f"{GiftsOfKinomiWorld.game_nickname}_texts_vanilla.json")
    if not vanilla_text_file.is_file():
        return None
    texts = json.load(open(vanilla_text_file, encoding="utf-8"))
    apply_text_edits(texts)
    save_edited_text_data(texts)
    return json.load(open(dict_file, encoding="utf-8")), texts


def save_edited_text_data(texts: dict[str, str]) -> None:
    from ...world import GiftsOfKinomiWorld
    texts["version"] = GiftsOfKinomiWorld.version()

    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    text_file = text_dir.joinpath(f"{GiftsOfKinomiWorld.game_nickname}_texts.json")

    with text_file.open("w", encoding="utf-8") as f:
        json.dump(texts, f, ensure_ascii=False, indent=4)

    del texts["version"]

# TODO
def apply_text_edits(texts: dict[str, str]) -> None:
    return


def get_modded_text_data(rom_data: RomData, parsed_sym: sym) -> tuple[dict[str, str], dict[str, str]]:
    result = load_modded_text_data()
    if result is not None:
        return result

    dictionary, texts = get_text_data(rom_data, True, parsed_sym)
    apply_text_edits(texts)
    save_edited_text_data(texts)
    return dictionary, texts