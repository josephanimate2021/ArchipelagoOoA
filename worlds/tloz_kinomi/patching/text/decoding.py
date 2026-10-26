from ...common.patching.RomData import RomData
from ...common.patching.Util import simple_hex
from ..sym import sym
from ...common.patching.text.decoding import decode_text
from typing import Any

def parse_texts(rom: RomData, parsed_sym: sym, dictionary: dict[str, str] | None = None):
    text_dict: dict[str, str] = {}
    texts = {}
    textDefines = {}
    l = "TX_" if dictionary is not None else "DICT"

    for label, addr in parsed_sym.get_labels().items():
        if label.startswith(l) and label.endswith("_ADDR"):
            key = label.split("_ADDR")[0]
            text_dict[key] = decode_text(rom, addr.address_in_rom(), dictionary)

    if l == "TX_": # Texts are always changed, so we will have to create some modifications.
        group = 0
        keys = []
        for i in text_dict.keys():
            if f"TX_{simple_hex(group)}" not in i:
                group += 1
            if i.startswith(f"TX_{simple_hex(group)}_"):
                count = 0
                while True:
                    key = f"TX_{simple_hex(group)}{simple_hex(count)}"
                    if key not in keys:
                        textDefines[key] = i
                        texts[key] = text_dict[i]
                        keys.append(key)
                        break
                    count += 1
            else:
                textDefines[i] = i
                texts[i] = text_dict[i]
                keys.append(i)
        return [{p: i[p] for p in sorted(i.keys())} for i in [texts, textDefines]]
    else: # Dicts won't be changed for a while. So just return what was decoded to speed things up.
        return text_dict, {}