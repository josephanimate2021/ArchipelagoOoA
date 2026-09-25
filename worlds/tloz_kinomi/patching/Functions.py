from typing import List

import os
import random
import Utils
from settings import get_settings
from ..common.patching.RomData import RomData
from .Util import *
from .treasureAddresses import sym
from ..common.patching.z80asm.Assembler import Z80Assembler
from ..common.patching.z80asm.Assembler import GameboyAddress
from ..data.Constants import *
from .Constants import *
from pathlib import Path

from .. import LOCATIONS_DATA, GiftsOfKinomiMasterKeys


def get_treasure_addr(parsed_sym: sym, rom: RomData, item_name: str):
    item_id, item_subid = get_item_id_and_subid(item_name)
    addr = parsed_sym.find("section", "TreasureObjectData")["full_address"] + (item_id * 4)
    if rom.read_byte(addr) & 0x80 != 0:
        addr = parsed_sym.find("section", "Bank_15")["full_address"] + rom.read_word(addr + 1)
    return addr + (item_subid * 4)

def set_static_items(parsed_sym: sym, rom: RomData, patch_data):
    for location_name, location_data in LOCATIONS_DATA.items():
        if location_name in patch_data["locations"]:
            item_name = patch_data["locations"][location_name]
        else:
            item_name = location_data["vanilla_item"]

        itemsTableAddr = parsed_sym.find("label", "itemsTable").address_in_rom()
        for i in range(len(STATIC_ITEM_ROOM_ORDER)):
            if location_data["room"] == STATIC_ITEM_ROOM_ORDER[i]:
                item_id, item_subid = get_item_id_and_subid(item_name)
                rom.write_bytes(itemsTableAddr + i, [item_id, item_subid])

def set_boss_items(parsed_sym: sym, rom: RomData, patch_data, i=0):
    no_boss_dungeons = [2, 6]
    for location_name, location_data in LOCATIONS_DATA.items():
        if i == 7: # base case for the recursive function
            break
        elif i in no_boss_dungeons: # continue on if there are no bosses for that dungeon.
            set_boss_items(parsed_sym, rom, patch_data,i+1)
            break
        elif "dungeon" in location_data and location_data["dungeon"] == i: # write down the boss checks if there is a dungeon with a boss in it.
            if location_name.endswith(" Boss") and location_name in patch_data["locations"]:
                item_id, item_subid = get_item_id_and_subid(patch_data["locations"][location_name])
                rom.write_bytes(parsed_sym.find("label", "bossItemTable").address_in_rom() + (
                    0x0c if i == 5
                    else i
                ), [item_id, item_subid])
                set_boss_items(parsed_sym, rom, patch_data, i+1)
                break

def set_refill_npc(rom: RomData):
    if get_settings().tloz_kinomi_options.refill_npc in REFILL_NPCS:
        refill_npc_addr = REFILL_NPCS[get_settings().tloz_kinomi_options.refill_npc]
        rom.write_byte(refill_npc_addr, 0x01)
    elif get_settings().tloz_kinomi_options.refill_npc != "disabled":
        raise Exception(get_settings().tloz_kinomi_options.refill_npc + " is not a valid option for the refill npc.")

def modify_required_gifts_and_slates_count(parsed_sym: sym, rom: RomData, patch_data):

    # Firstly, modify the sign outside link's house that says the required gifts and slates count.
    rom.write_byte(GameboyAddress(0x22, 0x602c).address_in_rom(), 0x30 + patch_data["options"]["required_gifts"])
    if patch_data["options"]["required_gifts"] == 1:
        rom.write_byte(GameboyAddress(0x22, 0x6032).address_in_rom(), 0x20)
    rom.write_byte(GameboyAddress(0x22, 0x6051).address_in_rom(), 0x30 + patch_data["options"]["required_slates"])
    if patch_data["options"]["required_slates"] == 1:
        rom.write_byte(GameboyAddress(0x22, 0x6058).address_in_rom(), 0x20)

    # Then, we modify the amount of slates neeeded to open the stairs to the temple of the tokay boss room.
    rom.write_byte(GameboyAddress(0x0a, 0x6505).address_in_rom(), patch_data["options"]["required_slates"])

    # And the gifts required to beat ganon.
    rom.write_byte(GameboyAddress(0x04, 0x648c).address_in_rom(), patch_data["options"]["required_gifts"]) # For summoning a tree in forever falls.
    rom.write_byte(GameboyAddress(0x0b, 0x4eb2).address_in_rom(), patch_data["options"]["required_gifts"]) # For getting a din interaction responsible for the zelda getting kidnapped cutscene, which we'll use for the indication that a user got the exact gifts neexed.

def get_asm_files(patch_data):
    if patch_data["options"]["remove_extra_stairs_from_lost_labyrinth_past"]:
        ASM_FILES.append("asm/conditional/no_extra_stairs_for_lost_labyrinth.yaml")
    if patch_data["options"]["open_staircase_to_ancient_ages_locations"]:
        ASM_FILES.append("asm/conditional/add_some_ages_old_locations.yaml")
    return ASM_FILES

def set_treasure_data(parsed_sym: sym, rom: RomData,
                      item_name: str, text_id: int | None,
                      sprite_id: int | None = None,
                      param_value: int | None = None):
    addr = get_treasure_addr(parsed_sym, rom, item_name)
    if text_id is not None:
        rom.write_byte(addr + 0x02, text_id)
    if sprite_id is not None:
        rom.write_byte(addr + 0x03, sprite_id)
    if param_value is not None:
        rom.write_byte(addr + 0x01, param_value)

def alter_treasures(parsed_sym: sym, rom: RomData):

    set_treasure_data(parsed_sym, rom, "Potion", 0x6d)

    # Set data for remote Archipelago items
    set_treasure_data(parsed_sym, rom, "Archipelago Item", 0x57, 0x5a)
    set_treasure_data(parsed_sym, rom, "Archipelago Progression Item", 0x57, 0x59)
    #set_treasure_data(parsed_sym, rom, "King Zora's Potion", 0x45, 0x5e)

    # Make bombs increase max carriable quantity when obtained from treasures,
    # not drops (see asm/seasons/bomb_bag_behavior)
    set_treasure_data(parsed_sym, rom, "Bombs (10)", None, None, 0x90)

def process_item_name_for_shop_text(item_name: str) -> List[int]:
    words = item_name.split(" ")
    current_line = 0
    lines = [""]
    while len(words) > 0:
        line_with_word = lines[current_line]
        if len(line_with_word) > 0:
            line_with_word += " "
        line_with_word += words[0]
        if len(line_with_word) <= 16:
            lines[current_line] = line_with_word
        else:
            current_line += 1
            lines.append(words[0])
        words = words[1:]

    result = []
    for line in lines:
        if len(result) > 0:
            result.append(0x01)  # Newline
        result.extend(line.encode())
    return result


def write_chest_contents(parsed_sym: sym, rom: RomData, patch_data):
    """
    Chest locations are packed inside several big tables in the ROM, unlike other more specific locations.
    This puts the item described in the patch data inside each chest in the game.
    """
    for location_name, location_data in LOCATIONS_DATA.items():
        if (
            'collect' not in location_data 
            or 'room' not in location_data 
            or location_data['collect'] != COLLECT_CHEST
            or location_name not in patch_data["locations"]
        ):
            continue
        else:
            chest_addr = rom.get_chest_addr(location_data['room'], 0x16, 0x55ed)
        item_name = patch_data["locations"][location_name]
        item_id, item_subid = get_item_id_and_subid(item_name)
        rom.write_byte(chest_addr, item_id)
        rom.write_byte(chest_addr + 1, item_subid)

def write_rando_npcItem_contents(parsed_sym: sym, rom: RomData, patch_data):
    """
    Items given by NPCs work differently than freestanding items, which is why they are much easier to work with
    """
    for location_name, location_data in LOCATIONS_DATA.items():
        if (
            'room' not in location_data
            or location_name not in patch_data["locations"]
            or "collect" not in location_data
            or location_data["collect"] != COLLECT_TOUCH
        ):
            continue

        item_name = patch_data["locations"][location_name]
        item_id, item_subid = get_item_id_and_subid(item_name)
        if "addr" in location_data:
            rom.write_bytes(location_data["addr"], [item_id, item_subid])

def force_collect_mode_on_nonchest_items(parsed_sym: sym, rom: RomData, patch_data, treasure_object_addresss):
    """
    Takes an item object code and changes it's collect mode to accomidate for the modifications
    """
    def get_info():
        info = {
            'items_count': {},
            'item_subids_to_avoid': {}
        }
        for location_name, location_data in LOCATIONS_DATA.items():
            if (
                'room' not in location_data
                or location_name not in patch_data["locations"]
                or "collect" not in location_data
            ):
                continue
            item_name = patch_data["locations"][location_name]
            if item_name not in info['items_count']:
                info["items_count"][item_name] = 1
            else:
                info["items_count"][item_name] += 1
            item_id, item_subid = get_item_id_and_subid(item_name)
            if location_data["collect"] == COLLECT_CHEST:
                if item_id not in info["item_subids_to_avoid"]:
                    info["item_subids_to_avoid"][item_id] = [item_subid]
                else:
                    info["item_subids_to_avoid"][item_id].append(item_subid)
        return info
    print(get_info())

    
def inject_slot_name(rom: RomData, slot_name: str):
    slot_name_as_bytes = list(str.encode(slot_name))
    slot_name_as_bytes += [0x00] * (0x40 - len(slot_name_as_bytes))
    rom.write_bytes(0xfffc0, slot_name_as_bytes)

def set_newGame_stuff(parsed_sym: sym, rom: RomData):
    rom.write_byte(GameboyAddress(0x02, 0x420f).address_in_rom(), 0x02) # Skip the screen to select link, secret or new game and skip to new game
    rom.write_byte(GameboyAddress(0x01, 0x7fc1).address_in_rom(), 0x00) # Set starting bomb to 0.
    rom.write_byte(GameboyAddress(0x02, 0x792f).address_in_rom(), 0x14) # Sets the bank to 14 for the file select text.
    
def write_seed_tree_content(rom: RomData, patch_data):
    for _, tree_data in SEED_TREE_DATA.items():
        original_data = rom.read_byte(tree_data["codeAdress"])
        item_name = patch_data["locations"][tree_data["location"]]
        item_id, _ = get_item_id_and_subid(item_name)
        newdata = (original_data & 0x0f) | (item_id - 0x20) << 4
        rom.write_bytes(tree_data["codeAdress"], [newdata])

# helper function that adds param2 to i unless stopped by my base case, which is helpful for finding the right rom address for a certain param in a table despite changes in the disasm code.
def find_address_for_param_helper(lineNumber, param, param2 = 4, i=0,c=0):
    return i - param if c == lineNumber else find_address_for_param_helper(lineNumber, param, param2, i + param2, c + 1)

def set_dungeon_warps(parsed_sym: sym, rom: RomData, patch_data):
    warp_matchings = patch_data["dungeon_entrances"]
    entrance_dest_groups = []
    exit_dest_groups = []
    warp_array_indexes = {}

    # Apply warp matchings expressed in the patch
    for i in range(len(warp_matchings)): # STEP 1: Get all of the necessary bytes appended to an array for the update.
        warp_array_indexes[warp_matchings[i][0]] = i
        dWarp = DUNGEON_WARPS[i]
        def loop(t, update_array):
            index_label, index_lineNumber = dWarp[t]
            label = f"group{index_label}WarpSources" if isinstance(index_label, int) else index_label
            base_address = parsed_sym.find("label", label)
            if base_address is not None:
                bytes_count = find_address_for_param_helper(index_lineNumber, 2)
                update_array.append(rom.read_byte(GameboyAddress(base_address.bank, base_address.offset + bytes_count).address_in_rom()))
        for t in [["entrance", entrance_dest_groups], ["exit", exit_dest_groups]]:
            loop(t[0], t[1])
    for e in warp_matchings: # STEP 2: Apply all warps to their randomized position using all gathered bytes
        def modify_warp(from_index, to_index, t, array):
            from_index_label, from_index_lineNumber = DUNGEON_WARPS[from_index][t]
            entrance_label = f"group{from_index_label}WarpSources" if isinstance(from_index_label, int) else from_index_label
            base_address = parsed_sym.find("label", entrance_label)
            if base_address is not None:
                bytes_count = find_address_for_param_helper(from_index_lineNumber, 2)
                rom.write_byte(GameboyAddress(base_address.bank, base_address.offset + bytes_count).address_in_rom(), array[to_index])
        for d in [[warp_array_indexes[e[0]], warp_array_indexes[e[1]], "entrance", entrance_dest_groups], [warp_array_indexes[e[1]], warp_array_indexes[e[0]], "exit", exit_dest_groups]]:
            modify_warp(d[0], d[1], d[2], d[3])

    #    # Change Minimap popups to indicate the randomized dungeon's name
    #    for i in range(8):
    #        entrance_name = f"d{i}"
    #        dungeon_index = int(warp_matchings[entrance_name][1:])
    #        map_tile = DUNGEON_ENTRANCES[entrance_name]["map_tile"]
    #        rom.write_byte(0x???? + map_tile, 0x81 | (dungeon_index << 3))

def set_file_select_text(assembler: Z80Assembler, slot_name: str):
    def char_to_tile(c: str) -> int:
        if '0' <= c <= '9':
            return ord(c) - 0x20
        if 'A' <= c <= 'Z':
            return ord(c) + 0xa1
        if c == '+':
            return 0xfd
        if c == '-':
            return 0xfe
        if c == '.':
            return 0xff
        else:
            return 0xfc  # All other chars are blank spaces

    row_1 = [char_to_tile(c) for c in f"ARCHIP. {VERSION}".center(16, " ")]
    row_2 = [char_to_tile(c) for c in slot_name.replace("-", " ").upper().center(16, " ")]

    text_tiles = [0x74, 0x31]
    text_tiles.extend(row_1)
    text_tiles.extend([0x41, 0x40])
    text_tiles.extend([0x02] * 12)  # Offscreen tiles

    text_tiles.extend([0x40, 0x41])
    text_tiles.extend(row_2)
    text_tiles.extend([0x51, 0x50])
    text_tiles.extend([0x02] * 12)  # Offscreen tiles

    assembler.add_floating_chunk("dma_FileSelectStringTiles", text_tiles)

    
def set_heart_beep_interval_from_settings(rom: RomData):
    heart_beep_interval = get_settings()["tloz_kinomi_options"]["heart_beep_interval"]
    if heart_beep_interval == "half":
        rom.write_byte(0x914B, 0x3f * 2)
    elif heart_beep_interval == "quarter":
        rom.write_byte(0x914B, 0x3f * 4)
    elif heart_beep_interval == "disabled":
        rom.write_bytes(0x914B, [0x00, 0xc9])  # Put a return to avoid beeping entirely

def set_character_sprite_from_settings(parsed_sym, rom: RomData):
    sprite = get_settings()["tloz_kinomi_options"]["character_sprite"]
    sprite_dir = Path(Utils.local_path(os.path.join('data', 'sprites', 'oos_ooa')))
    if sprite == "random":
        sprite_filenames = [f for f in os.listdir(sprite_dir) if sprite_dir.joinpath(f).is_file() and f.endswith(".bin")]
        sprite = sprite_filenames[random.randint(0, len(sprite_filenames) - 1)]
    elif not sprite.endswith(".bin"):
        sprite += ".bin"
    if sprite != "link.bin":
        sprite_path = sprite_dir.joinpath(sprite)
        if not (sprite_path.exists() and sprite_path.is_file()):
            raise ValueError(f"Path '{sprite_path}' doesn't exist")
        sprite_bytes = list(Path(sprite_path).read_bytes())
        rom.write_bytes(0x68000, sprite_bytes)

    palette = get_settings()["tloz_kinomi_options"]["character_palette"]
    if palette == "random":
        palette = random.choice(get_available_random_colors_from_sprite_name(sprite))

    if palette == "green":
        return  # Nothing to change
    if palette not in PALETTE_BYTES:
        raise ValueError(f"Palette color '{palette}' doesn't exist (must be 'green', 'blue', 'red' or 'orange')")
    palette_byte = PALETTE_BYTES[palette]

    # Link palette restored after Medusa Head / Ganon stun attacks
    rom.write_byte(0x15271, 0x08 | palette_byte)


    # Link in file select (still and moving)
    fileSelectDrawLink = [parsed_sym.find("label", f"fileSelectDrawLink@sprites{i}").address_in_rom() + 4 for i in range(3)]
    for i in range(2):
        rom.write_byte(fileSelectDrawLink[i], palette_byte)
        rom.write_byte(fileSelectDrawLink[i] + 4, palette_byte)
    rom.write_byte(fileSelectDrawLink[2], 0x20 | palette_byte)
    rom.write_byte(fileSelectDrawLink[2] + 4, 0x20 | palette_byte)

def apply_misc_option(rom: RomData, patch_data):
    if patch_data["options"]["master_keys"] != GiftsOfKinomiMasterKeys.option_disabled:
        # Remove small key consumption on keydoor opened
        rom.write_byte(0x18366, 0x00)
        # Change obtention text
        rom.write_bytes(0x78247, [0x4d, 0x61, 0x73, 0x74, 0x65, 0x72, 0x20, 0x4b, 0x65, 0x79, 0x09, 0x01, 0x21, 0x00]) # I really wish that the dictionnay of ages would be more useful...
    if patch_data["options"]["master_keys"] == GiftsOfKinomiMasterKeys.option_all_dungeon_keys:
        # Remove boss key consumption on boss keydoor opened (boss door behave like normal locked door)
        rom.write_word(0x1835e, 0x0000)