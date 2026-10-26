import json
from pathlib import Path

import Utils
from ...common.patching.RomData import RomData
from ..text.decoding import parse_texts
from ..sym import sym


def load_vanilla_dict_data() -> None | dict[str, str]:
    """
    Gets the vanilla dict, this is always assumed to already exist
    """
    from ...world import GiftsOfKinomiWorld
    game_name = GiftsOfKinomiWorld.game_nickname

    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    vanilla_text_file = text_dir.joinpath(f"{game_name}_dict.json")
    return json.load(open(vanilla_text_file, encoding="utf-8"))


def load_vanilla_text_data() -> None | dict[str, str]:
    from ...world import GiftsOfKinomiWorld
    game_name = GiftsOfKinomiWorld.game_nickname

    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    vanilla_text_file = text_dir.joinpath(f"{game_name}_texts_vanilla.json")
    if not vanilla_text_file.is_file():
        return None
    return json.load(open(vanilla_text_file, encoding="utf-8"))

def load_text_defines() -> None | dict[str, str]:
    from ...world import GiftsOfKinomiWorld
    game_name = GiftsOfKinomiWorld.game_nickname

    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    vanilla_text_file = text_dir.joinpath(f"{game_name}_text_defines.json")
    return json.load(open(vanilla_text_file, encoding="utf-8"))


def save_vanilla_text_data(dictionary: dict[str, str], texts: dict[str, str]) -> None:
    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    text_dir.mkdir(parents=True, exist_ok=True)

    from ...world import GiftsOfKinomiWorld
    game_name = GiftsOfKinomiWorld.game_nickname
    dict_file = text_dir.joinpath(f"{game_name}_dict.json")
    text_file = text_dir.joinpath(f"{game_name}_texts_vanilla.json")

    with dict_file.open("w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False,  indent=4)

    with text_file.open("w", encoding="utf-8") as f:
        json.dump(texts, f, ensure_ascii=False,  indent=4)

def save_text_defines(textDefines: dict[str, str]) -> None:
    text_dir = Path(Utils.cache_path("oos_ooa/text"))
    text_dir.mkdir(parents=True, exist_ok=True)

    from ...world import GiftsOfKinomiWorld
    game_name = GiftsOfKinomiWorld.game_nickname
    textDefines_file = text_dir.joinpath(f"{game_name}_text_defines.json")

    with textDefines_file.open("w", encoding="utf-8") as f:
        json.dump(textDefines, f, ensure_ascii=False,  indent=4)


def get_text_data(rom_data: RomData, get_dictionary: bool, parsed_sym: sym) -> tuple[None | dict[str, str], dict[str, str]]:
    result = load_vanilla_text_data()
    if result is not None:
        if get_dictionary:
            dictionary = load_vanilla_dict_data()
        else:
            dictionary = None
        return dictionary, result

    dictionary, _ = parse_texts(rom_data, parsed_sym)
    texts, defines = parse_texts(rom_data, parsed_sym, dictionary)
    save_vanilla_text_data(dictionary, texts)
    save_text_defines(defines)
    return dictionary, texts