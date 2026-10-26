from ...common.patching.RomData import RomData
from ...common.patching.rooms.decoding import decompress_room
from ..sym import sym
from ...common.patching.z80asm.Assembler import GameboyAddress
from ..Util import world_path
from ...common.patching.Util import simple_hex

import os
import json

def decompress_rooms(rom: RomData, parsed_sym: sym) -> list[bytearray]:
    room_layout_group_table = parsed_sym.find("label", "roomLayoutGroupTable").address_in_rom()
    table_addresses = []
    for label, addr in parsed_sym.get_labels().items():
        if label == f"roomLayoutGroup{len(table_addresses)}Table":
            table_addresses.append(addr)

    big_rooms_group_start = 5 if len(table_addresses) == 7 else 4

    room_data = []
    for group in range(len(table_addresses)):
        current_address = room_layout_group_table + group * 8
        room_type = 1 if group < big_rooms_group_start else 0
        base_address = GameboyAddress(
            rom.read_byte(current_address + 4),
            rom.read_word(current_address + 5)
        ).address_in_rom()

        if room_type == 1:
            for i in range(0x100):
                room_info = rom.read_word(table_addresses[group].address_in_rom() + i * 2)

                room_data.append(decompress_room(rom, base_address, room_type, room_info, None))
    return room_data