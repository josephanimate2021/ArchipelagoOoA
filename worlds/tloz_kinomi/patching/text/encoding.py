from ...common.patching.text.encoding import (
    GameboyAddress,
    RomData,
    encode_text_data,
    build_compact_table,
    simple_hex,
    logging
)
from ..data_manager.text import load_text_defines
from ..sym import sym
from ..Util import world_path

import json
import Utils

def write_text_data(rom: RomData, dictionary: dict[str, str], texts: dict[str, str], parsed_sym: sym):
    text_offset_len = 0
    while True:
        if parsed_sym.find("label", f"TEXT_OFFSET_{text_offset_len + 1}") is None:
            break
        text_offset_len += 1
    text_addresses_limit = parsed_sym.find("label", "room0000").address_in_rom()
    text_defines = load_text_defines()

    dicts = [{} for _ in range(text_offset_len)]
    bytesd = {}
    found_first_offset = False
    offset_count = 0
    for label, addr in parsed_sym.get_labels().items():
        if label.startswith("textTableENG_") and __debug__:
            bank, offset = addr.__str__().split(":")
            addr_end = parsed_sym.find_addr_end(bank, offset).address_in_rom()
            if addr_end != addr.address_in_rom():
                bytesd[label] = [simple_hex(int(i)) for i in rom.read_bytes(addr.address_in_rom(), addr_end - 1)]
        if addr == text_addresses_limit:
            break
        if label == f"TEXT_OFFSET_{offset_count + 1}":
            if not found_first_offset:
                found_first_offset = True
            offset_count += 1
        elif found_first_offset:
            for p, v in text_defines.items():
                val = label.split("_ADDR")[0]
                if (label.startswith("DICT") and label.endswith("_ADDR")) or v == val:
                    pr = val if label.startswith("DICT") else p
                    dicts[offset_count - 1][pr] = (
                        texts if label.startswith("TX_") else dictionary
                    )[pr]
                    break
    
    with open(world_path("debug.json"), "w") as f:
        f.write(json.dumps({
            "dicts": {f"dict{i}": dicts[i] for i in range(len(dicts))},
            "bytes": {p: v for p, v in bytesd.items()}
        },  indent=4))
    encoded_dicts = [encode_text_data(dicts[i], dictionary) for i in range(len(dicts))]
    encoded_dicts[0].update(encode_text_data(dictionary))

    #print(encoded_dicts)