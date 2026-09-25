from .Util import world_path
from ..common.patching.z80asm.Assembler import *
import json
from typing import Any

def str_hex_to_int(h) -> int:
    return int("0x" + h, 0)

class sym():
    bank_limit = 0x0b
    def __init__(self):
        with open(world_path("disasm/ages.sym"), "rt") as f:
            self.array = []
            code = f.readline()
            while code != "":
                self.array.append(code.splitlines()[0])
                code = f.readline()

    def browse_sym(self, property) -> List[str]:
        found_property = False
        info = []
        for stuff in self.array:
            if not stuff:
                continue
            if stuff.startswith("[") and "]" in stuff:
                if found_property:
                    break
                if not found_property and stuff == f"[{property}]":
                    found_property = True
            elif found_property:
                info.append(stuff)
        return info
    
    def get_labels(self, change_gbAddress_offset = True) -> Dict[str, GameboyAddress]:
        info = {}
        for stuff in self.browse_sym("labels"):
            address, label = stuff.split(" ")
            bank, addr = address.split(":")
            if str_hex_to_int(addr[:1]) > self.bank_limit:
                continue
            info[label] = GameboyAddress(str_hex_to_int(bank), str_hex_to_int(addr), change_gbAddress_offset)
        return info

    def get_defs(self) -> Dict[str, int]:
        info = {}
        for stuff in self.browse_sym("definitions"):
            address, label = stuff.split(" ")
            info[label] = str_hex_to_int(address)
        return info
    
    def get_sections(self) -> List[Dict[str, Any]]:
        array = []
        for stuff in self.browse_sym("sections"):
            full_address, others = stuff.split(" ")
            bank_and_address, address, size, label = others.split(" ")
            addr = bank_and_address.split(":")[1]
            if str_hex_to_int(addr[:1]) > self.bank_limit:
                continue
            array.append({
                "full_address": str_hex_to_int(full_address),
                "bank_and_address": [str_hex_to_int(s) for s in bank_and_address.split(":")],
                "address": str_hex_to_int(address),
                "size": str_hex_to_int(size),
                "label": label
            })
        return array

    def find(self, type: str, label: str) -> None | Dict[str, Any] | Any:
        if type == "section":
            for section in self.get_sections():
                if section["label"] == label:
                    return section
        elif type.startswith("label"):
            labels = self.get_labels(type != "label_noChangeToGbAddressOffset")
            defs = self.get_defs()
            if label in labels:
                return labels[label]
            elif label in defs:
                return defs[label]
            else:
                return None
        return None