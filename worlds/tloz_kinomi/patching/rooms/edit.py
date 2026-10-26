import pkgutil
from typing import Any

from settings import get_settings

from ...common.patching.Util import simple_hex
from ...common.patching.RomData import RomData
from .decoding import decompress_rooms
from ..sym import sym

### How rooms work:
# Room number 0xYZZ = group Y, room ZZ
# Group 0 is the present overworld (usually 0ZZ)
# Group 1 is the past overworld (usually 1ZZ)
# Groups 2-3 are small indoor rooms and parts of it being underwater regions of both present/past (usually 2ZZ/3ZZ)
# Groups 4-5 are the big rooms (usually 4ZZ/5ZZ and 6ZZ)

# Positions are assessed with YX format
# Positions in small rooms are written in decimal, as a line is 10 tiles long
# Positions in big rooms are written in hex, as a line is 15 tiles long

# If editing big rooms, you'll need to call the edit_room_manually function as normal room compression does not work on hack base roms for some reason.
def apply_room_edits(rom_data: RomData, patch_data: dict[str, Any], parsed_sym: sym) -> list[bytearray]:
    room_data = decompress_rooms(rom_data, parsed_sym)

    apply_misc_edits(room_data, patch_data, parsed_sym, rom_data)
    apply_lostLabyrinth_edits(patch_data, room_data, parsed_sym, rom_data)

    return room_data

def apply_lostLabyrinth_edits(patch_data, room_data, parsed_sym: sym, rom_data: RomData):
    if patch_data["options"]["remove_extra_stairs_from_lost_labyrinth_past"]:
        room_data[0x162][67] = 0x3a
        room_data[0x151][27] = 0x3a
        room_data[0x163][37] = 0xd8
        t = 0x7b
        for i in range(0x457, 0x477, 0x10):
            edit_room_manually(i, t, 0xa0, parsed_sym, rom_data)
            edit_room_manually(i, 0x79, 0x53, parsed_sym, rom_data)
            t -= 0x10

def apply_misc_edits(room_data, patch_data, parsed_sym: sym, rom_data: RomData):
    if patch_data["options"]["shuffle_entrances"]["portals"]: # This is mostly for removing barriers since some portals are being randomized without logic.
        room_data[0x308][31] = 0xa0
        room_data[0x379][34] = 0xef
        room_data[0x318][28] = 0xa0
        for i in range(0x008, 0x208, 0x100):
            room_data[i][27] = 0x3a
        edit_room_manually(0x562, 0x37, 0xeb, parsed_sym, rom_data)
        edit_room_manually(0x562, 0x47, 0xb2, parsed_sym, rom_data)
    if patch_data["options"]["open_staircase_to_ancient_ages_locations"]: # Adds staircase to kinomi town
        room_data[0x012][37] = 0xdc

def edit_room_manually(room: int, position: int, new_tile: int, parsed_sym: sym, rom_data: RomData):
    """
    Applies manual edits to a specified room plus the position

    Parameters:
        room (int): A specified number of a screen in the game. Anything above that will result in an AssertionError depending on the loaded sym.
        position (int): XY format of there the tile is that you want to edit. Anything above that will result in an AssertionError.
        new_tile (int): A new tile to place. It has to be a hex number ranging from 0x00 to 0xff. Anything above that will result in an AssertionError.
        parsed_sym (sym): Contents from a loaded sym file (as a class)
        big_rooms_group_start (int): Amount of room groups in the game.
        rom_data (RomData) Result of the ROM from the RomData class.
    """

    # Check for errors.
    assert position < 0x100, "The position of a tile cannot be above 0xff."
    assert new_tile < 0x100, "Tiles cannot be above 0xff."
    room_addr = parsed_sym.find("label", f"room{simple_hex(room, 4)}").address_in_rom()
    assert room_addr is not None, f"Room {simple_hex(room, 4)} is not valid in the loaded sym."

    # Modify the room if no errors are present.
    rom_data.write_byte(room_addr + position, new_tile)
