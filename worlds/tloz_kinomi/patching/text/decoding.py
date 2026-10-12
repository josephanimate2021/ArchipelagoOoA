from ...common.patching.RomData import RomData
from ...common.patching.Util import simple_hex
from ..sym import sym
from ...common.patching.text.decoding import decode_text
from typing import Any

def parse_texts(rom: RomData, parsed_sym: sym, dictionary: dict[str, str] | None = None):
    text_dict: dict[str, str] = {}
    texts = {}
    l = "TX_" if dictionary is not None else "DICT"

    for label, addr in parsed_sym.get_labels().items():
        if label.startswith(l) and label.endswith("_ADDR"):
            key = label.split("_ADDR")[0]
            text_dict[key] = decode_text(rom, addr.address_in_rom(), dictionary)

    if l == "TX_":
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
                        texts[key] = text_dict[i]
                        keys.append(key)
                        break
                    count += 1
            else:
                texts[i] = text_dict[i]
                keys.append(i)

    return text_dict if l != "TX_" else {p: texts[p] for p in sorted(texts.keys())}